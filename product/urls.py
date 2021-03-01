from django.urls import path
from.import views

app_name = 'product'
urlpatterns = [
    path('',views.product_list ,name='listview'),
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
    # path(r'query_image_of_product', views.query_image_of_product, name='query_image_of_product')
]
