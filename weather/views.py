from django.shortcuts import render

def home(request):
    import json
    import requests
    api_request = requests.get("http://api.meteored.cl/index.php?api_lang=cl&localidad=17725&affiliate_id=dypamzcc8893&v=3.0")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})