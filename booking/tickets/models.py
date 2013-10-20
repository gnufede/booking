from django.db import models
from django.contrib.auth.models import User
#from core.models import TimeStampedModel
from model_utils.models import TimeStampedModel, TimeFramedModel

from decimal import Decimal

class EventManager(models.Model):
    user = models.ForeignKey(User)
    shop = models.TextField()

class EventOwner(models.Model):
    user = models.OneToOneField(EventManager)

class EventAdmin(models.Model):
    user = models.OneToOneField(User)

# Create your models here.
class Event(TimeStampedModel, TimeFramedModel):
    owner = models.ForeignKey(EventOwner)
    admins = models.ManyToManyField(EventAdmin)
    title = models.TextField(max_length=100)
    slug = models.SlugField(blank=True)
    description = models.TextField()
#    start_time = models.DateTimeField()
#    end_time = models.DateTimeField()
    max_tickets = models.IntegerField()
    available_tickets = models.IntegerField()
    original_ticket_price = models.DecimalField(max_digits=20, decimal_places=2)
    ticket_price = models.DecimalField(max_digits=20,decimal_places=2)
    published = models.BooleanField()
    published_date = models.DateTimeField()

    class Meta:
        permissions = (
            ("view_event", "Can see the event"),
            ("publish_event","Can publish event"),
#            ("change_event","Can change event info"),
            ("change_ticket_price","Can change ticket price"),
            ("create_event","Can create events"),
#            ("delete_event","Can delete event"),
        )

    def __unicode__(self):
        return self.title

class TicketBuyer(models.Model):
    user = models.OneToOneField(User)

class Ticket(TimeStampedModel):
    event = models.ForeignKey(Event)
    owner = models.ForeignKey(TicketBuyer)
    price = models.DecimalField(max_digits=20,decimal_places=2)

    def __unicode__(self):
        return self.event.title +', ' + self.user.name
    
