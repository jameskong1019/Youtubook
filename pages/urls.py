from pages.views import page, index, detail
from django.urls.conf import path


app_name = "pages"

urlpatterns = [
    path('', index, name='index'),
    path('page/', page, name='page'),
    path('detail/<str:video_id>', detail, name='detail') 
]
