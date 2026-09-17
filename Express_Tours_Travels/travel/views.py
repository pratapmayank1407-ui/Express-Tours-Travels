from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookingInquiryForm, ContactMessageForm
from .models import ContactMessage, Destination, GalleryImage, Review, TourPackage
from django.conf import settings


def home(request):
    packages = TourPackage.objects.filter(is_active=True, is_featured=True).select_related("destination")[:6]
    destinations = Destination.objects.filter(is_featured=True)[:6]
    reviews = Review.objects.filter(is_published=True)[:6]
    gallery = GalleryImage.objects.filter(is_published=True)[:8]
    return render(request, "travel/home.html", {"packages": packages, "destinations": destinations, "reviews": reviews, "gallery": gallery})


def packages(request):
    qs = TourPackage.objects.filter(is_active=True).select_related("destination")
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    if query:
        qs = qs.filter(Q(title__icontains=query) | Q(destination__name__icontains=query) | Q(short_description__icontains=query))
    if category:
        qs = qs.filter(category=category)
    return render(request, "travel/packages.html", {"packages": qs, "query": query, "category": category})


def package_detail(request, pk):
    package = get_object_or_404(TourPackage, pk=pk, is_active=True)
    form = BookingInquiryForm(request.POST or None, package=package)
    if request.method == "POST" and form.is_valid():
        inquiry = form.save()
        _notify_business(inquiry)
        messages.success(request, "Thank you! Your enquiry has been received. Our team will contact you shortly.")
        return redirect("package_detail", pk=package.pk)
    return render(request, "travel/package_detail.html", {"package": package, "form": form})


def book(request):
    form = BookingInquiryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        inquiry = form.save()
        _notify_business(inquiry)
        messages.success(request, "Your trip request has been submitted successfully. We will contact you soon.")
        return redirect("book")
    return render(request, "travel/book.html", {"form": form})


def contact(request):
    form = ContactMessageForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        message = form.save()
        _notify_contact(message)
        messages.success(request, "Your message has been sent. We will get back to you soon.")
        return redirect("contact")
    return render(request, "travel/contact.html", {"form": form})


def about(request):
    return render(request, "travel/about.html")


def gallery(request):
    images = GalleryImage.objects.filter(is_published=True)
    return render(request, "travel/gallery.html", {"images": images})


def _notify_business(inquiry):
    package_name = inquiry.package.title if inquiry.package else "Custom trip"
    subject = f"New Travel Enquiry — {inquiry.customer_name} — {inquiry.destination}"
    body = (
        f"Name: {inquiry.customer_name}\nPhone: {inquiry.phone}\nEmail: {inquiry.email or '-'}\n"
        f"Destination: {inquiry.destination}\nPackage: {package_name}\nTravel date: {inquiry.travel_date or '-'}\n"
        f"Travelers: {inquiry.travelers}\nBudget: {inquiry.budget or '-'}\nMessage: {inquiry.message or '-'}"
    )
    try:
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_RECEIVER_EMAIL], fail_silently=True)
    except Exception:
        pass


def _notify_contact(message):
    subject = f"Website Contact — {message.subject or message.name}"
    body = f"Name: {message.name}\nPhone: {message.phone or '-'}\nEmail: {message.email}\n\n{message.message}"
    try:
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_RECEIVER_EMAIL], fail_silently=True)
    except Exception:
        pass
