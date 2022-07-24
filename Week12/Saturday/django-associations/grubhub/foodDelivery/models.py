from django.db import models

class User(models.Model):
    pass


class Restaurant(models.Model):
    pass


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='orders')


class FoodItem(models.Model):
    pass

    orders = models.ManyToManyField(
        Order, through='OrderFoodItem', related_name='food_items')


class OrderFoodItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE)
    food_item = models.ForeignKey(
        FoodItem, on_delete=models.CASCADE, related_name='food_items')