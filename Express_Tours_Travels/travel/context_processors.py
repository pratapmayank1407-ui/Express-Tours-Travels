from django.conf import settings


def site_settings(request):
    return {
        "business_name": "Express Tours & Travels",
        "phone_primary": "8115922455",
        "phone_secondary": "8471075977",
        "email": "pratap.mayank1407@gmail.com",
        "city": "Lucknow, Uttar Pradesh",
        "maps_url": settings.GOOGLE_MAPS_URL,
        "map_lat": settings.MAP_LAT,
        "map_lng": settings.MAP_LNG,
        "whatsapp_primary": "https://wa.me/918115922455",
        "whatsapp_secondary": "https://wa.me/918471075977",
    }
