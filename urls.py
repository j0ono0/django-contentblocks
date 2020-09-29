from django.urls import path
from contentblocks.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]