from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.product_mixin_view),
    path("create/", views.product_mixin_view),
    path("<int:pk>/", views.product_mixin_view),
    path("<int:pk>/update/", views.product_mixin_view),
    path("<int:pk>/delete/", views.product_mixin_view),
    path("listcreate/", views.product_list_create_view),
]
