from django.shortcuts import render, get_object_or_404
from .models import Phone

def phone_catalog(request):
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'price_asc':
        phones = Phone.objects.all().order_by('price')
    elif sort_by == 'price_desc':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all().order_by('name')
    return render(request, 'catalog.html', {'phones': phones})

def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'phone_detail.html', {'phone': phone})
