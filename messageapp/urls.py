from django.urls import path
from .views import MessageListView, MessageCreateView, MessageSearchView

urlpatterns = [
    path('messages/<str:account_id>/', MessageListView.as_view(), name='get_messages'),
    path('create/', MessageCreateView.as_view(), name='create_message'),
    path('search/', MessageSearchView.as_view(), name='search_messages'),
]

