from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.


def index(request):

    movies = Movie.objects.all()
    return render(request=request,  template_name="movies/index.html",
                  context={"movies": movies})


def detail(request, movie_id):
    # regular
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    #     return render(request=request, template_name="movies/detail.html", context={"movie": movie})
    # except Movie.DoesNotExist:
    #     raise Http404()

    #  Django shotcut
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request=request, template_name="movies/detail.html", context={"movie": movie})
