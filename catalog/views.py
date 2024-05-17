from django.shortcuts import render
from catalog.models import Product, Contact

# Create your views here.


def home(request):
    list_of_products = Product.objects.all()
    a = 5 if len(list_of_products) >= 5 else len(list_of_products)
    [print(item) for item in list_of_products[:a]]

    #[print(item.pk) for item in Product.objects.all()]

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

    data = {"product": Product.objects.get(pk=pk)}  # PrimaryKey (= 19, 20 ... 24)

    return render(request, 'catalog/product.html', context=data)

