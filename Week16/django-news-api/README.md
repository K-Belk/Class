# Django News API

As a new developer you and your family have decided to become [digital nomads](https://www.investopedia.com/terms/d/digital-nomad.asp#:~:text=The%20Bottom%20Line-,What%20Is%20a%20Digital%20Nomad%3F,a%20company's%20headquarters%20or%20office.). As a result, you have taken on clients that need to develop web applications. Your first client has asked you to develop a proof of concept News Site.

The MVP (Minimal Viable Product) needs to have 2 core functions.

  1. Display Top Headlines from the U.S.
  2. Be able to search for a specific subject and display recent news about the subject

# Getting Started

Your application can have, but not limited to, one HTML template, 2 URL's, and only 2 view methods in order to meet the minimum requirements of the MVP.

Use the [NewsAPI](https://newsapi.org/) to retrieve/search for articles. Please make an account at [NewsAPI](https://newsapi.org/) to get an API Key. You'll need this API Key to successfully make GET requests (get a list of articles). **This API has great documentation. (NOTE: You DON'T need to use a Client Library!)**

Look over the following links on how to make HTTP requests to a 3rd party API:

  1. [Request](https://realpython.com/python-requests/)
  2. [Response](https://realpython.com/python-requests/#the-response)

  Example Request:
  ```py
  import requests as req
  
  # Making a get request to retrieve Top Headlines
  res = req.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={YOUR_API_KEY}')
  data = res.json()
  # pass your 'data' to your template
  ```

# User Requirements

1. When a user visits the url  `http://localhost:8000/news/` display all Top Headline news articles.
2. Have a search form that allows the user to type in a search query and click "Submit".
3. After a user clicks "Submit" display articles related to that search query.

# Release 0

Create a Django Project called `news_site` and Django App called `news`. You don't need to use a database for this application. We are just making requests to the NewsAPI and displaying the results on the screen.

# Release 1

**URLs**

- First, we need to register your news's URLs with the project's URLs:

```py
## urls.py
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
]
```

- Next, create `news/urls.py`:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # any other urls
]
```

# Release 2

**Create your view methods**

# Release 3

**Create your templates**

# Minimal Viable Product

### Home Page
![](https://github.com/ptcharlieplatoon/django-news-api/blob/main/news_api_1.png)

### Query Results
![](https://github.com/ptcharlieplatoon/django-news-api/blob/main/news_api_2.png)

# Get Creative!!
