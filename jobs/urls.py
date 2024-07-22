from django.urls import path
from .views import *

app_name = 'jobs'

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('about/', about_us, name='about'),
    path('job-post/', job_post, name='job-post'),
    path('job-listing/', job_listing, name='job-listing'),
    path('job-single/<int:id>/', job_single, name='job-single'),
    path('search/', SearchView.as_view(), name='search'),
    path('apply/<int:job_id>/', apply_job, name='apply'),
]
