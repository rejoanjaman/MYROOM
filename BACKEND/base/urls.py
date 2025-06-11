from django.urls import path
from.import views


urlpatterns = [
    path('',views.home,name='home'),
    #path('room/<str:ph>/',views.room,name='room'),
    path('login/',views.login, name="login"),
    path('create-profile/', views.create_user_profile, name='create_profile')
]



