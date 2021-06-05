from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


def HomeView(request):
    return render(request, 'login.html')

@permission_classes((AllowAny,))
class LoginView(APIView):
    # @csrf_exempt
    # @api_view(('POST',))
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username == 'Anwar' and password == 'Admin123':
            return Response({"status": "pass"},status= status.HTTP_200_OK)
        else:
            return Response({"status": "fail"}, status=status.HTTP_401_UNAUTHORIZED)



def TableView(request):
    return render(request, 'Tablesheet.html')