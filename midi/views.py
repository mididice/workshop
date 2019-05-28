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
    base_dir = settings.BASE_DIR
    basic_dir = os.path.join(base_dir, 'wavebasic')
    result_dir = settings.MEDIA_ROOT
    filename = ''.join(slug)+".wav"
    outfile = os.path.join(result_dir, filename)
    result_list = slug.split('-')
    if not os.path.isdir(result_dir):
        os.mkdir(result_dir)
    if not os.path.isfile(outfile):
        combine.tidalwave(basic_dir, result_list, outfile)
    return render(request, 'midi/result.html',
                  context={'music_list': result_list, 'music': filename, 'identification': slug})


def download(request, slug):
    file_path = os.path.join(settings.MEDIA_ROOT, slug+".wav")
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="audio/wav")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404