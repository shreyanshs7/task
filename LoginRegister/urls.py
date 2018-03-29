from django.conf.urls import url
from .views import register,index
urlpatterns = [
    url(r'^$', index , name="index"),
    url(r'^register/', register , name="register"),
    

]