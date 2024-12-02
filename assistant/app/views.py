from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Comment, Screenshot
from .serializers import CommentSerializer, ScreenshotSerializer

# Define a simple home view
def home(request):
    return render(request, 'home.html')  # Ensure 'home.html' exists in your templates folder

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})
class UploadCommentView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UploadScreenshotView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        print("Incoming Data:", request.data)  # Log request data
        print("Files:", request.FILES)  # Log uploaded files

        serializer = ScreenshotSerializer(data=request.data)  # No `files` argument
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Errors:", serializer.errors)  # Log validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.serializers import CommentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Comment
from app.serializers import CommentSerializer
class CommentListView(APIView):
    def get(self, request):
        # Fetch all comments
        comments = Comment.objects.all()
        # Serialize the data
        serializer = CommentSerializer(comments, many=True)
        print("Available classes in views.py:", dir())

        return Response(serializer.data)

class ScreenshotListView(APIView):
    def get(self, request):
        screenshots = Screenshot.objects.all()
        serializer = ScreenshotSerializer(screenshots, many=True)
        return Response(serializer.data)
