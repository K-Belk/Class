from pyexpat import model
from .models import Product
from django.db.models import Avg, Max
from django.db.models.functions import Length


class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod
    def find_by_model(cls, model_name):
        return Product.objects.get(model__exact = model_name)

    @classmethod
    def last_record(cls):
        return Product.objects.order_by().last()
    
    @classmethod
    def by_rating(cls, rating):
        return Product.objects.filter(rating__exact = rating)

    @classmethod
    def by_rating_range(cls, low_rating, high_rating):
        return Product.objects.filter(rating__range=(low_rating, high_rating))

    @classmethod
    def by_rating_and_color(cls, rating, color):
        return Product.objects.filter(rating__exact = rating, color__exact = color)

    @classmethod
    def by_rating_or_color(cls, rating, color):
        return Product.objects.filter(rating__exact = rating) | Product.objects.filter(color__exact = color)

    @classmethod
    def no_color_count(cls):
        return len(Product.objects.filter(color__exact = None))
    
    @classmethod
    def below_price_or_above_rating(cls, price, rating):
        return Product.objects.filter(price_cents__lt = price) | Product.objects.filter(rating__gt = rating)

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.order_by('category', '-price_cents') 

    @classmethod
    def products_by_manufacturer_with_name_like(cls, str):
        return Product.objects.filter(manufacturer__contains = str)

    @classmethod
    def manufacturer_names_for_query(cls, query):
        return [name.manufacturer for name in Product.objects.filter(manufacturer__contains = query)]

    @classmethod
    def not_in_a_category(cls, product):
        return Product.objects.exclude(category__exact = product)

    @classmethod
    def limited_not_in_a_category(cls, product, limit):
        return Product.objects.exclude(category__exact = product)[:limit]

    @classmethod
    def category_manufacturers(cls, category):
        return [result.manufacturer for result in Product.objects.filter(category__exact = category)]

    @classmethod
    def average_category_rating(cls, category):
        return Product.objects.filter(category__exact = category).aggregate(Avg('rating'))

    @classmethod
    def greatest_price(cls):
        return Product.objects.aggregate(Max('price_cents'))

    @classmethod
    def longest_model_name(cls):
        return Product.objects.order_by('model')[:1][0].id

    @classmethod 
    def ordered_by_model_length(cls):
        # values list

        return [result.id for result in Product.objects.order_by(Length('model'))]