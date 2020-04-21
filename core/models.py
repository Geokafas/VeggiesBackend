from django.db import models
from django.conf import settings

#frouta/products
class Item(models.Model):
    CHOICES = [(1, 'ΦΡΟΥΤΑ'),(2, 'ΛΑΧΑΝΙΚΑ'),(3,'VEGGIESTREET')]

    product_title = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_id = models.IntegerField(primary_key=True)
    product_picture = models.ImageField(upload_to = 'items/', default = 'no-img.jpg')
    product_description = models.TextField(max_length = 300, blank = True, help_text = "Dwse mia perigrafi tou proiontos")
    product_quantity = models.IntegerField(default=1)
    product_category = models.IntegerField(choices=CHOICES, default=1)
    def __str__(self):
        return self.product_title

#prepei na ta ta3inomo sto admin panel analoga me to kathe proion
class ItemRatings(models.Model):
    CHOICES = [(1,'ΔΕΝ ΜΟΥ ΑΡΕΣΕ ΚΑΘΟΛΟΥ'),(2,'ΔΕΝ ΜΟΥ ΑΡΕΣΕ'),(3,'ΜΕΤΡΙΟ'),(4,'ΚΑΛΟ'),(5,'ΤΕΛΕΙΟ')]
    product_rating = models.IntegerField(choices=CHOICES)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.product_rating)

#prepei na ta ta3inomo sto admin panel analoga me to kathe proion
class ItemReviews(models.Model):
    product_review = models.TextField(max_length = 300, blank = True, help_text = "Dwse th gnwmmh sou gia to proion")
    pub_date = models.DateField()
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return self.product_review