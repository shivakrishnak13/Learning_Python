from django.urls import path
from . import views

urlpatterns = [
    path("add-dish/",views.add_dish,name='add_dish'),
    path("home/",views.home,name='home'),
    path("update/<int:id>/",views.update,name='update'),
    path("delete/<int:id>/",views.delete,name='delete'),
    path('order/<int:id>/',views.place_order,name='order'),
    path('update_status/<int:id>/',views.update_status,name='update_status'),
]