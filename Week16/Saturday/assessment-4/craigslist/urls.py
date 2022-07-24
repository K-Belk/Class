from django.urls import path
from . import views



urlpatterns = [
    path('', views.CategoriesListView.as_view(), name='all_categories'), # - `/categories`: A page listing all the categories
    path('new/', views.AddCategoryView.as_view(), name='add_category'), # - `/categories/new`: A page with a form to create a new category
    path('<int:category_id>/', views.CategoryDetailView.as_view(), name='category_details'), # - `/categories/:category_id`: A page to view the detail of a specific category and a list of all of its associated posts
    path('<pk>/edit/', views.CategoryUpdateView.as_view(), name='update_category'), # - `/categories/:category_id/edit`: A page with a form to update a specific category, with current values filled in already. 
    path('<pk>/delete/', views.CategoryDeleteView.as_view(), name='delete_category'), # Also include the ability to delete the specific category here.
    path('<int:category_id>/posts/new/', views.AddPostView.as_view(), name='add_post'), # - `/categories/:category_id/posts/new`: A page with a form to create a new post, under the current category by default.
    path('<int:category_id>/posts/<int:post_id>/', views.PostDetailView.as_view(), name='post_detail'), # - `/categories/:category_id/posts/:post_id`: A page to view the detail of a specific post. Also include the ability go back to the parent category detail page (`/categories/:category_id/`)
    path('<int:category_id>/posts/<pk>/edit/', views.PostUpdateView.as_view(), name='update_post'), # - `/categories/:category_id/posts/:post_id/edit`: A page with a form to update a specific post, with current values filled in already. 
    path('<int:category_id>/posts/<pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'), # Also include the ability to delete the specific post here.
    ]




