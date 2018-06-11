from django.conf.urls import url
# from .views import(    
#     CreateView,
    
# )

from .views import(
    CreateView,
    # StudentRegisterAPIView
    UserRegisterAPIView,
    login_view
)
urlpatterns = [
   url(r'^create/$', CreateView.as_view(),name='signup'),
   url(r'^user-create/$', UserRegisterAPIView.as_view(),name='sigup'),
   url(r'^student_form/$', login_view,name='student_form'),
   
#    url(r'^register/$', StudentRegisterAPIView.as_view(),name='signup'),
   

]
