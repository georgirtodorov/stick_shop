from django.urls import re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^user_login/$', views.user_login, name='user_login'),
    re_path('^profile/$', views.redirect_to_user_profile, name='redirect-user-detail'),
    re_path('^profile/(?P<pk>\d+)/$', views.UserProfile.as_view(), name='user-detail'),
    re_path('^profile/view/(?P<pk>\d+)/$', views.ViewUserProfile.as_view(), name='user_view-detail'),
    re_path('^profile/delete/(?P<pk>\d+)/$', views.delete_user, name='profile-delete'),
]

