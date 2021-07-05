from pages.views import page, index
from django.urls.conf import path


app_name = "pages"

urlpatterns = [
    path('', index, name='index'),
    path('page/', page, name='page'),
]
