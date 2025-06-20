from django.contrib import admin
from django.urls import path
from e_shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('index', views.index, name='index'),
    path('product/<int:id>', views.product, name='product-details'),
    path('cart/<int:id>', views.add_to_cart, name='cart'),
    path('view-cart', views.view_cart, name='view-cart'),
    path('contact', views.contact_view),
    path('remove-from-cart/<int:id>', views.remove_item_from_cart, name='remove-from-cart')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
