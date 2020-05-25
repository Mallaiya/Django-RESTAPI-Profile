from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from profiles_api import serializers, models, permissions


class TestAPIView(APIView):
    
    serializer_class = serializers.TestSerializer

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
        
        serializer = self.serializer_class(data=request.data)
        
        if(serializer.is_valid()): 
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)

        if (serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'{name} updated'

            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)

        if (serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'{name} patched successfully'

            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        return Response({'message':  'Deleted Successfully'})


class TestViewSet(viewsets.ViewSet):
    serializer_class = serializers.TestSerializer

    def list(self, request):
        return Response({'message': 'Data fetched successfully form view sets', 'data': [1,2,3,4]})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
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

    def update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)

        if (serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'{name} updated'

            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)

        if (serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'{name} patched successfully'

            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        return Response({'message': 'Deleted Successfully'})



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

    # def list(self, request):
    #     return Response({'message': 'Data fetched successfully form view sets', 'data': })

    # print("---------------------", queryset)
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UserPermission, ) 
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'dob', 'email')


class LoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES