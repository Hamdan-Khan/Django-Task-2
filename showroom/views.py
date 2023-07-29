from django.shortcuts import render
from .models import Brand, Staff, CarModel


def BrandsListView(request):
    brands = Brand.objects.all()
    return render(request, 'showroom/brands_list.html', {'brands': brands})


def BrandDataView(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    models = CarModel.objects.filter(brand=brand)
    return render(request, 'showroom/brand_data.html', {'brand': brand, 'models': models})


def TeamView(request):
    staff = Staff.objects.all()
    return render(request, 'showroom/team.html', {'staff': staff})
