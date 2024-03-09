import requests
from django.shortcuts import render
from django.http import JsonResponse


def home_view(request):
    return render(request, 'weather_app/index.html')


def get_weather_data(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        country = request.GET.get('country')
        api_key = '7aed8943db39fcaa28c231d00762f70f'

        if not city or not country:
            return JsonResponse({'error': 'City and country parameters are required.'}, status=400)

        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric')

        if response.status_code == 200:
            data = response.json()

            icon_code = data['weather'][0]['icon']

            weather_data = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'condition': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'icon_url': f'https://openweathermap.org/img/wn/{icon_code}.png',
            }

            return JsonResponse(weather_data)
        else:
            return JsonResponse({'error': 'Failed to fetch weather data. Please try again later.'},
                                status=response.status_code)

    return JsonResponse({'error': 'Invalid request method'})
