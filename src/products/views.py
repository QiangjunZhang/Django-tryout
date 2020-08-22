from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm


# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {'objects': obj
    }
    return render(request, "product/product_detail.html", context)


def product_create_view(request):
    form = RawProductForm(request.POST)
    # print(request.POST.get('title'))
    context = {'form': form}
    return render(request, "product/product_create.html", context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {'form': form
#     }
#     return render(request, "product/product_create.html", context)