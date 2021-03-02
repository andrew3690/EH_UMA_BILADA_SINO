from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('listing/',views.Listing.as_view(),name ='listing'),
    path('listing/A_la_carte',views.A_la_carte_view.as_view(),name = 'a_la_carte'),
    path('listing/Delivery',views.Delivery_view.as_view(),name = 'delivery'),
    path('listing/Rodizio',views.Rodizio_view.as_view(),name = 'rodizio')
]