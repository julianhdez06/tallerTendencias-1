from rest_framework import serializers
from .models import *

class ReservationSerializers(serializers.ModelSerializer):
    event_name = serializers.SerializerMethodField()
    attendee_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Reservation
        fields = ['id', 'num_entrys', 'event_name', 'attendee_name']

    def get_event_name(self, obj):
        return obj.idEvent.name

    def get_attendee_name(self, obj):
        return obj.idAttendee.nombre
        
