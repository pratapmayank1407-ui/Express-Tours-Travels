from django.db import models
from django.urls import reverse


class Destination(models.Model):
    name = models.CharField(max_length=120)
    short_description = models.CharField(max_length=220)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name


class TourPackage(models.Model):
    CATEGORY_CHOICES = [
        ("family", "Family"),
        ("honeymoon", "Honeymoon"),
        ("adventure", "Adventure"),
        ("pilgrimage", "Pilgrimage"),
        ("custom", "Custom"),
    ]

    title = models.CharField(max_length=160)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="packages")
    short_description = models.CharField(max_length=280)
    description = models.TextField()
    duration = models.CharField(max_length=60, help_text="Example: 5 Days / 4 Nights")
    price_from = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="custom")
    image_url = models.URLField(blank=True)
    includes = models.TextField(blank=True, help_text="One item per line")
    excludes = models.TextField(blank=True, help_text="One item per line")
    is_featured = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_featured", "-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("package_detail", args=[self.pk])

    @property
    def include_list(self):
        return [x.strip() for x in self.includes.splitlines() if x.strip()]

    @property
    def exclude_list(self):
        return [x.strip() for x in self.excludes.splitlines() if x.strip()]


class BookingInquiry(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    customer_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=25)
    email = models.EmailField(blank=True)
    destination = models.CharField(max_length=120)
    package = models.ForeignKey(TourPackage, on_delete=models.SET_NULL, null=True, blank=True, related_name="inquiries")
    travel_date = models.DateField(null=True, blank=True)
    travelers = models.PositiveIntegerField(default=1)
    budget = models.CharField(max_length=80, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Booking enquiry"
        verbose_name_plural = "Booking enquiries"

    def __str__(self):
        return f"{self.customer_name} — {self.destination}"


class Review(models.Model):
    customer_name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(default=5)
    text = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} ({self.rating}/5)"


class GalleryImage(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="gallery/", blank=True, null=True)
    image_url = models.URLField(blank=True)
    alt_text = models.CharField(max_length=180, blank=True)
    is_published = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "-id"]

    def __str__(self):
        return self.title

    @property
    def display_url(self):
        if self.image:
            return self.image.url
        return self.image_url


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=25, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=180, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.subject or 'Contact'}"
