import django.core.exceptions
from django.shortcuts import render
# import catalog.models
from catalog.models import Product, Contact

# Create your views here.


def home(request):
    list_of_products = Product.objects.all()
    a = 5 if len(list_of_products) >= 5 else len(list_of_products)
    [print(item) for item in list_of_products[:a]]

    # [print(item.pk) for item in Product.objects.all()]

    data = {"objects": list_of_products}

    return render(request, 'catalog/home.html', context=data)


def contacts(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        print('INPUT DATA: ', name)

    our_contacts = Contact.objects.all()
    data = {"our_contacts": our_contacts}

    return render(request, 'catalog/contacts.html', context=data)


def product(request, pk):

    product = get_object_or_None(Product, pk)  # PrimaryKey (= 19, 20 ... 24)

    if product is None:
        return render(request, 'catalog/404.html')
    else:

        data = {"product": product}
        return render(request, 'catalog/product.html', context=data)


def get_object_or_None(My_Model, pk):

    try:
        return My_Model.objects.get(pk=pk)
    except django.core.exceptions.ObjectDoesNotExist:
        return None
