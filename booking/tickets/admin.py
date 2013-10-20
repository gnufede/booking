from tickets.models import Event, EventOwner, EventAdmin, EventManager, TicketBuyer, Ticket
from django.contrib import admin
 
admin.site.register(Event)
admin.site.register(EventOwner)
admin.site.register(EventAdmin)
admin.site.register(EventManager)
admin.site.register(TicketBuyer)
admin.site.register(Ticket)
