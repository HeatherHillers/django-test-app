from django.db import models



class Inventory(models.Model):
    # inventory of ingredients
    # ingredient, units in stock
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    units = models.FloatField(help_text="Units in stock")

    def __str__(self):
        return f"{self.ingredient.name}: {self.units}"

class Menu(models.Model):
    # menu for a specific date
    # date, items (many-to-many with MenuItem)
    date = models.DateField()
    items = models.ManyToManyField('MenuItem')
    def __str__(self):
        return f"Menu for {self.date}"
    
class Ingredient(models.Model):
    # name, units, cost per unit (cpu)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    cpu = models.FloatField(help_text="Cost per unit")

    def __str__(self):
        return f"{self.name} ({self.cpu}€ per {self.unit})"
    
class MenuItem(models.Model):
    # meal entry in the menu
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField()
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    instructions = models.TextField()

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    units = models.FloatField()

    def __str__(self):
        return f"{self.units} of {self.ingredient.name} for {self.recipe.name}"

class InventoryItem(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    units = models.FloatField()

    def __str__(self):
        return f"{self.ingredient.name}: {self.units}"

class PurchaseOrder(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.FloatField()
    order_date = models.DateField(auto_now_add=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order for {self.quantity} of {self.menu_item.name} on {self.order_date}"
    
    def cost(self):
        # total cost based on recipe ingredients and their cpu
        total_cost = 0
        for ri in self.menu_item.recipe.recipeingredient_set.all():
            total_cost += ri.units * ri.ingredient.cpu
        return total_cost * self.quantity
    
    def price(self):
        # total price based on menu item price
        return self.menu_item.price * self.quantity