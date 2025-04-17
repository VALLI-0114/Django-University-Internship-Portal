from django.contrib import admin
from django.urls import path, include  # Include is needed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),  # Ensure this includes `base.urls`
]
