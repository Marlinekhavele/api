from django.conf.urls import url
from .views import(
    LoginView,
    CreateView,
    APIRootView
)
urlpatterns = [
    url(r'^login/$', LoginView.as_view(),name='login'),
   url(r'^create/$', CreateView.as_view(),name='register'),
   url(r'^apiroot/$', APIRootView.as_view(),name='root'),


]
