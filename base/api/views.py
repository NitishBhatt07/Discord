# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    return Response(routes)
    # return JsonResponse(routes, safe=False)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    # objects can not be converted to json so we use serializer
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request,pk):
    room = Room.objects.get(id=pk)
    # objects can not be converted to json so we use serializer
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)