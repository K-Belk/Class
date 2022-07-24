from django.shortcuts import render
from .forms import InputForm
import requests as req

TICKETMASTER_API_KEY = 'T2DlzWRfcFlFNGz7Peke1c3OI0cL49Yw'


def _get_artist_shows(artist):
    clean_artist = artist.replace('', '%20')
    return f"https://app.ticketmaster.com/discovery/v2/events.json?keyword={clean_artist}&countryCode=US&apikey={TICKETMASTER_API_KEY}"

def home(request):
    if request.method == 'POST':
        artist = InputForm(request.POST)
        if artist.is_valid:
            print(artist)
            # resp = req.get(_get_artist_shows(artist))
            # shows = resp.json()
            # print(shows)
            data = {

            }

            return render(request, 'ticketmaster/home.html', data)
    else:
        artist = InputForm()
        return render(request, 'ticketmaster/home.html', {'artist': artist})

    # 