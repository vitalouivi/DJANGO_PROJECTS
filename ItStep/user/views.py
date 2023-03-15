from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView
from .models import User
from .forms import UserForm


class UserAddView(FormView):
    template_name = 'user/create.html'
    form_class = UserForm
    initial = {
        'slug': 'login',
        'name': 'name',
        'surname': 'surname',
        'date_of_birth': '01/01/1999',
        'email': 'mail@mail.ru',
        'telephone': '+7(---)--- -- --'
    }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['users'] = User.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        #return reverse('user:user-info', kwargs={'username': self.object.cleaned_data['username']})
        return reverse('user:index')


class UserListView(ListView):
    template_name = 'user/index.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


class UserDetailView(DetailView):
    template_name = 'user/user.html'
    model = User
    context_object_name = "user"


def login(request):
    return render(request, 'user/login.html')




