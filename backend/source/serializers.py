
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from source.models import Source,Event
from datetime import datetime,timedelta
from rest_framework import serializers

class CreateEventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['date', 'source', 'color']

class CreateEventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'source', 'date', 'color']



class EventSerializer(ModelSerializer):
    state = serializers.SerializerMethodField()
    visible = serializers.BooleanField(default=True)
    origin = serializers.BooleanField(default=True)
    class Meta:
        model = Event
        fields = ['id', 'source', 'date', 'color','state','visible', 'origin']

    def get_state(self, obj):
        return ''


class CreateSourceSerializer(ModelSerializer):
    events = EventSerializer(many=True,read_only=True)
    class Meta:
        model=Source
        fields=['id','name', 'user','events']

class SourceSerializer(ModelSerializer):
    events = EventSerializer(many=True)
    class Meta:
        model = Source
        fields = ['id','name', 'user', 'events']


class SourceMonthSerializer(ModelSerializer):
    events = SerializerMethodField()
    class Meta:
        model = Source
        fields = ['id','name', 'user', 'events']

    def get_events(self, obj):
        request =  self.context['request']
        date = request.GET.get('date', '')

        if not date:
            date = datetime.today().strftime('%Y-%m-%d')

        date = datetime.strptime(date, '%Y-%m-%d')
        results = Event.objects.filter(
                            source__id=obj.id,
                            date__year__gte=date.year,
                            date__month__gte=date.month,
                            date__year__lte=date.year,
                            date__month__lte=date.month)

        return EventSerializer(results, many=True).data
