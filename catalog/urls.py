from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactView, ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, VersionCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('<int:pk>/all_products/', ProductListView.as_view(), name='products'),
    path('<int:pk>/product_info/', ProductDetailView.as_view(), name='product_info'),
    path('createproduct/', ProductCreateView.as_view(), name='create_product'),
    path('updateproduct/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
path('createversion/', VersionCreateView.as_view(), name='create_version')
]
