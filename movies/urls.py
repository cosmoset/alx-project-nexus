from .views import FavoriteMovieView

urlpatterns += [
    path('favorites/', FavoriteMovieView.as_view(), name='favorite-movies'),
]
