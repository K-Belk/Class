from django.urls import reverse
from .models import Categories, Posts
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

def _get_category(category_id):
    return Categories.objects.get(id=category_id)

class CategoriesListView(ListView):
    model = Categories
    context_object_name = 'categories'

class AddCategoryView(CreateView):
    model = Categories
    fields = '__all__'
    success_url = '/categories/'

class CategoryDetailView(DetailView):
    model = Categories
    context_object_name = 'category'
    pk_url_kwarg = 'category_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['object'].posts.all()
        return context

class CategoryUpdateView(UpdateView):
    model = Categories
    fields = '__all__'
    success_url = '/categories/'

class CategoryDeleteView(DeleteView):
    model = Categories
    success_url = '/categories/'

class AddPostView(CreateView):
    model = Posts
    fields = ['title', 'description']
    pk_url_kwarg = 'category_id'

    def form_valid(self, form):
        url_kwargs = self.kwargs
        self.object = form.save(commit=False)
        self.object.category = _get_category(url_kwargs['category_id'])
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        url_kwargs = self.kwargs
        return reverse('category_details', args=(url_kwargs['category_id'],))

class PostDetailView(DetailView):
    model = Posts
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

class PostUpdateView(UpdateView):
    model = Posts
    fields = ['title', 'description']
    pk_url_kwargs = 'post_id'

    def form_valid(self, form):
        url_kwargs = self.kwargs
        self.object = form.save(commit=False)
        self.object.category = _get_category(url_kwargs['category_id'])
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        url_kwargs = self.kwargs
        return reverse('category_details', args=(url_kwargs['category_id'],))

class PostDeleteView(DeleteView):
    model = Posts
    pk_url_kwargs = 'post_id'

    def get_success_url(self) -> str:
        url_kwargs = self.kwargs
        return reverse('category_details', args=(url_kwargs['category_id'],))