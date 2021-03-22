from django.urls import path
from .views import profile, CreateAct


urlpatterns = [
    path('', profile, name='profile'),
    path('new/', CreateAct.as_view(), name='new-activity'),
]
