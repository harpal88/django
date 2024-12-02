from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import ScreenshotListView


urlpatterns = [
    path('admin/', admin.site.urls),  # Enables the Django admin interface
    path('', include('app.urls')),   # Includes app-level URLs
    path('screenshots/', ScreenshotListView.as_view(), name='screenshot_list'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
