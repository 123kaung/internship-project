from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Bid
from .forms import BidForm
from projects.models import Project  # Import from the projects app

def bid_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.project = project
            bid.freelancer = request.user
            bid.save()
            return redirect('home')  # Adjust to your homepage view name
    else:
        form = BidForm()
    return render(request, 'bids/bid_project.html', {'form': form, 'project': project})