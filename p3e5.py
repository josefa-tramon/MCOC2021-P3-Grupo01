import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
import geopandas as gps
from networkx.algorithms import astar_path, all_simple_paths, all_shortest_paths, dijkstra_path


zonas_gdf = gps.read_file("eod.json")

north = -33.3637
south = -33.56
east = -70.5240
west = -70.680

G = ox.graph_from_bbox(north, south, east, west, 

						network_type = "drive",

						custom_filter='["highway"~"motorway|primary|secondary|tertiary|construction"]')

ox.config(use_cache = True, log_console = True)

gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)

plt.figure()

ax = plt.subplot(111)

zona_origen =  502 #poner nuestras zonas
zona_destino = 299 #poner nuestras zonas

zonas_gdf[zonas_gdf.ID == zona_origen].plot(ax=ax, color="#CDCDCD")
zonas_gdf[zonas_gdf.ID == zona_destino].plot(ax=ax, color="#CDCDCD")



# gdf_edges[gdf_edges.highway=="motorway"].plot(ax=ax, color="orange")
# gdf_edges[gdf_edges.highway=="primary"].plot(ax=ax, color="yellow")
# gdf_edges[gdf_edges.highway=="secondary"].plot(ax=ax, color="green")
# gdf_edges[gdf_edges.highway=="tertiary"].plot(ax=ax, color="blue")
#[598, 599, 146, 590, 587, 591, 506, 515, 506, 683, 666, 682, 677, 668, 306, 320, 321, 300, 669, 312, 296, 293, 269, 266, 292, 303, 304, 291, 307, 287, 288, 289, 290, 512, 505, 504, 513, 496, 507, 508, 498, 499, 500, 497, 503, 510, 511, 516, 434, 514, 267, 684, 313, 299]

id_zonas_a_graficar = [598, 599, 146, 590, 587, 591, 506, 515, 506, 683, 666, 682, 677, 668, 306, 320, 321, 300, 669, 312, 296, 293, 269, 266, 292, 303, 304, 291, 307, 287, 288, 289, 290, 512, 505, 504, 513, 496, 507, 508, 498, 499, 500, 497, 503, 510, 511, 516, 434, 514, 267, 684, 313, 299]
zonas_seleccionadas = zonas_gdf[zonas_gdf.ID.isin(id_zonas_a_graficar)]
centroids_seleccionados = zonas_seleccionadas.centroid

zonas_seleccionadas.plot(ax=ax, color="none")

###############################


colors = []
linewidth = []

for ni, nf, indice in G.edges:

	claves = G.edges[ni, nf, indice].keys()

	if 'name' in claves:
		
		highway = G.edges[ni, nf, indice]['highway']
		name    = G.edges[ni, nf, indice]['name']


		if highway == 'motorway':
			colors.append('orange')
			linewidth.append(1)

		elif highway == 'secondary':
			colors.append('green')
			linewidth.append(1)

		elif highway == 'tertiary':
			colors.append('blue')
			linewidth.append(1)

		elif highway == 'primary':
			colors.append('yellow')
			linewidth.append(1)

		elif name == 'Autopista Vespucio Oriente':
			colors.append('red')
			linewidth.append(5)

		else:
			colors.append('none')
			linewidth.append(1)

nuevos_edges = gps.clip(gdf_edges, zonas_seleccionadas)

nuevos_edges.plot(ax=ax, color = colors, linewidth = linewidth)


gdf_edges[gdf_edges.name == "Autopista Vespucio Oriente"].plot(ax=ax, color="red", linewidth=4)

plt.show()