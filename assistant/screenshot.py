import os
import django

# Set up Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assistant.settings')  # Replace 'assistant' with your project name
django.setup()

# Now import your models
from app.models import Screenshot
from django.core.files.uploadedfile import SimpleUploadedFile

# Simulate an uploaded file
file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")

# Create a Screenshot object
screenshot = Screenshot.objects.create(image=file)
print(f"Screenshot saved with ID: {screenshot.id}, URL: {screenshot.image.url}")
