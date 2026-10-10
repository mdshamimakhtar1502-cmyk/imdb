from django.urls import path
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import WatchListAV,WatchDetailsAV,StreamPlatformAV,StreamPlatformDetailAV

urlpatterns = [
    path('list/',WatchListAV.as_view(),name="WatchListAV"),
    path('<int:pk>/', WatchDetailsAV.as_view(),name='WatchDetailsAV'),
    path('stream/',StreamPlatformAV.as_view(), name='StreamPlatformAV'),
    path('stream/<int:pk>/',StreamPlatformDetailAV.as_view(), name='StreamPlatformDetailAV'),
    
]
