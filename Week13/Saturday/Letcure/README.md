Saturday, April 2, 2022
====================
### Video Resources from Previous Cohorts
- [Videos](https://www.youtube.com/channel/UCASZ7zW_Egu0T4KG3YEdGfw/playlists)


### Lecture Topics
- Full-Stack Django


# CRUD in Django
The majority of code you write professionally for the web will actually share a striking familiarity: it will be focused on performing the same handful of operations on a record in the database. There are a million tiny variations on how this will happen, but at the core, there are only four major operations we'll perform on our data.

In the web world we call this a CRUD app. That is, it has four essential functions:

1. Creating new records
2. Retrieving records
3. Updating existing records
4. Deleting existing records

Twitter is a CRUD app. Instagram is a CRUD app. Salesforce is a CRUD app, and so is Amazon. This pattern is so important, that we're going to spend a big chunk of our week praticing building them. You need to be able to write a simple CRUD interface from memory quickly, so that you can focus on the individual features that differentiate each product.

A huge shoutout to [Rayed](https://rayed.com/posts/2018/05/django-crud-create-retrieve-update-delete/) for providing us with this tutorial and helping our community!

## Setup
Today, we're going to create a CRUD app for books in a books. Let's start by setting up our project and app:
```bash
$ mkdir library_project
$ cd library_project
$ python -m venv venv
$ source venv/bin/activate
$ pip install django
$ django-admin startproject library
$ cd library
$ python manage.py startapp books
```
We have a project called `library` and an app called `books`. Remember that a project can have many apps and an app can be ported into many projects. Picture Amazon's business model. Amazon has many sources of revenue/business (`projects` in Django). Each one of those `projects` has different apps that it uses. For example, Amazon Video Streaming allows you to order on-demand videos using a `video` app. They will then charge you using their `orders` app and associate a digital order with your account. That same `orders` app associates physical orders with your account and charges you just the same.

In our example `library` project, there's a `books` app that keeps track of all our books.

To register our app with our project, we need to add it to `library/settings.py`:
```python
INSTALLED_APPS = [
    ...,
    'books',
]
```

Next, we need to create the Model (Python class that connects directly into the database) in `books/models.py`:
```python
from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField()
    def __str__(self):
        return f"ID: {self.id} Title: {self.title}"
```

Our Book model has a book `title` and a number of `pages`. Let's create the migration and migrate it to the database:

```bash
$ ./manage.py makemigrations
$ ./manage.py migrate
```

Once we've got that in the database, let's create a new file `books/urls.py` and inside it, define the possible routes a user can go to:
```python
from django.urls import path
from . import views
app_name = 'books'
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:book_id>', views.book_view, name='book_view'),
    path('new', views.book_create, name='book_new'),
    path('edit/<int:book_id>', views.book_update, name='book_edit'),
    path('delete/<int:book_id>', views.book_delete, name='book_delete'),
]
```

These routes are registered under the application, but we need to associate it back with the project in `library/urls.py`:

```python
# add this on top
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
]
```

Next, in our `books/views.py`, we need to create the controller code that will do all the heavy lifting once a user actually hits a URL in `books/urls.py`:

```python
from django.shortcuts import render, redirect
from django.forms import ModelForm
from books.models import Book
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pages']
def get_book(book_id):
  return Book.objects.get(id=book_id)
def book_list(request):
    books = Book.objects.all()
    data = {'all_books': books}
    return render(request, 'books/book_list.html', data)
def book_view(request, book_id):
    book = get_book(book_id)
    data = {'book': book}
    return render(request, 'books/book_detail.html', data)
def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('books:book_list')
    return render(request, 'books/book_form.html', {'form': form, 'new_or_edit': 'New'})
def book_update(request, book_id):
    book = get_book(book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books:book_list')
    return render(request, 'books/book_form.html', {'form' :form, 'new_or_edit': 'Edit'})
def book_delete(request, book_id):
    book = get_book(book_id)
    if request.method=='POST':
        book.delete()
        return redirect('books:book_list')
    return render(request, 'books/book_confirm_delete.html', {'object':book})
```

Finally, let's create the templates themselves so that we have code to look at on the screen. We'll be creating 4 views:
1. `books/templates/books/book_list.html`
```html
<h1>Books</h1>

<table border="1">
  <thead>
    <tr>
      <th>Title</th>
      <th>Pages</th>
      <th>View</th>
      <th>Edit</th>
      <th>Delete</th>
    </tr>
  </thead>
  <tbody>
    {% for book in all_books %}
      <tr>
        <td>{{ book.title }}</td>
        <td>{{ book.pages }}</td>
        <td><a href="{% url 'books:book_view' book.id %}">view</a></td>
        <td><a href="{% url 'books:book_edit' book.id %}">edit</a></td>
        <td><a href="{% url 'books:book_delete' book.id %}">delete</a></td>
      </tr>
    {% endfor %}
  </tbody>
</table>

<a href="{% url 'books:book_new' %}">New</a>
```
2. `books/templates/books/book_detail.html`
```html
<h1>Book Details</h1>
<h2>Title: {{ book.title }}</h2>
Pages: {{ book.pages }}
<hr/>
<a href="{% url 'books:book_list' %}">Back</a>
```

3. `books/templates/books/book_form.html`
```html
<h1>Book Form: {{ new_or_edit }}</h1>
<form method="post">{% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="Submit" />
</form>
```

4. `books/templates/books/book_confirm_delete.html`
```html
<h1>Book Delete</h1>
<form method="post">{% csrf_token %}
  Are you sure you want to delete "{{ object.title }}" ?
  <input type="submit" value="Submit" />
</form>
```

Lastly, run `$ ./manage.py runserver` from your command line and see your work!

## Forms in Django
Django is an opinionated framework, meaning that the core development team has implemented their opinions in the creation of the framework. We see an example of that with Django Forms - there's a lot of magic happening, almost to the point where it's too simple. The decision to make forms super simple in Django was made because the creators of Django believe that developers have better things to do than to create basic forms all day.

Online forms within web applications consist of two things:
1. The HTML form displayed on the screen
2. The processing of data (saving what you type into a database or sending the data somewhere else)

Under the hood of Django, these two essential things are still happening. Let's start with how the form is created and how it's saved in `views.py`:

```python
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pages']
```

Here, we have `BookForm`, a class that inherits from Django's `ModelForm`. Through this inheritance, `BookForm` has all the functionality of `ModelForm` - the class that Django uses to create a form for a model in an application. In its subclass `Meta`, we tell `ModelForm` that the model we want to read/write to is `Book` and that the fields that we want to collect are `title` and `pages`. From this information, Django makes the assumption that whenever you receive data via the `BookForm`, you want to read/write to the `Book` table in your database and will read/write data for you.

From here, Django takes the `BookForm` object that you create and passes it into the appropriate `template` as `form`. In our template file, we see code that looks a bit foreign: `{{ form.as_p }}`. This code interpolates the form object into HTML code that we can interact with on screen.
