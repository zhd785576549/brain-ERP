from django.conf.urls import url
from views import LoginView


urlpatterns = [
    url(r'login/$', LoginView.as_view(), name='member_login'),
]