from django.db import models

class CarouselSlide(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    heading = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading

class FooterContent(models.Model):
    address = models.TextField()
    email = models.EmailField(default="")
    phone_number = models.CharField(max_length=20, default="")

    def __str__(self):
        return "Footer Content"
    
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption


class ContactInfo(models.Model):
    company_name = models.CharField(
        max_length=255,
        default="Startup Guru Business Center",
        help_text="Company / Center Name (e.g. Startup Guru Business Center)"
    )
    office_address = models.CharField(
        max_length=255,
        default="Office No-13, F-14 First Floor",
        help_text="Office / Floor / Suite (e.g. Office No-13, F-14 First Floor)"
    )
    street_address = models.CharField(
        max_length=255,
        default="Al Nahda Street, Al Twar-1",
        help_text="Street / Area (e.g. Al Nahda Street, Al Twar-1)"
    )
    city_country = models.CharField(
        max_length=255,
        default="Dubai - UAE",
        help_text="City & Country (e.g. Dubai - UAE)"
    )
    po_box = models.CharField(
        max_length=50,
        default="233642",
        help_text="P.O. Box Number"
    )
    email = models.EmailField(
        default="support@accutrack.ae",
        help_text="Primary support/contact email address"
    )
    phone_number = models.CharField(
        max_length=50,
        default="+971 54 333 7493",
        help_text="Mobile / Primary Phone (displayed on header, contact card, and footer)"
    )
    landline_number = models.CharField(
        max_length=50,
        default="+971 4 296 9899",
        help_text="Landline Number (displayed on footer and contact details)"
    )
    whatsapp_number = models.CharField(
        max_length=50,
        default="971543337493",
        help_text="WhatsApp Number with country code and digits only (e.g. 971543337493)"
    )
    google_maps_embed_url = models.TextField(
        default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3607.6450180505485!2d55.35089467472997!3d25.282524228240568!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3e5f5c8b80b14ea3%3A0xb88d7b254998748d!2sRoyal%20House%20Building!5e0!3m2!1sen!2sin!4v1733827038163!5m2!1sen!2sin",
        help_text="Google Maps Embed URL (the 'src' attribute inside Google Maps iframe)"
    )

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return f"{self.company_name} Contact Details"

    @property
    def clean_phone(self):
        return ''.join(c for c in self.phone_number if c.isdigit() or c == '+')

    @property
    def clean_landline(self):
        return ''.join(c for c in self.landline_number if c.isdigit() or c == '+')

    @property
    def clean_whatsapp(self):
        return ''.join(c for c in self.whatsapp_number if c.isdigit())