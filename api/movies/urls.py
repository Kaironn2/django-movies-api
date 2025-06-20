from django.urls import path

from movies.views import (
    MovieListCreateView,
    MovieRetrieveUpdateDestroyView,
    MoviesByGenreListView,
    MovieStatsView,
)

urlpatterns = [
    path('', MovieListCreateView.as_view(), name='movie-list-create'),
    path('<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
    path('stats/', MovieStatsView.as_view(), name='movie-stats'),
    path('movies-by-genres/', MoviesByGenreListView.as_view(), name='movies-by-genres')
]
