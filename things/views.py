from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_view(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Things</title>
    </head>
    <body>
        <h1>Things</h1>
    </body>
    </html>
    """
    return HttpResponse(html)

