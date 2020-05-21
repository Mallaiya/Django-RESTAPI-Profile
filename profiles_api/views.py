from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class TestAPIView(APIView):
    serializer_data = serializers.TestSerializer

    def get(self, request, format=None):
        data = [
            {
                'name': 'Mallaiya',
                'age': 20,
            },
            {
                'name': 'Tamil',
                'age': 20,
            }
        ]
        return Response({'message': 'Successfully got data', 'data': data})


    def post(self, request):
        serializer = self.serializer_data(data=request.data)

        if(serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        serializer = self.serializer_data(data=request.data)

        if (serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'{name} updated'

            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk=None):
        serializer = self.serializer_data(data=request.data)

        if (serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'{name} patched successfully'

            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        return Response({'message':  'Deleted Successfully'})
