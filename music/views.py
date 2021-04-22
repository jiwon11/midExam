from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from music.models import Music
from music.forms import MusicForm


def home(request):
    welcome = "Welcome to ABC Musical Store"
    return render(request, 'home.html', {'welcome' : welcome})


def author(request):
    author = "jiwon"
    return render(request, 'author.html', {'author' : author})


def list_musics(request):
    musics = Music.objects.all()
    return render(request, 'list_musics.html', {'musics': musics})


def create_music(request):
    form = MusicForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('music_detail_list')

    return render(request, 'music_form.html', {'form': form})


def update_music(request, id):
    music = Music.objects.get(id=id)
    form = MusicForm(request.POST or None, instance=music)

    if form.is_valid():
        form.save()
        return redirect('music_detail_list')

    return render(request, 'music_form.html', {'form': form, 'music': music})


def delete_music(request, id):
    music = Music.objects.get(id=id)

    if request.method == 'POST':
        music.delete()
        return redirect('music_detail_list')

    return render(request, 'music_delete_confirm.html', {'music': music})


from .filters import MusicFilter


def search(request):
    music_list = Music.objects.all()
    musics = MusicFilter(request.GET, queryset=music_list)
    return render(request, 'search.html', {'filter': musics})
