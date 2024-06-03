import django.core.exceptions
from django.shortcuts import render
# import catalog.models
from catalog.models import Product, Contact, Article

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

# Create your views here.


class ProductListView(ListView):
    model = Product


"""def home(request):
    list_of_products = Product.objects.all()
    a = 5 if len(list_of_products) >= 5 else len(list_of_products)
    [print(item) for item in list_of_products[:a]]

    # [print(item.pk) for item in Product.objects.all()]

    data = {"object_list": list_of_products}

    return render(request, 'catalog/product_list.html', context=data)"""


class ContactListView(ListView):
    model = Contact


"""def contacts(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        print('INPUT DATA: ', name)

    our_contacts = Contact.objects.all()
    data = {"object_list": our_contacts}

    return render(request, 'catalog/contact_list.html', context=data)"""


class ProductDetailView(DetailView):
    model = Product


"""def product(request, pk):

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
