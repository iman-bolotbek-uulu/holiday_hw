import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from my_app import views
from my_project import settings

router = routers.DefaultRouter()
router.register('tweet', views.TweetViewSet, basename='home')
router.register('comment', views.CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth-drf/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('register/', views.RegisterUser.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns