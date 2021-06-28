from pages.views import page
from django.urls.conf import path


app_name = "pages"

urlpatterns = [
    path('page/', page, name='page')
]
