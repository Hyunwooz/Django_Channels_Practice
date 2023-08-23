from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request):
        return render(request, 'chat/index.html')


class Room(View):
    def get(self, request, roomName):
        
        return render(request, 'chat/room.html')