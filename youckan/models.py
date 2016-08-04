# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser as AbstractBaseUser


class Oauth2ProviderGrant(models.Model):
    user = models.ForeignKey('YouckanUser', models.DO_NOTHING)
    code = models.CharField(max_length=255)
    application = models.ForeignKey('SsoOauth2Application', models.DO_NOTHING)
    expires = models.DateTimeField()
    redirect_uri = models.CharField(max_length=255)
    scope = models.TextField()

    class Meta:
        managed = False
        db_table = 'oauth2_provider_grant'


class Oauth2ProviderAccesstoken(models.Model):
    """
      id  | user_id |             token              | application_id |            expires            |  scope
    ------+---------+--------------------------------+----------------+-------------------------------+---------
    28169 |    1234 | dcBSKkM9Ha4MjsySUcqMsB9UiFXWSQ |              3 | 2016-08-04 08:27:37.696068+02 | profile
    28168 |     678 | JUT5N8cNov7oT65ylx657NeBCP4Aly |              3 | 2016-08-04 08:07:16.212989+02 | profile
    """
    user = models.ForeignKey('YouckanUser', models.DO_NOTHING)
    token = models.CharField(max_length=255)
    application = models.ForeignKey('SsoOauth2Application', models.DO_NOTHING)
    expires = models.DateTimeField()
    scope = models.TextField()

    class Meta:
        managed = False
        db_table = 'oauth2_provider_accesstoken'


class Oauth2ProviderRefreshtoken(models.Model):
    user = models.ForeignKey('YouckanUser', models.DO_NOTHING)
    token = models.CharField(max_length=255)
    application = models.ForeignKey('SsoOauth2Application', models.DO_NOTHING)
    access_token = models.ForeignKey(Oauth2ProviderAccesstoken,
                                     models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_refreshtoken'


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=75)
    code = models.CharField(max_length=32)
    verified = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SsoOauth2Application(models.Model):
    client_id = models.CharField(unique=True, max_length=100)
    user = models.ForeignKey('YouckanUser', models.DO_NOTHING)
    redirect_uris = models.TextField()
    client_type = models.CharField(max_length=32)
    authorization_grant_type = models.CharField(max_length=32)
    client_secret = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    is_internal = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'sso_oauth2application'


class YouckanUser(AbstractBaseUser):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    email = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=150)

    class Meta:
        db_table = 'youckan_user'


class YouckanUserprofile(models.Model):
    user = models.ForeignKey(YouckanUser, models.DO_NOTHING, unique=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'youckan_userprofile'
