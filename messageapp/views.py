from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        account_id = self.kwargs['account_id']
        return Message.objects.filter(account_id=account_id)

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageSearchView(APIView):
    def get(self, request):
        query_params = request.query_params
        messages = Message.objects.all()
        
        if 'message_id' in query_params:
            message_ids = query_params.get('message_id').split(',')
            messages = messages.filter(message_id__in=message_ids)
        
        if 'sender_number' in query_params:
            sender_numbers = query_params.get('sender_number').split(',')
            messages = messages.filter(sender_number__in=sender_numbers)
        
        if 'receiver_number' in query_params:
            receiver_numbers = query_params.get('receiver_number').split(',')
            messages = messages.filter(receiver_number__in=receiver_numbers)
        
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

