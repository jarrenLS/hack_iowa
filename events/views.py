from django.views.generic import FormView
from django.shortcuts import get_object_or_404

from .forms import RSVPForm
from .models import Attendee, Event


class RSVPView(FormView):
    form_class = RSVPForm
    template_name = 'events/rsvp.html'
    
    def dispatch(self, request, event_pk, *args, **kwargs):
        self.event = get_object_or_404(Event, pk=event_pk)
        return super(RSVPView, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        email = form.cleaned_data['email']
        created, attendee = Attendee.objects.get_or_create(email=email)
        self.event.attendees.add(attendee)
        return super(RSVPView, self).form_valid(form)