
from django.urls import path ,include
from . import views
urlpatterns = [

     path('',views.homepage,name='homepage'),
     path('vrform/',views.vrform,name='vrform'),
      path('addpost/',views.addpost,name='addpost'),
]
