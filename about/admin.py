from django.contrib import admin
from .models import AboutUs, ThingsWeOffer
from django_summernote.admin import SummernoteModelAdmin


@admin.register(AboutUs)
class AboutUsAdmin(SummernoteModelAdmin):

    list_display = ('restaurant_name', 'description')
    summernote_fields = ('description')


@admin.register(ThingsWeOffer)
class ThingsWeOfferAdmin(SummernoteModelAdmin):

    list_display = ('title', 'description')
    summernote_fields = ('description')
