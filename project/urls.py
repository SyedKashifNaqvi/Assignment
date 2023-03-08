from django.contrib import admin
from django.urls import path, include
from app.views import product_report
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('product_report/', product_report, name="product_report")
]
