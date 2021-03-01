from django.shortcuts import render,get_object_or_404
# from django.views import ListView
# from .views import ListView,DetailView
from .models import Product,Category


# Create your views here.
    # def get_list_product(requets):
    #     list_product = Product.objects.all()
    #     # list_category = Category.objects.all()
    #     products = {'listproducts':list_product}
    #     # categories = {'listcategories':list_category}
    #     return render(request,'pages/index.html',products)
def product_list(request, category_slug=None):
    category_id = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'pages/index.html',{'category_id': category_id,'categories': categories,'products': products})
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
    id=id,
    slug=slug,)
    return render(request,'pages/product_detail.html',{'product': product}) 
# def create(self, request, *args, **kwargs):
#     ProductImage = serializer.save()

#     image_list = request.FILES.getlist('image_path')
#     for item in image_list: 
#         images = Images.objects.create(Product=Product, photo=item)
#         images.save()
#     return Response(serializer.data)


# from django.http import HttpResponse
# def query_image_of_product(request, *args, **kwargs):
#     data = Product.objects.all()
#     for p in data:
#         print(p.images)
#         for pp in p.images:
#             print(pp.images)
#     # print(data)
#     html = "<html><body>{% for p in data %} <tr>{{p}}</tr> {% endfor %}</body></html>" % data
#     return HttpResponse(html)