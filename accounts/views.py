from django.views import generic
from django.contrib.auth import logout
from django.views.generic import DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


from django.shortcuts import render

from .models import ProfileUser


def redirect_user(request):
    url = f'/branch/'
    return HttpResponseRedirect(url)

def logout_view(request):
    logout(request)
    url = f'/accounts/login/'
    return redirect_user(url)


class SignUp(generic.CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '//' # trqbva da sazdam homepage
    template_name = 'signup.html'




#ADMIN
def redirect_to_user_profile(request):
    if request.user.is_authenticated:
        user_profile = ProfileUser.objects.all().filter(user__pk=request.user.pk)[0]
        print(user_profile)
        redirect_url = f"{user_profile}/"
        return HttpResponseRedirect(redirect_to=redirect_url)


class UserProfile(DetailView):
    model = ProfileUser
    template_name = 'user_profile.html'
    context_object_name = 'user'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'signup.html'



