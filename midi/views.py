from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.conf import settings
import os
import os.path
import numpy as np
from midi import combine


def index(request):
    midi_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
    np.random.shuffle(midi_list)
    return render(request, 'midi/index.html', {'json_list': midi_list})


def make_one(request, slug):
    static_dir = settings.STATIC_ROOT
    wave_dir = os.path.join(static_dir, 'wave')
    result_dir = settings.MEDIA_ROOT
    result_dir = os.path.join(result_dir, 'one')
    filename = ''.join(slug)+".wav"
    outfile = os.path.join(result_dir, filename)
    altslug = slug.replace('_', '+')
    result_list = altslug.split('-')
    if not os.path.isdir(result_dir):
        os.mkdir(result_dir)
    if not os.path.isfile(outfile):
        combine.tidalwave(wave_dir, result_list, outfile)
    return render(request, 'midi/result.html',
                  context={'music_list': result_list, 'music': filename, 'identification': slug, 'type':"one/"})

def make_bright(request, slug):
    static_dir = settings.STATIC_ROOT
    wave_dir = os.path.join(static_dir, 'wave')
    wave_dir = os.path.join(wave_dir, 'bright')
    result_dir = settings.MEDIA_ROOT
    result_dir = os.path.join(result_dir, 'bright')
    filename = ''.join(slug)+".wav"
    outfile = os.path.join(result_dir, filename)
    altslug = slug.replace('_', '+')
    result_list = altslug.split('-')
    if not os.path.isdir(result_dir):
        os.mkdir(result_dir)
    if not os.path.isfile(outfile):
        combine.tidalwave(wave_dir, result_list, outfile)
    return render(request, 'midi/result.html',
                  context={'music_list': result_list, 'music': filename, 'identification': slug, 'type':"bright/"})

def make_dark(request, slug):
    static_dir = settings.STATIC_ROOT
    wave_dir = os.path.join(static_dir, 'wave')
    wave_dir = os.path.join(wave_dir, 'dark')
    result_dir = settings.MEDIA_ROOT
    result_dir = os.path.join(result_dir, 'dark')
    filename = ''.join(slug)+".wav"
    outfile = os.path.join(result_dir, filename)
    altslug = slug.replace('_', '+')
    result_list = altslug.split('-')
    if not os.path.isdir(result_dir):
        os.mkdir(result_dir)
    if not os.path.isfile(outfile):
        combine.tidalwave(wave_dir, result_list, outfile)
    return render(request, 'midi/result.html',
                  context={'music_list': result_list, 'music': filename, 'identification': slug, 'type':"dark/"})

def make_mixed(request, slug):
    static_dir = settings.STATIC_ROOT
    wave_dir = os.path.join(static_dir, 'wave')
    wave_dir = os.path.join(wave_dir, 'mixed')
    result_dir = settings.MEDIA_ROOT
    result_dir = os.path.join(result_dir, 'mixed')
    filename = ''.join(slug)+".wav"
    outfile = os.path.join(result_dir, filename)
    altslug = slug.replace('_', '+')
    result_list = altslug.split('-')
    if not os.path.isdir(result_dir):
        os.mkdir(result_dir)
    if not os.path.isfile(outfile):
        combine.tidalwave(wave_dir, result_list, outfile)
    return render(request, 'midi/result.html',
                  context={'music_list': result_list, 'music': filename, 'identification': slug, 'type':'mixed/'})

def download(request, type, slug):
    file_path = os.path.join(settings.MEDIA_ROOT, type)
    file_path = os.path.join(file_path, slug+".wav")
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="audio/wav")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def dark(request):
    midi_list = ['A','B','C','D','E','F']
    return render(request, "midi/dark.html", {'json_list': midi_list})

def bright(request):
    midi_list = ['A','B','C','D','E','F']
    return render(request, "midi/bright.html", {'json_list': midi_list})

def mixed(request):
    midi_list = ['A','B','C','D','E','F','G','H','I','J','K','L']
    return render(request, "midi/mixed.html", {'json_list': midi_list})

def dice(request):
    return render(request, 'midi/dice.html')