from django.urls import path

from . import views

urlpatterns = [
    # ... your existing URLs
    path('chat/', views.chat_interface, name='chat_interface'),
    path('api/chat/', views.chat_with_assistant, name='chat_with_assistant'),
]
