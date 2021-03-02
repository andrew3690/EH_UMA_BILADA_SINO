from django.urls import path
from . import views


app_name = 'main'
urlpatterns  = [
	path('', views.HomeView.as_view()),
	path('home/', views.HomeView.as_view(), name = 'home'),
    path('login/',views.LoginView.as_view(),name ='login'),
    path('logout/',views.LogoutRedirectView.as_view(),name = 'logout'),
    path('list/',views.EntregaListView.as_view(),name='entregas_lista'),
    path('list/<int:pk>/detail/',views.EntregaDetailView.as_view(),name='entrega_detail')
]
