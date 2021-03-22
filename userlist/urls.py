from django.urls import path
from .views import index, ActivityDetailView, MemberActivityCreateView

urlpatterns = [
    path('', index, name='home'),
    path('activity/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    path('activity/join/', MemberActivityCreateView.as_view(), name='activity-join')
]
