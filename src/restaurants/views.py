from django.db.models import Q
from django .http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
import random


def restaurant_createview(request):
	form = RestaurantLocationCreateForm(request.POST or None)
	errors = None
	if form.is_valid():
		form.save()
		# obj = RestaurantLocation.objects.create(
		# 		name = form.cleaned_data.get('name'),
		# 		location = form.cleaned_data.get('location'),
		# 		category = form.cleaned_data.get('category')
		# 	) 
		return HttpResponseRedirect("/restaurants")
	if form.errors:
		errors = form.errors
	template_name = 'restaurants/form.html'
	context = { "form" : form, "errors":errors	}
	return render(request, template_name, context)

def restaurant_listview(request):
	template_name = 'restaurants/restaurant-list.html'
	queryset = RestaurantLocation.objects.all()
	context = {
		"object_list": queryset
		}
	return render(request, template_name, context)


class RestaurantListView(ListView):
	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(
				Q(category__iexact=slug) |
				Q(category__icontains=slug)
			)
		else:
			queryset = RestaurantLocation.objects.all()
		return queryset

class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all()
	

class RestaurantCreateView(CreateView):
	form_class = RestaurantLocationCreateForm
	template_name = 'restaurants/form.html'
	success_url = '/restaurants/'

	# def get_context_data(self, *args, **kwargs):
	# 	print(self.kwargs)
	# 	context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs) 
	# 	print(context)
	# 	return context

	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	# 	obj = get_object_or_404(RestaurantLocation, id=rest_id)
	# 	return obj

# class SearchRestaurantListView(ListView):
# 	template_name = 'restaurants/restaurant-list.html'
# 	def get_queryset(self):
# 		print(self.kwargs)
# 		slug = self.kwargs.get("slug")
# 		if slug:
# 			queryset = RestaurantLocation.objects.filter(
# 				Q(category__iexact=slug) |
# 				Q(category__icontains=slug)
# 			)
# 		else:
# 			queryset = RestaurantLocation.objects.none()
# 		return queryset



# class AsianFusionRestaurantListView(ListView):
# 	queryset = RestaurantLocation.objects.filter(category__iexact='asian fusion')
# 	template_name = 'restaurants/restaurant-list.html'

# def home(request):
# 	num = random.randint(0,100)
# 	some_list = [num, random.randint(0,100), random.randint(0,100), random.randint(0,100)]
# 	context ={ "html_var":"test", 
# 	"num":num,
# 	"bool_item":True,
# 	"some_list":some_list
# 	}
# 	return render(request, "home.html", context) #response 

# def about(request):
# 	context ={}
# 	return render(request, "about.html", context) #response 

# def contact(request):
# 	context ={}
# 	return render(request, "contact.html", context) #response 
# 
# 
# 
# class ContactView(View):
# 	def get(self, request, *args, **kwargs):
# 		context= {}
# 		return render(request, "contact.html", context)

# 		# def post(self, request, *args, **kwargs):
# 		# context= {}
# 		# print(kwargs)
# 		# return render(request, "contact.html", context)

# 		# def put(self, request, *args, **kwargs):
# 		# context= {}
# 		# print(kwargs)
# 		# return render(request, "contact.html", context)


# class HomeView(TemplateView):
# 	template_name = 'home.html'
# 
# 	def get_context_data(self, *args, **kwargs):
# 		context = super(HomeView, self).get_context_data(*args, **kwargs)
# 		print(context)
# 		num = random.randint(0,100)
# 		some_list = [num, random.randint(0,100), random.randint(0,100), random.randint(0,100)]
# 		context ={ "html_var":"test", 
# 		"num":num,
# 		"bool_item":True,
# 		"some_list":some_list
# 		}
# 		return context
# 
# class ContactView(TemplateView):
# 	template_name = 'contact.html'
# 
# class AboutView(TemplateView):
# 	template_name = 'about.html'
