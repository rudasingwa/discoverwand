from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse

# Create your models here.

class Business(models.Model):
	CompanyName = models.CharField(max_length=120, null=True)
	Companylogo = models.FileField()
	LogoPreview = models.FileField(default=True)
	Address = models.CharField(max_length=120, null=True)
	Location = models.CharField(max_length=120, null=True)
	PhoneNumber = models.IntegerField()	
	Website = models.URLField(max_length=200)
	Facebook = models.URLField(max_length=200)
	Twitter = models.URLField(max_length=200)
	Instagram = models.URLField(max_length=200)
	BusinessDescription = HTMLField()
	Bznss_Category = models.CharField(max_length=120, null=True)
	Updated = models.DateTimeField(auto_now=False,auto_now_add=True)
	Created = models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return self.CompanyName


	def get_absolute_url(self):		
		return reverse("detail", kwargs={"id": self.id})