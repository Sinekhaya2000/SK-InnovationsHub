from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic import ListView, DetailView
from .models import Job, Topic  # 👈 Make sure Topic model exists

# Existing ListView and DetailView classes
class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'

class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'

# Home view to display recent jobs
def home_view(request):
    recent_jobs = Job.objects.order_by('-id')[:3]
    topics = Topic.objects.all()[:5]  # Add some topics to the home page
    return render(request, 'jobs/home.html', {
        'recent_jobs': recent_jobs,
        'topics': topics,
    })

# Custom login view to handle login
def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

# Create Profile view
def create_profile_view(request):
    return render(request, 'users/create_profile.html')

# ✅ Topic detail view (NEW)
def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, 'jobs/topic_detail.html', {'topic': topic})
