from django.urls import path
from source.views import (
    CreateSourceAPIView,
    SourceForMonthAPIView,
    UpdateEventAPIView,
    DeleteEventAPIView,
    CreateEventAPIView,
    SourcesListAPIView,
    UpdateSourceAPIView,
    DeleteSourceAPIView,
    DetailSourceAPIView,
    SaveSourceListCreateAPIView,
    CalendarExcelAPIView
    )

app_name = 'source'

urlpatterns = [
    path('',SourcesListAPIView.as_view(), name='sources-list') ,
    path('save/',SaveSourceListCreateAPIView.as_view(), name='sources-save') ,
    path('excel/',CalendarExcelAPIView.as_view(), name='calendar-excel') ,
    path('create/',CreateSourceAPIView.as_view(), name='sources-create') ,
    path('<int:pk>/',SourceForMonthAPIView.as_view(), name='source-month') ,
    path('<int:pk>/detail/',DetailSourceAPIView.as_view(), name='source-detail') ,
    path('<int:pk>/update/',UpdateSourceAPIView.as_view(), name='source-update') ,
    path('<int:pk>/delete/',DeleteSourceAPIView.as_view(), name='source-delete') ,

    #### Event Urls ####
    path('event/create/',CreateEventAPIView.as_view(), name='event-create') ,
    path('event/<int:pk>/update/',UpdateEventAPIView.as_view(), name='event-update') ,
    path('event/<int:pk>/delete/',DeleteEventAPIView.as_view(), name='event-delete') ,
]