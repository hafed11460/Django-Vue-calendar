from django.urls import path
from source.views import (
    CreateSourceAPIView,
    SourceForMonthAPIView,
    UpdateEventAPIView,
    DeleteEventAPIView,
    CreateEventAPIView,
    SourcesListAPIView,
    )

urlpatterns = [
    path('',SourcesListAPIView.as_view(), name='sources-list') ,
    path('create/',CreateSourceAPIView.as_view(), name='sources-create') ,
    path('<int:pk>/',SourceForMonthAPIView.as_view(), name='source-month') ,

    #### Event Urls ####
    # path('',ListShiftAPIView.as_view(), name='shifts-list') ,
    path('event/create/',CreateEventAPIView.as_view(), name='event-create') ,
    path('event/<int:pk>/update/',UpdateEventAPIView.as_view(), name='event-update') ,
    path('event/<int:pk>/delete/',DeleteEventAPIView.as_view(), name='event-delete') ,
]