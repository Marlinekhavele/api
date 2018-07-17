from django.conf.urls import url
# from .views import(    
#     CreateView,
    
# )

from .views import(
    CreateView,
    # StudentRegisterAPIView
    UserRegisterAPIView,
   StudentSignup,
    StudentLogin
)
urlpatterns = [
    url(r'^student-signup/$', StudentSignup,name='StudentSignup'),
    url(r'^StudentLogin/$', StudentLogin,name='StudentLogin'),
    url(r'^create/$', CreateView.as_view(),name='signup'),
    url(r'^user-create/$', UserRegisterAPIView.as_view(),name='sigup'),
    
   
   
#    url(r'^register/$', StudentRegisterAPIView.as_view(),name='signup'),
   

]
