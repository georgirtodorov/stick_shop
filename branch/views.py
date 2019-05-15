from django.shortcuts import render
from django.views import generic
from .models import MagicWand, Survachki, Fetchers, Stick
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import ProfileUser

# Create your views here.
'''PRODUCT LISTING'''

class MagicWandList(generic.ListView):
    model = MagicWand
    template_name = 'magicwand_list.html'
    context_object_name = 'magic_wand'


class SurvachkiList(generic.ListView):
    model = Survachki
    template_name = 'survachki_list.html'
    context_object_name = 'survachki'


class FetchersList(generic.ListView):
    model = Fetchers
    template_name = 'fetchers_list.html'
    context_object_name = 'fechers'

#LIST ALL ??? HOW

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
            furniture = Stick.objects.all().filter(user = user.pk)
            return furniture
        except:
            return []