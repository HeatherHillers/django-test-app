from django.urls import path
from .views import Inventory, PurchaseOrderView, MenuView  #, MenuDetailView, MenuDeleteView
urlpatterns = [
    path('', Inventory.as_view(), name='inventory'),
    path('purchase-orders/', PurchaseOrderView.as_view(), name='purchase-order-list'),
    path('menu/', MenuView.as_view(), name='menu-list'),
    path('inventory/', Inventory.as_view(), name='inventory'),
    #path('menu/<int:pk>/', MenuDetailView.as_view(), name='menu-detail'),
    #path('menu/delete/<int:pk>/', MenuDeleteView.as_view(), name='menu-delete'),
]
