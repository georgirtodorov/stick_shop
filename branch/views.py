from django.shortcuts import render
from django.views import generic
from .models import MagicWand, Survachki, Fetchers, Stick
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import ProfileUser , User
from collections.abc import Iterable
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers


from .forms import CreateMagicWandForm, CreateFetchersForm, CreateSurvachkiForm

def serialize_data(queryset):
    if isinstance(queryset, Iterable):
        return serializers.serialize('json', queryset)
    else:
        return serializers.serialize('json', [ queryset ])

# Create your views here.
def has_access_to_modify(current_user, item):
    if current_user.is_superuser:
        return True
    elif current_user.id == item.user.id:
        return True
    return False

'''PRODUCT DETAILS '''

'''USER STICKS'''

class UserStickList(LoginRequiredMixin, generic.ListView):
    model = Stick
    template_name = 'stick_list.html'
    context_object_name = 'stick'

    def get_queryset(self):
        user_id = int(self.request.user.id)

        try:
            user = ProfileUser.objects.all().filter(user__pk=user_id)[0]
            sticks = Stick.objects.all().filter(user = user.pk)
            return sticks
        except:
            return []


class StickList(generic.ListView):
    model = Stick
    template_name = 'survachki_list.html'
    context_object_name = 'survachki'


    '''CREATE FORMS'''

def stick_create_options(request):
    return render(request, 'stick_create_options.html')


class MagicWandCreate(LoginRequiredMixin, generic.CreateView):

    model = MagicWand
    template_name = 'Item_create.html'
    form_class = CreateMagicWandForm
    success_url = '/admin/'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)


class FetchersCreate(LoginRequiredMixin, generic.CreateView):

    model = Fetchers
    template_name = 'Item_create.html'
    form_class = CreateFetchersForm
    success_url = '/admin/'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)


class SurvachkiCreate(LoginRequiredMixin, generic.CreateView):

    model = Survachki
    template_name = 'Item_create.html'
    form_class = CreateSurvachkiForm
    success_url = '/admin/'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)

    ''' END CREATE FORMS'''

    '''PRODUCT LISTING'''

class MagicWandList(generic.ListView):
    model = MagicWand
    template_name = 'Item_list.html'
    context_object_name = 'item'


class SurvachkiList(generic.ListView):
    model = Survachki
    template_name = 'Item_list.html'
    context_object_name = 'item'


class FetchersList(generic.ListView):
    model = Fetchers
    template_name = 'Item_list.html'
    context_object_name = 'item'

    '''END PRODUCT LISTING'''

    '''EDIT VIEWS'''
class MagicWandEdit(LoginRequiredMixin, generic.UpdateView):
    model = MagicWand
    form_class = CreateMagicWandForm
    template_name = 'Item_modify.html'
    success_url = '/branch/magic_wand'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        instance = MagicWand.objects.get(pk=pk)
        form = CreateMagicWandForm(request.POST or None, instance=instance)
        return render(request, 'Item_modify.html', {'form': form})


class SurvachkiEdit(LoginRequiredMixin, generic.UpdateView):
    model = Survachki
    form_class = CreateSurvachkiForm
    template_name = 'Item_modify.html'
    success_url = '/branch/survachki'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        instance = Survachki.objects.get(pk=pk)
        form = CreateSurvachkiForm(request.POST or None, instance=instance)
        return render(request, 'Item_modify.html', {'form': form})


class FetchersEdit(LoginRequiredMixin, generic.UpdateView):
    model = Fetchers
    form_class = CreateFetchersForm
    template_name = 'Item_modify.html'
    success_url = '/branch/fetchers'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        instance = Fetchers.objects.get(pk=pk)
        form = CreateFetchersForm(request.POST or None, instance=instance)
        return render(request, 'Item_modify.html', {'form': form})

    '''END EDIT VIEWS'''

    '''DELETE EDIT VIEWS'''
class MagicWandDelete(LoginRequiredMixin, generic.DeleteView):
    model = MagicWand
    login_url = 'accounts/login/'
    context_object_name = 'item'

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        return render(request, 'Item_delete.html', {'item': self.get_object()})

    def post(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        item = self.get_object()
        item.delete()
        return HttpResponseRedirect('/branch/magic_wand')


class SurvachkiDelete(LoginRequiredMixin, generic.DeleteView):
    model = Survachki
    login_url = 'accounts/login/'
    context_object_name = 'item'

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        return render(request, 'Item_delete.html', {'item': self.get_object()})

    def post(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        item = self.get_object()
        item.delete()
        return HttpResponseRedirect('/branch/survachki')


class FetchersDelete(LoginRequiredMixin, generic.DeleteView):
    model = Fetchers
    login_url = 'accounts/login/'
    context_object_name = 'item'

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        return render(request, 'Item_delete.html', {'item': self.get_object()})

    def post(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        item = self.get_object()
        item.delete()
        return HttpResponseRedirect('/branch/fetchers')