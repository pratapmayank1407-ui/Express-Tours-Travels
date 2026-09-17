from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Destination",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("short_description", models.CharField(max_length=220)),
                ("description", models.TextField(blank=True)),
                ("image_url", models.URLField(blank=True)),
                ("is_featured", models.BooleanField(default=True)),
                ("sort_order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["sort_order", "name"]},
        ),
        migrations.CreateModel(
            name="GalleryImage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("image", models.ImageField(blank=True, null=True, upload_to="gallery/")),
                ("image_url", models.URLField(blank=True)),
                ("alt_text", models.CharField(blank=True, max_length=180)),
                ("is_published", models.BooleanField(default=True)),
                ("sort_order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["sort_order", "-id"]},
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("customer_name", models.CharField(max_length=100)),
                ("rating", models.PositiveSmallIntegerField(default=5)),
                ("text", models.TextField()),
                ("is_published", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("phone", models.CharField(blank=True, max_length=25)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(blank=True, max_length=180)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="TourPackage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=160)),
                ("short_description", models.CharField(max_length=280)),
                ("description", models.TextField()),
                ("duration", models.CharField(help_text="Example: 5 Days / 4 Nights", max_length=60)),
                ("price_from", models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ("category", models.CharField(choices=[("family", "Family"), ("honeymoon", "Honeymoon"), ("adventure", "Adventure"), ("pilgrimage", "Pilgrimage"), ("custom", "Custom")], default="custom", max_length=30)),
                ("image_url", models.URLField(blank=True)),
                ("includes", models.TextField(blank=True, help_text="One item per line")),
                ("excludes", models.TextField(blank=True, help_text="One item per line")),
                ("is_featured", models.BooleanField(default=True)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("destination", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="packages", to="travel.destination")),
            ],
            options={"ordering": ["-is_featured", "-created_at"]},
        ),
        migrations.CreateModel(
            name="BookingInquiry",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("customer_name", models.CharField(max_length=120)),
                ("phone", models.CharField(max_length=25)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("destination", models.CharField(max_length=120)),
                ("travel_date", models.DateField(blank=True, null=True)),
                ("travelers", models.PositiveIntegerField(default=1)),
                ("budget", models.CharField(blank=True, max_length=80)),
                ("message", models.TextField(blank=True)),
                ("status", models.CharField(choices=[("new", "New"), ("contacted", "Contacted"), ("confirmed", "Confirmed"), ("cancelled", "Cancelled")], default="new", max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("package", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="inquiries", to="travel.tourpackage")),
            ],
            options={"ordering": ["-created_at"], "verbose_name": "Booking enquiry", "verbose_name_plural": "Booking enquiries"},
        ),
    ]
