from pages.views import page, index, detail
from django.urls import include
from django.urls.conf import path
from rest_framework import routers
from pages import views

app_name = "pages"

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('page/', page, name='page'),
    path('detail/<str:video_id>', detail, name='detail'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
