import folium
import pandas

data=pandas.read_csv("stadium.csv" ,encoding = "cp1252")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
capacity=list(data["capacity"])
website=list(data["website"])
picture=list(data["picture"])

map=folium.Map(location=[23.379379735000043,79.44332654800007],zoom_start=5)

fg=folium.FeatureGroup(name="my map")


for lt,ln,nm,cp,ws,pic in zip(lat,lon,name,capacity,website,picture):
    fg.add_child(folium.Marker(location=[lt,ln],popup="<b>name  : </b>"+nm+ "<br> <b>capacity : </b> "+str(cp)+"<br><b>wikipidea link: </b><a href="+ws+">click here</a>"+"<br> <img src="+pic+" height=142 width=290>",icon=folium.Icon(color='green')))
fg.add_child(folium.GeoJson(data=(open('india_states.json','r',encoding='utf-8-sig').read())))

map.add_child(fg)

map.save("map1.html")