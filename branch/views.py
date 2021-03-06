from django.shortcuts import render
from django.views import generic
from .models import MagicWand, Survachki, Fetchers, Stick
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import ProfileUser, User
from django.http import HttpResponseRedirect

from .forms import CreateMagicWandForm, CreateFetchersForm, CreateSurvachkiForm


# Create your views here.
def has_access_to_modify(current_user, item):
    if current_user.is_superuser:
        return True
    elif current_user.id == item.username.id:
        return True
    return False



    '''CREATE FORMS'''

def stick_create_options(request):
    return render(request, 'stick_create_options.html')


class MagicWandCreate(LoginRequiredMixin, generic.CreateView):

    model = MagicWand
    template_name = 'Item_create.html'
    form_class = CreateMagicWandForm
    success_url = '/branch/magic_wand/'

    def form_valid(self, form):
        print(self.request.user.id)
        print(User.objects.all().filter(username=self.request.user.username)[0])
        user = User.objects.get(username=self.request.user.username)
        print(user)
        #username = User.objects.all().filter(username=self.request.user.username)[0])
        #print(username)
        form.instance.username = user
        return super().form_valid(form)


class FetchersCreate(LoginRequiredMixin, generic.CreateView):

    model = Fetchers
    template_name = 'Item_create.html'
    form_class = CreateFetchersForm
    success_url = '/branch/fetchers'

    def form_valid(self, form):
        user = User.objects.get(username=self.request.user.username)
        print(user)
        form.instance.username = user
        return super().form_valid(form)


class SurvachkiCreate(LoginRequiredMixin, generic.CreateView):

    model = Survachki
    template_name = 'Item_create.html'
    form_class = CreateSurvachkiForm
    success_url = '/branch/survachki'

    def form_valid(self, form):
        user = User.objects.get(username=self.request.user.username)
        print(user)
        form.instance.username = user
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