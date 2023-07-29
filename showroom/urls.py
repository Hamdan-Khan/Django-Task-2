from django.urls import path
from . import views

app_name = "showroom"

urlpatterns = [
    path("", views.BrandsListView, name="brands_list"),
    path("<int:brand_id>", views.BrandDataView, name="brand_data"),
    path("team/", views.TeamView, name='team_view')
]
