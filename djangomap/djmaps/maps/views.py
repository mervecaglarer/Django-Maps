from django.shortcuts import render

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoibWVydmVjYWdsYXJlciIsImEiOiJja2x6NGZ2OXYyOWNhMm9wM3V1aDdud29xIn0.RfG1DMP7YLoYHO5G3O2VoA'
    return render(request, 'default.html', {'mapbox_access_token': mapbox_access_token })