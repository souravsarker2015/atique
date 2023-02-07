from django.contrib import messages
from rest_framework import response, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from myapp.api.serializers import ChildSerializer
from myapp.models import Child


@api_view(['GET', 'PUT', 'DELETE'])
def child(request, pk):
    if request.method == "GET":
        child = Child.objects.get(id=pk)
        on_boarded = child.is_onboarded
        if on_boarded is True:
            serializer = ChildSerializer(child)
            return Response(serializer.data)
        else:
            content = {"error": "data  not found"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    # if request.method == "PUT":
    #     stream = Stream.objects.get(pk=pk)
    #     serializer = StreamSerializer(stream, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #
    # if request.method == "DELETE":
    #     Stream.objects.get(id=pk).delete()
    #     return Response(status=status.HTTP_200_OK)
