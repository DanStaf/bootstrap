import django.core.exceptions
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
# import catalog.models
from catalog.models import Product, Contact, Article, Version, Category
from catalog.forms import ProductForm, VersionForm, ProductDescriptionForm, ProductCategoryForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.forms import inlineformset_factory

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from catalog.services import get_category_list


class ContactListView(ListView):
    model = Contact


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    login_url = "/users/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ...
        context['object_list'] = get_category_list()
        return context


###


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    login_url = "/users/login/"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    login_url = "/users/login/"


class ProductCreateUpdate(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # Формирование формсета
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form, object_is_new=True):
        context_data = self.get_context_data()
        formset = context_data['formset']

        if form.is_valid() and formset.is_valid():
            self.object = form.save()

            if object_is_new:
                self.object.owner = self.request.user
                self.object.save()

            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:

            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductCreateView(LoginRequiredMixin, ProductCreateUpdate, CreateView):
    login_url = "/users/login/"

    def form_valid(self, form, *args):
        return super().form_valid(form, True)


def check_user_is_owner_or_su(self):
    pk = self.kwargs.get('pk')
    product = get_object_or_404(Product, pk=pk)
    return (self.request.user == product.owner) or self.request.user.is_superuser


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, ProductCreateUpdate, UpdateView):
    login_url = "/users/login/"

    def form_valid(self, form, *args):
        return super().form_valid(form, False)

    def test_func(self):
        return check_user_is_owner_or_su(self)


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    login_url = "/users/login/"

    def test_func(self):
        return check_user_is_owner_or_su(self)


@permission_required('set_published')
def product_publish(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if product is None:
        return render(request, 'catalog/404.html')
    else:

        product.is_published = False if product.is_published else True
        product.save()

        return redirect('catalog:home')


class ProductDescriptionUpdateView(PermissionRequiredMixin, ProductUpdateView):
    login_url = "/users/login/"
    permission_required = 'change_description'
    form_class = ProductDescriptionForm

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])

    def test_func(self):
        return True


class ProductCategoryUpdateView(PermissionRequiredMixin, ProductUpdateView):
    login_url = "/users/login/"
    permission_required = 'change_category'
    form_class = ProductCategoryForm

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])

    def test_func(self):
        return True


###


class ArticleListView(ListView):
    model = Article

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_qty += 1
        self.object.save()

        if self.object.views_qty == 100:
            print(f'''C O N G R A T U L A T I O N S ! ! ! ! !
the Article "{self.object.title}" reached 100 views!
''')

        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'photo',)
    success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'photo', 'is_published')
    # success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view_article', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('catalog:blog')

###########
