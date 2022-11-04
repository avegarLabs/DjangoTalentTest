from django.views import View
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from moviesRating.models import Movie, Rating, Reaction, Comment
import json


# this function are to created a movies crud
class MoviesViews(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        moviesList = list(Movie.objects.values())
        if len(moviesList) > 0:
            datos = {
                'message': "Success", 'movies': moviesList
            }
        else:
            datos = {
                'message': "Movies not found...."
            }
        return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Movie.objects.create(name=jd['name'], image=jd['image'],
                             url=jd['url'], language=jd['language'], summary=jd['summary'])
        datos = {
            'message': "Successs"
        }
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        items = list(Movie.objects.filter(id=id).values())
        if (len(items) > 0):
            movie = Movie.objects.get(id=id)
            movie.name = jd['name'],
            movie.image = jd['image'],
            movie.url = jd['url'],
            movie.language = jd['language'],
            movie.summary = jd['summary']
            movie.save()
            datos = {
                'message': "Successs"
            }
        else:
            datos = {
                'message': "Movie not found...."
            }
        return JsonResponse(datos)

    def delete(self, request, id):
        items = list(Movie.objects.filter(id=id).values())
        if (len(items) > 0):
            comentList = list(Comment.objects.filter(movieid=id).values())
            if len(comentList) > 0:
                for c in comentList:
                    Comment.objects.filter(id=c.id).delete()

            reactionList = list(Reaction.objects.filter(movieid=id).values())
            if len(reactionList) > 0:
                for r in reactionList:
                    Reaction.objects.filter(id=r.id).delete()
            Movie.objects.filter(id=id).delete()
            datos = {
                'message': "Delete Movie"
            }
        else:
            datos = {
                'message': "Movie not found...."
            }
        return JsonResponse(datos)
