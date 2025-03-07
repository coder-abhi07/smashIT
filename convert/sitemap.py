from django.contrib import sitemaps
from django.urls import reverse

class CustomSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    protocol = 'https'
    priority = 1.0

    def items(self):
        # Return a list of URL names you want to include in the sitemap
        return ['index', 'login', 'logout', 'callback', 'result']

    def location(self, item):
        # Define the URL for each item in the sitemap
        if item == 'index':
            return reverse('index')
        if item == 'login':
            return reverse('login')
        if item == 'logout':
            return reverse('logout')
        if item == 'callback':
            return reverse('callback')
        if item == 'result':
            return reverse('result')
        
        
