from django.conf.urls import url
from .views import verifyOtp

urlpatterns = [
    url(r'^verify', verifyOtp , name="verify"),
]