# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    email = models.CharField(max_length=255, null=True, blank=True)
    date_joined = models.DateTimeField(blank=True, null=True, default=timezone.now)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    phone_no = models.CharField(max_length=255, null=True, blank=True)
    team = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    prodvendor = models.ForeignKey(Prodvendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    value = models.IntegerField(null=True, blank=True)
    discount_value = models.IntegerField(null=True, blank=True)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Prodvendor(models.Model):

    #__Prodvendor_FIELDS__
    vendorcodename = models.CharField(max_length=255, null=True, blank=True)
    vendorcategory = models.CharField(max_length=255, null=True, blank=True)
    numvendorproducts = models.CharField(max_length=255, null=True, blank=True)
    vendornote = models.CharField(max_length=255, null=True, blank=True)

    #__Prodvendor_FIELDS__END

    class Meta:
        verbose_name        = _("Prodvendor")
        verbose_name_plural = _("Prodvendor")


class Category(models.Model):

    #__Category_FIELDS__
    categorynote = models.CharField(max_length=255, null=True, blank=True)

    #__Category_FIELDS__END

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Category")



#__MODELS__END
