from django.http import HttpResponse
from django.shortcuts import render

from pdf2image import convert_from_path


def handle_uploaded_file(f):
    with open('tmp/test.pdf', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    images = convert_from_path('tmp/test.pdf')
    for i, image in enumerate(images):
        image.save(f'tmp/page{i:04}.png', 'png')


def index(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['pdf'])
    return render(request, 'pdfs/index.html')
