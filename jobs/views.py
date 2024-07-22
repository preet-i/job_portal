from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.views.generic import ListView
from .forms import ContactForm, JobListingForm, JobApplyForm
from .models import JobListing, ApplyJob

def home(request):
    qs = JobListing.objects.all()
    jobs = JobListing.objects.all().count()
    user = User.objects.all().count()
    company_name = JobListing.objects.filter(company_name__startswith='P').count()
    paginator = Paginator(qs, 5)  # Show 5 jobs per page
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,
        'job_qs': jobs,
        'company_name': company_name,
        'candidates': user
    }
    return render(request, "home.html", context)

def about_us(request):
    return render(request, "jobs/about_us.html", {})

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, "jobs/contact.html", context)

# @login_required
def job_listing(request):
    query = JobListing.objects.all().count()
    qs = JobListing.objects.all().order_by('-published_on')
    paginator = Paginator(qs, 3)  # Show 3 jobs per page
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,
        'job_qs': query
    }
    return render(request, "jobs/job_listing.html", context)

# @login_required
def job_post(request):
    form = JobListingForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('/jobs/job-listing/')
    context = {
        'form': form,

    }
    return render(request, "jobs/job_post.html", context)

def job_single(request, id):
    job_query = get_object_or_404(JobListing, id=id)
    context = {
        'q': job_query,
    }
    return render(request, "jobs/job_single.html", context)

# @login_required
def apply_job(request, job_id):
    job = get_object_or_404(JobListing, id=job_id)
    if timezone.now() > job.application_deadline:
        return HttpResponse("The application deadline for this job has passed.")
    if request.method == 'POST':
        form = JobApplyForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect('/')
    else:
        form = JobApplyForm()

    return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})

class SearchView(ListView):
    model = JobListing
    template_name = 'jobs/search.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.filter(
            title__contains=self.request.GET['title'],
            job_location__contains=self.request.GET['job_location'],
            employment_status__contains=(self.request.GET['employment_status']),
        )
