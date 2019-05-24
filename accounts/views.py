from django.shortcuts import render
from .forms import UserForm,ProfileUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

'''for delete profiles'''
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

'''CUSTOM IMPORTS'''
from django.contrib.auth.models import User
from django.views.generic import DetailView
from .models import ProfileUser

def index(request):
    return render(request,'index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileUserForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileUserForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('redirect-user-detail'))
            else:
                return HttpResponse("Your account was inactive.")
        else:

            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            #return HttpResponse("Invalid login details given")
            return render(request, 'registration.html', {})
    else:
        return render(request, 'login.html', {})


'''CUSTOM VIEWS'''
def redirect_to_user_profile(request):
    if request.user.is_authenticated:
        print(request.user.pk)
        user = ProfileUser.objects.get(user_id=request.user.id)
        print(user.id)
        redirect_url = f"{user.id}/"
        return HttpResponseRedirect(redirect_to=redirect_url)


class UserProfile(DetailView):
    model = ProfileUser
    template_name = 'user_profile.html'
    context_object_name = 'user_profile'

'''DELETE PROFILES'''

def has_access_to_delete(current_user, item):
    if current_user.is_superuser:
        return True
    #elif current_user.id == item.user.id: item id nqma da se izpolzva
     #   return True
    return False

class ProfileDelete(LoginRequiredMixin, generic.DeleteView):
    model = ProfileUser
    login_url = 'accounts/login/'
    context_object_name = 'item'

    def get(self, request, pk):
        if not has_access_to_delete(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        return render(request, 'Item_delete.html', {'item': self.get_object()})

    def post(self, request, pk):
        if not has_access_to_delete(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        print(self.get_object())
        user = User.objects.get(username=self.get_object())
        user.delete()
        return HttpResponseRedirect('')


'''EDIT PROFILE'''
def has_access_to_edit(current_user, item):
    if current_user.is_superuser:
        return True
    elif current_user.id == item.user.id:
        return True
    return False

