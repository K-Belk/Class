
from django.urls import reverse
from django.shortcuts import render
from .models import  Group, Event
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model

User = get_user_model()

def all_groups(request):
    groups = Group.objects.all()
    return render(request, 'meetup_app/all_groups.html', {'groups': groups})

class GroupDetailView(DetailView):
    model = Group
    template_name = 'meetup_app/group_details.html'
    context_object_name='group'
    pk_url_kwarg = 'group_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = context['object'].users.all()
        context['events'] = context['object'].events.all()
        return context

def get_user(username):
    return User.objects.get(username=username)

class AddGroupView(CreateView):
    model = Group
    fields = ['title','users', 'description']
    success_url = '/meet/groups/'

    def form_valid(self, form):
        owner_username = self.request.user
        self.object = form.save(commit=False)
        self.object.owner = get_user(owner_username)
        print(self.object)
        self.object.save()
        return super().form_valid(form)

class GroupUpdateView(UpdateView):
    model = Group
    fields = '__all__'
    success_url = '/meet/groups/'

class GroupDeleteView(DeleteView):
    model = Group
    success_url = '/meet/groups/'

def get_group(group_id):
    return Group.objects.get(id=group_id)

class AddEventView(CreateView):
    model = Event
    fields = ['date', 'title', 'description', 'image_url']
    pk_url_kwarg = 'group_id'

    def form_valid(self, form):
        url_kwargs = self.kwargs
        self.object = form.save(commit=False)
        self.object.group = get_group(url_kwargs['group_id'])
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        url_kwargs = self.kwargs
        return reverse('meet:group_details', args=(url_kwargs['group_id'],) )

class EditEventView(UpdateView):
    model = Event
    fields = ['date', 'title', 'description', 'image_url']
    pk_url_kwarg = 'event_id'

    def form_valid(self, form):
        url_kwargs = self.kwargs
        self.object = form.save(commit=False)
        self.object.group = get_group(url_kwargs['group_id'])
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        url_kwargs = self.kwargs
        return reverse('meet:group_details', args=(url_kwargs['group_id'],) )

class DeleteEventView(DeleteView):
    model = Event
    pk_url_kwarg = 'event_id'

    def get_success_url(self) -> str:
        url_kwargs = self.kwargs
        return reverse('meet:group_details', args=(url_kwargs['group_id'],) )

