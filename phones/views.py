from django.shortcuts import render

from phones.management.commands.import_phones import Command
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    Command.handle('self')
    phones = Phone.objects.all()
    context ={}
    context['phones'] = phones
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    phones = Phone.objects.all()
    content = phones.filter(slug=slug)
    context['phones'] = content.values()

    return render(request, template, context)
