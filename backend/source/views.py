
from unicodedata import name

from django.shortcuts import get_object_or_404
from source.permissions import IsSourceOwner, IsEventOwner
from rest_framework.permissions import IsAuthenticated
from source.serializers import CreateSourceSerializer
from source.serializers import (
    EventSerializer,
    SourceMonthSerializer,
    CreateEventSerializer,
)
from source.models import Source, Event
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from source.serializers import SourceSerializer
from datetime import datetime,timedelta
from django.http import HttpResponse
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    ListCreateAPIView,
)
from source.excel import createExcelFile
# Create your views here.

class CalendarExcelAPIView(APIView):

    def get(self, request, format=None):
        date = request.GET.get('date', '')
        if not date:
            date =datetime.today().strftime('%Y-%m-%d')
        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=your_template_name.xlsx'
        excel_file = createExcelFile(date)
        response.write(excel_file)
        return response


class SaveSourceListCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated ]
    serializer_class = SourceMonthSerializer

    def post(self, request, format=None):
        data = request.data.get("data")
        sources = data['sources']
        date = data['date']
        print('------------------------------------------------------------------------ ')

        createEvents = []
        updateEvents = []
        deleteEvents = []
        # print(sources)
        for source in sources:
            for event in source['events']:
                if event['state'] == 'create':
                    create_vent = CreateEventSerializer(data=event)
                    if create_vent.is_valid():
                        createEvents.append(
                            Event(**create_vent.validated_data))
                if event['state'] == 'update':
                    event_instance = get_object_or_404(
                        Event, id=int(event['id']))
                    event_instance.color = event['color']
                    updateEvents.append(event_instance)
                if event['state'] == 'delete':
                    deleteEvents.append(int(event['id']))

        print('Create Events ', createEvents)
        print('Uodate Events ', updateEvents)
        print('Delete Events ', deleteEvents)
        Event.objects.bulk_create(createEvents)
        Event.objects.bulk_update(updateEvents, ['color'])
        Event.objects.filter(id__in=deleteEvents).delete()

        context = {}
        # context['data'] = sources
        context['message'] = 'success'
        return Response(context,status=status.HTTP_200_OK   )


class SourcesListAPIView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = SourceMonthSerializer
    queryset = Source.objects.all()
    # def get_queryset(self):
    #     user = self.request.user
    #     return Source.objects.filter(user=user)


class SourceForMonthAPIView(RetrieveAPIView):
    # permission_classes = [IsAuthenticated,IsSourceOwner]
    serializer_class = SourceMonthSerializer
    queryset = Source.objects.all()


class CreateSourceAPIView(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = CreateSourceSerializer
    queryset = Source.objects.all()


class DetailSourceAPIView(RetrieveAPIView):
    # permission_classes = [IsAuthenticated,IsSourceOwner]
    serializer_class = SourceSerializer
    queryset = Source.objects.all()


class UpdateSourceAPIView(UpdateAPIView):
    # permission_classes = [IsAuthenticated,IsSourceOwner]
    serializer_class = CreateSourceSerializer
    queryset = Source.objects.all()


class DeleteSourceAPIView(DestroyAPIView):
    # permission_classes = [IsAuthenticated,IsSourceOwner]
    serializer_class = SourceSerializer
    queryset = Source.objects.all()


##################### Events ########################
#####################        ########################


class CreateEventAPIView(CreateAPIView):
    # permission_classes = [IsAuthenticated ]
    serializer_class = CreateEventSerializer
    queryset = Event.objects.all()


class UpdateEventAPIView(UpdateAPIView):
    # permission_classes = [IsAuthenticated,IsEventOwner]
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class DeleteEventAPIView(DestroyAPIView):
    # permission_classes = [IsAuthenticated,IsEventOwner]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
