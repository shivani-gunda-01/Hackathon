import requests
from django.shortcuts import render

def display_locations(request):
    if request.method == 'POST':
        location = request.POST['location']
        api_key = 'YOUR_API_KEY'  # Replace with your Maps API key
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
        params = {
            'key': api_key,
            'location': location,
            'radius': 20000,  # 20 km radius
            'type': 'point_of_interest'  # Change to your desired place type
        }
        response = requests.get(url, params=params)
        data = response.json()
        results = data['results']
        context = {
            'results': results,
        }
        return render(request, 'locations.html', context)
    else:
        return render(request, 'input.html')
