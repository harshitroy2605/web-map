import folium 
import pandas

data=pandas.read_csv('stadium.csv',encoding="cp1252")

LAT=list(data['LAT'])
LON=list(data['LON'])
name=list(data['NAME'])
capacity=list(data['capacity'])
website=list(data['website'])
picture=list(data['picture'])

fg=folium.FeatureGroup('my map')
fg.add_child(folium.GeoJson(data=(open('india_states.json','r',encoding='utf-8-sig').read())))


 
for lt,ln,nm,cp,ws,pic in zip(LAT,LON,name,capacity,website,picture):
 	fg.add_child(folium.Marker(location=[lt,ln],popup="<b>name  : </b>"+nm+ "<br> <b>capacity : </b> "+str(cp)+"<br><b>wikipidea link: </b><a href="+ws+">click here</a>"+"<br> <img src="+pic+" height=142 width=290>",icon=folium.Icon(color='green')))


map=folium.Map(location=[21.1458,79.0882],zoom_start=5)





map.add_child(fg)
map.save('testmap1.html')