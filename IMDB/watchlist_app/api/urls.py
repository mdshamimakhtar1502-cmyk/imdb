from django.urls import path
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import WatchListAV,WatchDetailsAV,StreamPlatformAV,StreamPlatformDetailAV,ReviewList,ReviewCreate,ReviewDetail

urlpatterns = [
    path('list/',WatchListAV.as_view(),name="movie_list"),
    path('<int:pk>/', WatchDetailsAV.as_view(),name='movie_detail'),
    path('stream/',StreamPlatformAV.as_view(), name='stream_list'),
    path('stream/<int:pk>/',StreamPlatformDetailAV.as_view(), name='stream_detail'),
    
    path('stream/<int:pk>/review/',ReviewList.as_view(),name='review-list'),
    path('stream/<int:pk>/review-create/',ReviewCreate.as_view(), name='review-create'),
    path('stream/review/<int:pk>/',ReviewDetail.as_view(),name='review-detail')
    
]
