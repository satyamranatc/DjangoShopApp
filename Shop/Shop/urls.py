from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include("HomePage.urls")),
    path('Products/', include("Products.urls")),
    path('admin/', admin.site.urls),
]
