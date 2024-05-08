"""Main module."""
import ipyleaflet
from ipyleaflet import basemaps
from networkx import bfs_layers

class Map(ipyleaflet.Map):
    def __init__(self,center=[-10,35], zoom=5, **kwargs):
        super().__init__(center=center, zoom=zoom, **kwargs)
      
    
    
    def add_title_layer(self, url, name, **kwargs):
        layer = ipyleaflet.TileLayer(url=url, name=name, **kwargs)
        self.add_layer(layer)
        
    def add_basemaps(self, name):
        
        if isinstance(name, str):
            url = eval(f"basemaps.{name}").build_url()
            self.add_title_layer(url, name)
        else:
            self.add(name)
            
    def add_layers_control(self, position='topright'):
       self.add_layer(ipyleaflet.LayersControl(position=position))