from django.db import models
from django.conf import settings
from django.shortcuts import reverse


CATEGORY_CHOICES = (
    ('TR', 'Televisions and RTV'),
    ('CT', 'Computers and tablets'),
    ('SW', 'Smartphones and watches'),
    ('PC','Photo and cameras'),
    ('GA','Gaming' ))

 # Televisions # All televisions # OLED # UHD / 4K # Smart TV # More... # Projectors # Projectors # Screens # 
 # Projector holders # Laser pointers # More... # TV mounts # Handles # The basics # Shelfs # Soundbars # Home cinemas 
 # Home theater systems # Wireless home theaters # Stereo sets # Soundbars # AV receivers and amplifiers # More... 
 # Players # Blu-ray players # DVD players # Multimedia players # Network players # Portable DVD players 
 # iPod, players, MP3 / MP4 # MP3 / MP4 players # Power audio # Headphones # All headphones # True Wireless headphones 
 # Headphones # Earphones # Wireless headphones # Wired headphones # Gaming headphones # More... # Party # DJ controllers 

 # Disco lights # Car audio # car radios # FM transmitters # Speakers # Recorders # CB radios # More... # Microphones 
 # HI-FI audio # Mobile speakers # Smart speakers # Multiroom systems # Micro and mini towers # Power audio # More... 
 # GPS navigation # GPS navigation # Accessories and chargers for navigation # DVB-T and satellite television # DVB-T tuners 
 # Satellite tuners # Antennas # Accessories for DVB-T and SAT TV # Small RTV equipment # Radios # radio # Clock radios
 # Voice recorders # Portable DVD players # RTV accessories # Audio-video cables # Audio cables # Speaker cables 
 # Power cables # Remotes # More... # Music equipment # Ukulele # DJ controllers # Studio microphones # Disco lights 
 # Codes and top-ups # Top-up movies and series # Music boost # Household appliances # Built-in household appliances 
 # Small household appliances # Bicycles # sport and Recreation # Scooters and skateboards # House and garden 
 # LEGO # Outlet # sale


LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    image = models.ImageField()
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self .slug
        })

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} of {self.item.title}" 


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username