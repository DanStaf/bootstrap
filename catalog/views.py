from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def contacts(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        print('INPUT DATA: ', name)

    return render(request, 'contacts.html')


