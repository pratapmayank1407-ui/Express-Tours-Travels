from django.contrib import admin
from .models import BookingInquiry, ContactMessage, Destination, GalleryImage, Review, TourPackage


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("name", "is_featured", "sort_order")
    list_filter = ("is_featured",)
    search_fields = ("name", "short_description")
    list_editable = ("is_featured", "sort_order")


@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ("title", "destination", "category", "duration", "price_from", "is_active", "is_featured")
    list_filter = ("category", "is_active", "is_featured", "destination")
    search_fields = ("title", "destination__name", "short_description")
    list_editable = ("is_active", "is_featured")
    prepopulated_fields = {}


@admin.register(BookingInquiry)
class BookingInquiryAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "phone", "destination", "package", "travel_date", "travelers", "status", "created_at")
    list_filter = ("status", "travel_date", "created_at")
    search_fields = ("customer_name", "phone", "email", "destination")
    list_editable = ("status",)
    readonly_fields = ("created_at",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "rating", "is_published", "created_at")
    list_filter = ("rating", "is_published")
    search_fields = ("customer_name", "text")
    list_editable = ("is_published",)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "sort_order")
    list_filter = ("is_published",)
    list_editable = ("is_published", "sort_order")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "subject", "created_at")
    search_fields = ("name", "email", "phone", "subject", "message")
    readonly_fields = ("created_at",)
