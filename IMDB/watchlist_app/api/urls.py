from django.urls import path
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import MovieListAP,MovieDetailsAP

urlpatterns = [
    path('list/',MovieListAP.as_view(),name="movie_list"),
    path('<int:pk>/', MovieDetailsAP.as_view(),name='movie_details'),
]