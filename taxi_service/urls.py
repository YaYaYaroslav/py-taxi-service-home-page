from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('taxi/', include('taxi.urls', namespace='taxi')),
    path('', include('taxi.urls', namespace='taxi')),  # Додаємо кореневий шлях
]
