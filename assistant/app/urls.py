from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import UploadCommentView, UploadScreenshotView
from app.views import CommentListView

urlpatterns = [
    # General Views
    path('', views.home, name='dashboard'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    # Password Management
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    # API Endpoints
    path('upload/comment/', UploadCommentView.as_view(), name='upload_comment'),
    path('upload/screenshot/', UploadScreenshotView.as_view(), name='upload_screenshot'),
    
    path('comments/', CommentListView.as_view(), name='comment_list'),

]
