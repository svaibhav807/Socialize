from django.urls import path
from . import views


app_name = 'core'

urlpatterns=[
    path('', views.RegistrationView, name='register' ),
    path('login/', views.LoginView, name='login'),
    path('login/success/', views.successLogin, name='login-success'),
    path('profile/<str:user_name>/', views.displayUserProfile, name='user_profile_page'),
    path('profile/<str:user_name>/edit/',views.editProfile,name = "edit_profile"),
    path('profile/<str:user_name>/logout', views.userLogout , name="logout"),
    path('profile/<str:user_name>/follow/', views.userFollow, name="user_Follow"),
    path('profile/<str:user_name>/create_post',views.create_post,name="create_post"),
    path('profile/<str:user_name>/unfollow/', views.userUnfollow, name="user_Unfollow"),
    path('profile/<str:user_name>/<int:post_id>/create_comment',views.createComment , name = "create_comment"),
    path('profile/<str:user_name>/feed',views.displayFeed, name = "user_feed"),
    path('profile/<str:user_name>/<int:post_id>/like',views.postLike, name="post_like"),
    path('profile/<str:user_name>/followers',views.show_followers,name="see_followers")
]