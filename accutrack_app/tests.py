import tempfile
from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from accutrack_app.models import ContactInfo, CarouselSlide, GalleryImage, FooterContent
from accutrack_app.context_processors import contact_info as contact_info_processor
from django.core.files.uploadedfile import SimpleUploadedFile


MEDIA_ROOT = tempfile.mkdtemp()

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class AccuTrackViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.contact = ContactInfo.objects.create(
            company_name="Accutrack Technologies LLC",
            office_address="Office No-13, F-14 First Floor",
            street_address="Al Nahda Street, Al Twar-1",
            city_country="Dubai - UAE",
            po_box="233642",
            email="support@accutrack.ae",
            phone_number="+971 54 333 7493",
            landline_number="+971 4 296 9899",
            whatsapp_number="971543337493"
        )
        # Create a test slide in temp MEDIA_ROOT
        image_content = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01\x44\x00\x3b'
        test_img = SimpleUploadedFile("test_slide.gif", image_content, content_type="image/gif")
        self.slide = CarouselSlide.objects.create(
            image=test_img,
            heading="Test Heading Innovation",
            description="Test Description for Slide"
        )
        # Create a test gallery image
        test_gallery_img = SimpleUploadedFile("test_gallery.gif", image_content, content_type="image/gif")
        self.gallery = GalleryImage.objects.create(
            image=test_gallery_img,
            caption="Test Structured Cabling"
        )

    def test_home_page_status_and_content(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Test Heading Innovation')
        self.assertContains(response, 'Accutrack Technologies LLC')

    def test_about_page_status(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertContains(response, 'ABOUT US')

    def test_services_page_status(self):
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services.html')
        self.assertContains(response, 'OUR SERVICES WE OFFER')

    def test_gallery_page_status_and_content(self):
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')
        self.assertContains(response, 'Test Structured Cabling')

    def test_contact_page_status_and_form(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertContains(response, 'whatsappContactForm')
        self.assertContains(response, 'support@accutrack.ae')

    def test_admin_login_status(self):
        response = self.client.get('/admin/login/')
        self.assertEqual(response.status_code, 200)

    def test_static_redirects(self):
        for route in ['/favicon.ico', '/apple-touch-icon.png', '/site.webmanifest']:
            res = self.client.get(route)
            self.assertEqual(res.status_code, 301)


class ContactInfoModelTests(TestCase):
    def test_contact_info_properties(self):
        info = ContactInfo.objects.create(
            phone_number="+971 54 333 7493",
            landline_number="+971 (4) 296-9899",
            whatsapp_number="+971-54-333-7493"
        )
        self.assertEqual(info.clean_phone, "+971543337493")
        self.assertEqual(info.clean_landline, "+97142969899")
        self.assertEqual(info.clean_whatsapp, "971543337493")
        self.assertIn("Contact Details", str(info))

    def test_context_processor_auto_creation(self):
        # Ensure that if ContactInfo table is empty, context processor creates record #1
        ContactInfo.objects.all().delete()
        context = contact_info_processor(None)
        self.assertIn('contact_info', context)
        self.assertIsNotNone(context['contact_info'])
        self.assertEqual(ContactInfo.objects.count(), 1)


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class SlideAndGalleryModelTests(TestCase):
    def test_string_representations(self):
        image_content = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01\x44\x00\x3b'
        slide = CarouselSlide(
            image=SimpleUploadedFile("s.gif", image_content, content_type="image/gif"),
            heading="Modern Solutions"
        )
        self.assertEqual(str(slide), "Modern Solutions")

        gallery = GalleryImage(
            image=SimpleUploadedFile("g.gif", image_content, content_type="image/gif"),
            caption="High Tech Security"
        )
        self.assertEqual(str(gallery), "High Tech Security")
