from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from .models import InventoryItem, PurchaseOrder, MenuItem
# Create your views here.

class Inventory(ListView):
    model = InventoryItem
    paginate_by = 10
    template_name = 'inventory/inventory_list.html'
    # alias for the list in the template
    context_object_name = 'inventory_items'

class MenuView(ListView):
    model = MenuItem
    paginate_by = 10
    template_name = 'inventory/menu_list.html'
    context_object_name = 'menus'

# class DeleteInventoryItem(DeleteView):
#     model = InventoryItem
#     success_url = '/inventory/'

class PurchaseOrderView(ListView):
    model = PurchaseOrder
    template_name = 'inventory/purchase_order_list.html'
    context_object_name = 'purchase_orders'

    def profit(self):
        return self.revenue() - self.cost()
    
    def revenue(self):
        return sum(po.price() for po in self.get_queryset())
    
    def cost(self):
        return sum(po.cost() for po in self.get_queryset())

