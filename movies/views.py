from django.core.cache import cache

class TrendingMoviesView(APIView):
    def get(self, request):
        cache_key = "trending_movies"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        url = "https://api.themoviedb.org/3/trending/movie/week"
        params = { "api_key": settings.TMDB_API_KEY }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json().get('results', [])
            cache.set(cache_key, data, timeout=60 * 10)  # cache for 10 minutes
            return Response(data)
        except requests.RequestException:
            return Response({"error": "Failed to fetch trending movies"}, status=500)

class RecommendedMoviesView(APIView):
    def get(self, request):
        cache_key = "recommended_movies"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        url = "https://api.themoviedb.org/3/movie/top_rated"
        params = { "api_key": settings.TMDB_API_KEY }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json().get('results', [])[:10]
            cache.set(cache_key, data, timeout=60 * 10)  # 10 minutes
            return Response(data)
        except requests.RequestException:
            return Response({"error": "Failed to fetch recommended movies"}, status=500)
