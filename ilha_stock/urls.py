from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('categories/', include('categories.urls', namespace='categories')),
    path('brands/', include('brands.urls', namespace='brands')),
    path('products/', include('products.urls', namespace='products')),
    path('stock/', include('stock.urls', namespace='stock')),
]
