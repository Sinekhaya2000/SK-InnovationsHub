from django.urls import path
from django.contrib.auth import views as auth_views
from .views import JobListView, JobDetailView, home_view, custom_login_view, create_profile_view, topic_detail

urlpatterns = [
    path('', home_view, name='home'),
    path('jobs/', JobListView.as_view(), name='jobs'),
    path('<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('login/', custom_login_view, name='login'),
    path('create-profile/', create_profile_view, name='create_profile'),
    path('topics/<int:pk>/', topic_detail, name='topic_detail'),  # ✅ NEW
]
