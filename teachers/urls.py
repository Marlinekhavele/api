from django.conf.urls import url


from .views import(
   TeacherLoginAPIView,
   TeacherRegisterAPIView,
    UserRegisterAPIView,
    HeadTeacherRegisterAPIView,
    CountyOfficerRegisterAPIView
    
)
urlpatterns = [
 url(r'^login/$', TeacherLoginAPIView.as_view(),name='login'),
 url(r'^register/$', TeacherRegisterAPIView.as_view(),name='register'),
 url(r'^details/$', HeadTeacherRegisterAPIView.as_view(),name='details'),
 url(r'^create/$', CountyOfficerRegisterAPIView.as_view(),name='create')
]    
