from django.contrib import admin
from .models import (Inventory, 
                     Menu, 
                     Ingredient, 
                     MenuItem, 
                     Recipe, 
                     RecipeIngredient,
                     InventoryItem, 
                     PurchaseOrder)
# Register your models here.
admin.site.register(Inventory)
admin.site.register(Menu)
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(InventoryItem)
admin.site.register(PurchaseOrder)  


