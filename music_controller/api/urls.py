from django.urls import path
from .views import main # NOTE: Importing main(request) from `music_controller\api\views.py`

urlpatterns = [
    path('', main)
]