from django.urls import path
from . import views


app_name = 'management'
urlpatterns  = [
    path('login/',views.LoginView.as_view(),name ='login'),
    path('home/',views.HomeView.as_view(),name = 'home'),
    path('logout/',views.LogoutRedirectView.as_view(),name = 'logout'),
    path('list/',views.AddressListView.as_view(),name='address_list'),
    path('list/<int:pk>/detail/',views.AddressDetailView.as_view(),name='address_detail')
]

'''
    path('create/',views.AddressCreateView.as_view(),name='address_create'),
    path('list/<int:pk>/update/',views.AddressUpdateView.as_view(),name = 'address_update'),
    path('list/<int:pk>/destroy/',views.AddressDestroyView.as_view(),name = 'address_destroy')
    '''