from django.shortcuts import render

from phones.management.commands.import_phones import Command
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    Command.handle('self')
    params = request.GET.get('sort')
    if params == 'name':
        phones = Phone.objects.all().order_by('name')
    elif params == 'cheap':
        phones = Phone.objects.all().order_by('price')
    elif params == 'expensive':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug=slug)
    context = {'phones': phones.values()}
    return render(request, template, context)
