from django import forms
from .models import BookingInquiry, ContactMessage


class BookingInquiryForm(forms.ModelForm):
    travel_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = BookingInquiry
        fields = [
            "customer_name", "phone", "email", "destination", "package",
            "travel_date", "travelers", "budget", "message"
        ]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4, "placeholder": "Tell us what you need: hotels, vehicle, sightseeing, pickup, etc."}),
            "travelers": forms.NumberInput(attrs={"min": 1}),
        }

    def __init__(self, *args, package=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["package"].required = False
        self.fields["package"].queryset = self.fields["package"].queryset.filter(is_active=True)
        if package:
            self.fields["package"].initial = package
            self.fields["destination"].initial = package.destination.name


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "phone", "email", "subject", "message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 5})}
