from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:pk>/', views.details, name='details'),
    path('contact', views.contact, name='contact'),
    path('categories', views.categories, name='about'),
    path('videos', views.videos, name='videos'),
    path('about', views.about, name='about'),
    path('add_post', views.add_post, name='add_post'),
    path('add_category', views.add_category, name='add_category'),
    path('manage', views.manage, name='manage'),
    path('ads_form', views.ads_form, name='ads_form'),
    path('base', views.bases, name='base'),
    path('update/<int:pk>/', views.update_post, name='update_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('each_category/<int:pk>/', views.each_category, name='each_category'),
    path('add_video/', views.add_video, name='add_video'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),




]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
