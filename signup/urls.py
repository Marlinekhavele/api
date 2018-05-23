from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/$', views.LoginView.as_view()),
   url(r'^create/$', views.CreateView.as_view()),


]
