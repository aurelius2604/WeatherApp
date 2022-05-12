from django.shortcuts import render
import json
import urllib.request
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        city_url = city.replace(" ", "%20")
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city_url+'&appid=2d6599e5237a4548bf6ebd6185afc048&units=metric').read()
        json_data = json.loads(res)
        data = {
            "country": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'C ' + ' Feels like  ' + str(json_data['main']['feels_like']) + 'C',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "city": city,
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', data)
