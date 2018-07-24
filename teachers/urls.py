from django.conf.urls import url


from .views import(
    DashboardLoginView,
    TeacherRegisterAPIView,
    UserRegisterAPIView,
    HeadTeacherRegisterAPIView,
    CountyOfficerRegisterAPIView,
    APIRootView
    # MarlineRegisterAPIView
    
)
urlpatterns = [
 url(r'^user/$', UserRegisterAPIView.as_view(),name='user'),
 url(r'^login/$', DashboardLoginView.as_view(),name='login'),
 url(r'^register/$', TeacherRegisterAPIView.as_view(),name='register'),
 url(r'^detail/$', HeadTeacherRegisterAPIView.as_view(),name='detail'),
 url(r'^create/$', CountyOfficerRegisterAPIView.as_view(),name='create'),
 url(r'^apiroot/$', APIRootView.as_view(),name='apiroot'),
#  url(r'^teacher-register/$', MarlineRegisterAPIView.as_view(),name='teacher_register'),
]    
