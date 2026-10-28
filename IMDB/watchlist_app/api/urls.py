from django.urls import path
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import WatchListAV,WatchDetailAV,StreamPlatformAV,StreamPlatformDetailAV,ReviewList,ReviewCreate,ReviewDetail,WatchListGV

urlpatterns = [
    path('list/',WatchListAV.as_view(),name="movie-list"),
    path('<int:pk>/', WatchDetailAV.as_view(),name='movie-detail'),
    path('stream/',StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/',StreamPlatformDetailAV.as_view(), name='stream-detail'),
    
    path('<int:pk>/review/',ReviewList.as_view(),name='review-list'),
    path('<int:pk>/review-create/',ReviewCreate.as_view(), name='review-create'),
    path('review/<int:pk>/',ReviewDetail.as_view(),name='review-detail'),
    
    path('list2/',WatchListGV.as_view(),name='watch-list'),
    
]
