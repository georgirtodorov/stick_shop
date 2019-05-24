from django.urls import path, re_path, include
from django.contrib.auth.views import auth_logout
from . import views, models
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views


#urlpatterns = [
    #re_path('^profile/$', views.redirect_to_user_profile, name='redirect-user-detail'),
    #re_path('^profile/(?P<pk>\d+)/$', views.UserProfile.as_view(), name='user-detail'),
    #re_path('^profile/delete/$', models.ProfileUser.delete_user, name='user-delete'),

    #re_path('^', include('django.contrib.auth.urls')),
    #path('signup/', views.SignUp.as_view(), name='signup'),
    #path('logout/', views.logout_view, name='logout'),]

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),

    re_path('^profile/$', views.redirect_to_user_profile, name='redirect-user-detail'),
    re_path('^profile/(?P<pk>\d+)/$', views.UserProfile.as_view(), name='user-detail'),
    re_path('^profile/view/(?P<pk>\d+)/$', views.ViewUserProfile.as_view(), name='user_view-detail'),
    re_path('^profile/delete/(?P<pk>\d+)/$', views.ProfileDelete.as_view(), name='profile-delete'),

]

