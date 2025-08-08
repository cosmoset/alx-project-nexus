from rest_framework.permissions import IsAuthenticated
from .models import FavoriteMovie
from .serializers import FavoriteMovieSerializer

class FavoriteMovieView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        favorites = FavoriteMovie.objects.filter(user=request.user)
        serializer = FavoriteMovieSerializer(favorites, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FavoriteMovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        movie_id = request.data.get('movie_id')
        favorite = FavoriteMovie.objects.filter(user=request.user, movie_id=movie_id).first()
        if favorite:
            favorite.delete()
            return Response({"message": "Removed from favorites"}, status=204)
        return Response({"error": "Not found"}, status=404)
