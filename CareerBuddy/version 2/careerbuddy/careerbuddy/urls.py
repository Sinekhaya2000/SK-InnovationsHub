from django.contrib import admin
from django.urls import path, include
from jobs.views import home_view  # ✅ Import home_view from jobs app

urlpatterns = [
    path('', home_view, name='home'),        # ✅ Root URL path
    path('jobs/', include('jobs.urls')),     # Jobs app
    path('admin/', admin.site.urls),         # Admin panel
]
