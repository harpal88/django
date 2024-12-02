from django.db import models

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]  # Show a snippet of the comment

class Screenshot(models.Model):
    image = models.ImageField(upload_to='screenshots/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Screenshot {self.id} uploaded at {self.uploaded_at}"
