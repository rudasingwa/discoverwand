from __future__ import unicode_literals

from django.db import models

# Create your models here.

class RefImages(models.Model):
	word = models.CharField(max_length=30, null=True, blank=True)
   	Image = models.ImageField(default=True)
   	CompanyName = models.ForeignKey('Businesses.Business', on_delete=models.CASCADE, null=True)

   	def __unicode__(self):
		return self.word