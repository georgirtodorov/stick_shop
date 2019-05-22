from django.urls import path, re_path

from . import views

urlpatterns = [
    path('magic_wand/', views.MagicWandList.as_view(), name='magic_wand'),
    path('survachki/', views.SurvachkiList.as_view(), name='survachki'),
    path('fetchers/', views.FetchersList.as_view(), name='fetchers'),
    path('', views.UserStickList.as_view(), name='user-sticks'),
    re_path('^create/$', views.stick_create_options, name='stick_create_options'),
    re_path('^create/magic_wand_create/$', views.MagicWandCreate.as_view(), name='magic_wand_create'),
    re_path('^create/fetchers_create/$', views.FetchersCreate.as_view(), name='fetchers_create'),
    re_path('^create/survachki_create/$', views.SurvachkiCreate.as_view(), name='survachki_create'),
    re_path('^magic_wand/edit/(?P<pk>\d+)/$', views.MagicWandEdit.as_view(), name='magic_wand-edit'),
    re_path('^survachki/edit/(?P<pk>\d+)/$', views.SurvachkiEdit.as_view(), name='survachki-edit'),
    re_path('^fetchers/edit/(?P<pk>\d+)/$', views.FetchersEdit.as_view(), name='fetchers-edit'),
    re_path('^magic_wand/delete/(?P<pk>\d+)/$', views.MagicWandDelete.as_view(), name='magic_wand-delete'),
    re_path('^survachki/delete/(?P<pk>\d+)/$', views.SurvachkiDelete.as_view(), name='survachki-delete'),
    re_path('^fetchers/delete/(?P<pk>\d+)/$', views.FetchersDelete.as_view(), name='fetchers-delete'),
    #re_path('^details/(?P<pk>\d+)/$', views.FurnitureDetail.as_view(), name='furniture-detail'),

]
