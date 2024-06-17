import django.core.exceptions
from django.shortcuts import render
# import catalog.models
from catalog.models import Product, Contact, Article, Version
from catalog.forms import ProductForm, VersionForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.forms import inlineformset_factory

# Create your views here.


class ContactListView(ListView):
    model = Contact


###


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
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

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']

        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:

            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductUpdateView(UpdateView):
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

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']

        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:

            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


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

"""# FBV ProductListView

def home(request):
    list_of_products = Product.objects.all()
    a = 5 if len(list_of_products) >= 5 else len(list_of_products)
    [print(item) for item in list_of_products[:a]]

    # [print(item.pk) for item in Product.objects.all()]

    data = {"object_list": list_of_products}

    return render(request, 'catalog/product_list.html', context=data)"""



"""# FBV ProductDetailView

def product(request, pk):

    product = get_object_or_None(Product, pk)  # PrimaryKey (= 19, 20 ... 24)

    if product is None:
        return render(request, 'catalog/404.html')
    else:

        data = {"object": product}
        return render(request, 'catalog/product_detail.html', context=data)


def get_object_or_None(My_Model, pk):

    try:
        return My_Model.objects.get(pk=pk)
    except django.core.exceptions.ObjectDoesNotExist:
        return None
"""


"""# FBV ContactListView

def contacts(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        print('INPUT DATA: ', name)

    our_contacts = Contact.objects.all()
    data = {"object_list": our_contacts}

    return render(request, 'catalog/contact_list.html', context=data)"""
