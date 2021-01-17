from django.urls import path
from . import views


app_name = 'management'
urlpatterns  = [
    path('login/',views.login,name = 'login'),
    path('home/',views.home,name ='home'),
    path('logout/',views.logout,name = 'logout'),
    path('list/',views.address_list,name = 'address_list'),
    path('create/',views.create,name='address_create'),
    path('list/<int:id>/update/',views.update,name = 'address_update'),
    path('list/<int:id>/destroy/',views.destroy,name = 'address_destroy'),
]