from django.urls import path
from .views import(
	product_detail_view,
	product_create_view,
	product_list_view
)

app_name = 'products'
urlpatterns = [
	path('', product_list_view, name='product-list'),
	path('create/', product_create_view, name='product-create'),
	path('<int:id>/', product_detail_view, name='product-detail'),
	#path('products/<int:id>/', dynamic_lookup_view, name='product-detail'),
]