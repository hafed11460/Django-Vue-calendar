from source.permissions import IsSourceOwner, IsEventOwner
from rest_framework.permissions import IsAuthenticated
from source.serializers import CreateSourceSerializer
from source.serializers import (
    EventSerializer,
    SourceMonthSerializer,
    CreateEventSerializer,
)
from source.models import Source,Event

from source.serializers import SourceSerializer
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)

# Create your views here.





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
    permission_classes = [IsAuthenticated]
    serializer_class = CreateSourceSerializer
    queryset = Source.objects.all()


class DetailSourceAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated,IsSourceOwner]
    serializer_class = SourceSerializer
    queryset = Source.objects.all()


class UpdateSourceAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated,IsSourceOwner]
    serializer_class = CreateSourceSerializer
    queryset = Source.objects.all()


class DeleteSourceAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated,IsSourceOwner]
    serializer_class = SourceSerializer
    queryset = Source.objects.all()


##################### Events ########################
#####################        ########################


class CreateEventAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated ]
    serializer_class = CreateEventSerializer
    queryset = Event.objects.all()


class UpdateEventAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated,IsEventOwner]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class DeleteEventAPIView(DestroyAPIView):
    # permission_classes = [IsAuthenticated,IsEventOwner]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
