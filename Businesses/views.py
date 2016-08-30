from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Business
from Images.models import RefImages
from .forms import BusinessForm


def homepage(request):	
	context = {

	}
	return render(request, "index1.html", {})

def search_result(request):
	business = request.GET.get('q')
	city = request.GET.get("city")
	search_list = Business.objects.filter(Bznss_Category__contains=business,Location__contains=city ).order_by()
	#.filter(ag = 'business', Location='city')[:10]
	context ={
		"business_list": search_list,
		"bznss": business,
		"cite": city,
	}
	return render(request, "result1.html", context)

def detail(request, id=None):
	instance = get_object_or_404(Business, id=id)
	pictures = RefImages.objects.filter(CompanyName_id=id)
	context = {
		"instance": instance,
		"images": pictures,
	}
	
	return render(request, "item.html", context)


def Create(request):
	form = BusinessForm()
	context = {
		"form": form,
	}

	return render(request, "create.html", context) 
