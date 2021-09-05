from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    parm = request.GET['sort']
    if parm == 'by_name':
        phones = Phone.objects.all().order_by('name')

    elif parm == 'max_price':
        phones = Phone.objects.all().order_by('price')

    elif parm == 'min_price':
        phones = Phone.objects.all().order_by('-price')

    else: 
        phones = Phone.objects.all()

    template = 'catalog.html'
    
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)

