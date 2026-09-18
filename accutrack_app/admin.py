from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse
from .models import CarouselSlide, FooterContent, GalleryImage, ContactInfo


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'phone_number', 'landline_number', 'city_country')
    fieldsets = (
        ('Company & Building Information', {
            'description': 'These details appear in the Address column of the footer and on the Contact Us page.',
            'fields': ('company_name', 'office_address', 'street_address', 'city_country', 'po_box')
        }),
        ('Communication Channels', {
            'description': 'Phone, Landline, and Email displayed across the website header, contact card, and footer.',
            'fields': ('email', 'phone_number', 'landline_number')
        }),
        ('WhatsApp & Quick Connect', {
            'description': 'WhatsApp number used for floating chat buttons and the contact form message submission.',
            'fields': ('whatsapp_number',)
        }),
        ('Google Maps Location', {
            'description': 'Paste the "src" URL from Google Maps Embed iframe to update the interactive map on the Contact page.',
            'fields': ('google_maps_embed_url',)
        }),
    )

    def changelist_view(self, request, extra_context=None):
        # Automatically redirect to edit form of the singleton record
        obj, _ = ContactInfo.objects.get_or_create(id=1)
        return redirect(reverse('admin:accutrack_app_contactinfo_change', args=[obj.id]))

    def has_add_permission(self, request):
        return not ContactInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(CarouselSlide)
admin.site.register(GalleryImage)

