from django.urls import path, re_path

from . import views

urlpatterns = [
    path('magic_wand', views.MagicWandList.as_view(), name='magic_wand'),
    path('survachki', views.SurvachkiList.as_view(), name='survachki'),
    path('fetchers', views.FetchersList.as_view(), name='fetchers'),
    path('mine/', views.UserStickList.as_view(), name='user-sticks'),
]
