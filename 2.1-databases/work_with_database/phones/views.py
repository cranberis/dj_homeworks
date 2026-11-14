from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    match sort:
        case 'name':
            phones = Phone.objects.all().order_by('name')
        case 'min_price':
            phones = Phone.objects.all().order_by('price')
        case 'max_price':
            phones = Phone.objects.all().order_by('-price')
        case _:
            phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
