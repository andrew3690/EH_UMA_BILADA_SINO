from django.urls import path, include
from . import views


app_name = 'main'

gerenciador_patterns = [
    path("", views.HomeGerenciadorView.as_view(), name = "gerenciador_home"),
    path("entregas/", views.EntregaGerListView.as_view(), name = "gerenciador_entregas"),
    path("funcionarios/", views.FuncionarioGerListView.as_view(), name = "gerenciador_funcionarios"),
    path("veiculos/", views.VeiculoGerListView.as_view(), name = "gerenciador_veiculos"),
    path("objetos/", views.ObjetoGerListView.as_view(), name = "gerenciador_objetos"),
    path("enviar/<int:pk>", views.EnviarEntrega, name = "gerenciador_enviar_entrega"),

    path("create_funcionario/", views.CreateFuncionarioView.as_view(), name = "create_funcionario"),
    path("create_objeto/", views.CreateObjetoView.as_view(), name = "create_objeto"),
    path("create_veiculo/", views.CreateVeiculoView.as_view(), name = "create_veiculo"),
    path("create_entrega/", views.CreateEntregaView.as_view(), name = "create_entrega"),
    
]

urlpatterns  = [
	path('', views.HomeView.as_view()),
	path('home/', views.HomeView.as_view(), name = 'home'),
    path('login/',views.LoginView.as_view(),name ='login'),
    path('logout/',views.LogoutRedirectView.as_view(),name = 'logout'),
    path('list/',views.EntregaListView.as_view(),name='entregas_lista'),
    path('list/<int:pk>/detail/',views.EntregaDetailView.as_view(),name='entrega_detail'),
    path('list/<int:pk>/detail/produtos',views.EntregaDetailProdutosView.as_view(),name='entrega_detail_produtos'),
    path('list/<int:pk>/detail/funcionarios',views.EntregaDetailFuncionariosView.as_view(),name='entrega_detail_funcionarios'),
    path('gerenciador/', include(gerenciador_patterns))
]
