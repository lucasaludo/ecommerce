from django.urls import path
from pedidos import views


urlpatterns = [
    path('add/', views.PedidoCreateView.as_view(), name='addpedido'),
    path('resumo/', views.ResumoPedidoTemplateView.as_view(), name='resumopedido'),
    path('meus-pedidos/', views.PedidoListView.as_view(), name='listar_pedidos'),  # Nova URL para listar pedidos
    path('pedido/<int:pk>/', views.PedidoDetailView.as_view(), name='detalhes_pedido'),  # Nova URL para detalhes do pedido
]