from django.contrib import sitemaps
from django.urls import reverse

class CustomSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    protocol = 'https'
    priority = 1.0

    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['index', 'about', 'login', 'signup', 'dashboard']

    def location(self, item):
        return reverse(item)  # More concise way to handle all routes
    
    
    
