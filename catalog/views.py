from django.shortcuts import render
from catalog.models import Product, Contact

# Create your views here.


def home(request):
    list_of_products = Product.objects.all()

    a = 5 if len(list_of_products) >= 5 else len(list_of_products)

    [print(item) for item in list_of_products[:a]]

    return render(request, 'home.html')


def contacts(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        print('INPUT DATA: ', name)

    one_contact = Contact.objects.all()[0]
    data = {"first_name": one_contact.first_name, "last_name": one_contact.last_name}

    return render(request, 'contacts.html', context=data)


