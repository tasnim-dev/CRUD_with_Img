from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from AppCrud import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homePage, name="homePage"),
    path("updatePage/", views.updatePage, name="updatePage"),
    path("deletePage/", views.deletePage, name="deletePage"),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
