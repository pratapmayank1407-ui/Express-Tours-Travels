from django.core.management.base import BaseCommand
from travel.models import Destination, TourPackage, Review, GalleryImage

DESTINATIONS = [
    ("Kashmir", "Lakes, mountains and scenic valleys.", "A flexible Kashmir plan covering Srinagar, Gulmarg and Pahalgam with room for custom stays and activities.", "https://images.unsplash.com/photo-1605649487212-47bdab064df7?auto=format&fit=crop&w=1200&q=80"),
    ("Manali", "Mountains, cafes and adventure.", "A practical Manali escape with local sightseeing, nature spots and flexible transport options.", "https://images.unsplash.com/photo-1595815771614-ade9d652a65d?auto=format&fit=crop&w=1200&q=80"),
    ("Goa", "Beaches, sunsets and slow days.", "Beach time, local experiences and a stay-and-sightseeing plan designed around your pace.", "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80"),
    ("Rajasthan", "Heritage, forts and colourful cities.", "Discover Jaipur, Jodhpur, Udaipur or a custom Rajasthan circuit with private travel options.", "https://images.unsplash.com/photo-1477587458883-47145ed94245?auto=format&fit=crop&w=1200&q=80"),
    ("Kerala", "Backwaters, greenery and coastlines.", "Combine Kochi, Munnar, Thekkady and Alleppey into a relaxed custom itinerary.", "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80"),
    ("Ayodhya & Varanasi", "Spiritual journeys from North India.", "A custom pilgrimage circuit with transfers, hotel stays and sightseeing planning.", "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=1200&q=80"),
]

PACKAGES = [
    ("Kashmir Highlights Escape", "Kashmir", "A scenic family-friendly route through Srinagar, Gulmarg and Pahalgam.", "Plan a balanced Kashmir journey with sightseeing, comfortable stays and transfers. Dates and hotel category can be customized for your group.", "6 Days / 5 Nights", 28999, "family"),
    ("Manali Mountain Break", "Manali", "A compact mountain holiday with local sightseeing and free time.", "A flexible Manali itinerary for couples, friends and families. Add activities, private cab options and extra nights as required.", "5 Days / 4 Nights", 21999, "adventure"),
    ("Goa Beach Escape", "Goa", "A relaxed beach trip with stays, transfers and sightseeing options.", "Choose North Goa, South Goa or a mix. The package can be adjusted for couples, families or friend groups.", "4 Days / 3 Nights", 16999, "honeymoon"),
    ("Royal Rajasthan Circuit", "Rajasthan", "A heritage-focused multi-city Rajasthan experience.", "Build a route around Jaipur, Jodhpur, Jaisalmer and Udaipur with private vehicle and hotel choices.", "7 Days / 6 Nights", 32999, "family"),
    ("Kerala Nature & Backwaters", "Kerala", "A green, slow-travel itinerary across Kerala highlights.", "Combine hill stations, backwaters and local experiences with comfortable transfers and hotel options.", "7 Days / 6 Nights", 31999, "custom"),
    ("Ayodhya & Varanasi Pilgrimage", "Ayodhya & Varanasi", "A practical spiritual journey with transfers and stays.", "Plan temple visits, local sightseeing, transfers and hotel stays around your preferred pace and travel dates.", "4 Days / 3 Nights", 14999, "pilgrimage"),
]

class Command(BaseCommand):
    help = "Seed starter content for Express Tours & Travels"

    def handle(self, *args, **options):
        destinations = {}
        for i, item in enumerate(DESTINATIONS):
            name, short, desc, img = item
            obj, _ = Destination.objects.get_or_create(name=name, defaults={"short_description": short, "description": desc, "image_url": img, "is_featured": True, "sort_order": i})
            destinations[name] = obj
        for title, dest, short, desc, duration, price, category in PACKAGES:
            if not TourPackage.objects.filter(title=title).exists():
                TourPackage.objects.create(
                    title=title, destination=destinations[dest], short_description=short, description=desc,
                    duration=duration, price_from=price, category=category,
                    image_url=destinations[dest].image_url, includes="Hotel accommodation\nTransfers / local transport (as quoted)\nSightseeing as per itinerary\nTrip planning support",
                    excludes="Personal expenses\nMeals not listed in final quotation\nOptional activities unless included in quote",
                    is_featured=True, is_active=True,
                )
        for name, rating, text in [
            ("Sample Traveller", 5, "The website is ready for real customer reviews. Add your genuine guest feedback from the admin panel."),
            ("Happy Guest", 5, "Replace this starter review with a verified customer review before launch."),
        ]:
            Review.objects.get_or_create(customer_name=name, defaults={"rating": rating, "text": text, "is_published": True})
        self.stdout.write(self.style.SUCCESS("Starter content created."))
