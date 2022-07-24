# DRF Posts and Comments


# Requirements
Using the [Django REST Framework](https://www.django-rest-framework.org/), create an API that handles Posts and Comments. If you don't want to deal with users for this first challenge, that's fine.

The basic setup for any DRF project involves installing both Django and the Django REST Framework.  Don't forget to add `rest_framework` to your list of installed apps.

You will need to have the following files:
### Just like Django
1. `urls.py` to handle routes
2. `models.py` to handle your database

### Similar to Django
3. `views.py` to handle application logic (DRF has its own class-based views which look and feel like Django's)

### Different from Django
4. `serializers.py` to convert Python data into JSON and vice versa (DRF serializers look and feel like Django ModelForms)

You can interact with your API using DRF's built-in, and very nice interface, Postman, or good old-fashioned cURL.