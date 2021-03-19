from django.shortcuts import render
import folium

def index(request):
    return render(request, 'index.html')

def map(request):
    #Create Map
    m = folium.Map(location=[38.1721923828125, 30.23360859943705], zoom_start=6)
    #Add Marker
    folium.Marker(location=[37.1721923828125, 28.23360859943705], tooltip='Click For More Information',
                  popup='Muğla \n Yüzölçümü:12.974 \n Nüfus:1.015.229').add_to(m)
    folium.Marker(location=[39.9921923828125, 32.23360859943705], tooltip='Click For More Information',
                  popup='Ankara \n Yüzölçümü:25.437 \n Nüfus:5.663.322').add_to(m)
    #Add TileLayer
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)
    folium.LayerControl().add_to(m)
    #Get HTML representation of map
    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'map.html', context)