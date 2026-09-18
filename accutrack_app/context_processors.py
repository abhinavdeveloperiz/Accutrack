from .models import ContactInfo

def contact_info(request):
    info = ContactInfo.objects.first()
    if not info:
        info, _ = ContactInfo.objects.get_or_create(id=1)
    return {
        'contact_info': info
    }
