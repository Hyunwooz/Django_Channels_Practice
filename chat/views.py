from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request):
        return render(request, 'chat/index.html')


class Room(View):
    def get(self, request,room_name):
        print(room_name)
        return render(request, 'chat/room.html')