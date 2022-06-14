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

class SourceForMonthAPIView(RetrieveAPIView):
    # permission_classes = [IsAuthenticated,IsManager]
    serializer_class = SourceMonthSerializer
    queryset = Source.objects.all()
    # def get_queryset(self):
    #     user = self.request.user
    #     return Source.objects.filter(is_admin=False,location=user.location)


class SourcesListAPIView(ListAPIView):
    serializer_class = SourceMonthSerializer
    def get_queryset(self):
        return Source.objects.all()

class CreateSourceAPIView(CreateAPIView):
    # permission_classes = [IsAuthenticated,IsManager ]
    serializer_class = CreateSourceSerializer
    queryset = Source.objects.all()


##################### Events ########################
class CreateEventAPIView(CreateAPIView):
    # permission_classes = [IsAuthenticated,IsManager ]
    serializer_class = CreateEventSerializer
    queryset = Event.objects.all()


class UpdateEventAPIView(UpdateAPIView):
    # permission_classes = [IsAuthenticated,IsManager ]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class DeleteEventAPIView(DestroyAPIView):
    # permission_classes = [IsAuthenticated,IsManager ]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
