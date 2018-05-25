from django.db import models
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from .utils import unique_slug_generator
from .validators import validate_category

User = settings.AUTH_USER_MODEL

# Create your models here.
class RestaurantLocation(models.Model):
	owner 			= models.ForeignKey(User)
	name 			= models.CharField(max_length=120)
	location 		= models.CharField(max_length=120, null = True, blank=True)
	category		= models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
	timestamp		= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)
	slug 			= models.SlugField(blank = True, null = True)
	# my_date_field 	= models.DateField(auto_now_add=False, auto_now=False)

	def __str__(self):
		return self.name

	@property
	def title(self):
		return self.name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.category = instance.category.capitalize()
	print ('saving...')
	print (instance.timestamp)
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


# def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
# 	print ('saved...')
# 	print (instance.timestamp)

pre_save.connect(rl_pre_save_receiver, sender = RestaurantLocation)
# post_save.connect(rl_post_save_receiver, sender = RestaurantLocation)

# from django.conf import settings
# User = settings.AUTH_USER_MODEL
# steve_user = User.objects.get(id=1)
# steve_user.restaurantlocation_set.all() --> Lists all RestaurantLocation (FK) associated with the user
# ---- OTHER WAY OF DOING IT 
# from restaurants.models import RestaurantLocation 
# RestaurantLocations.objects.filter(owner__username__iexact='steve')
# ------
# from restaurants.models import RestaurantLocation 
# obj = RestaurantLocations.objects.all().first()
# obj.owner -> Returns User type