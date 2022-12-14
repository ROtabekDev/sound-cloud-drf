from django.urls import path
from .endpoint import auth_views, views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('me/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),

    
    path('author/', views.AuthorView.as_view({'get': 'list'})),
    path('author/<int:pk>/', views.AuthorView.as_view({'get': 'retrieve'})),
    
    path('social/', views.SocialLinkView.as_view({'get': 'list', 'post': 'create'})),
    path('social/<int:pk>/', views.SocialLinkView.as_view({'put': 'update', 'delete':'destroy'})),
    
    path('google/', auth_views.google_auth),
    path('login/google/', auth_views.google_login)
]