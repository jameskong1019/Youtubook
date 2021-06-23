from pages.views import hello_world
from django.urls.conf import path


app_name = "pages"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]
