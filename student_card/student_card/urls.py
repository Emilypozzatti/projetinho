
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import StudentCardViewSet

router = DefaultRouter()
router.register(r'cards', StudentCardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]


