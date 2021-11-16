import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import dijkstra_path

#DEFINIMOS FUNCIONES DE COSTOS QUE SERÀN ASOCIADOS A CADA ARCO POSTERIORMETNTE
f1=lambda f: 10 + f/120	    #r,v,z
f2=lambda f: 14 + 3*f/240	#s,u,w,y
f3=lambda f: 10 + f/240 	#t,x

#MATRIZ ORIGEN DESTINO
OD={
	("A","C"):1100.,
	("B","C"):1140.,
	("D","C"):350.,
	("A","D"):1110.,
	("B","D"):1160.,
	("A","E"):1020.,
	("C","E"):1170.,
	("D","E"):1190.,
	("C","G"):1180.,
	("D","G"):1200.,
	}


#UNA COPIA DE MATRIZ ORIGEN DESTINO
OD_target=OD.copy()


#CREAREMOS UN GRAFO
G=nx.Graph()

#ASIGNACION DE NODOS
G.add_node("A", pos=(0,4))
G.add_node("B", pos=(0,2))
G.add_node("C", pos=(2,2))
G.add_node("D", pos=(2,0))
G.add_node("E", pos=(4,4))
G.add_node("G", pos=(4,2))

#ASIGNAMOS LOS ARCOS ENTRE NODOS, SU RESPECTIVO COSTO y flujo
G.add_edge("A","B", fcosto= f1, flujo=0., costo=0.)       #r
G.add_edge("A","C", fcosto= f2, flujo=0., costo=0.)       #s
G.add_edge("B","D", fcosto= f2, flujo=0., costo=0.)       #u
G.add_edge("B","C", fcosto= f3, flujo=0., costo=0.)       #t
G.add_edge("C","G", fcosto= f3, flujo=0., costo=0.)	   #x
G.add_edge("C","E", fcosto= f2, flujo=0., costo=0.)	   #w
G.add_edge("D","C", fcosto= f1, flujo=0., costo=0.)	   #v
G.add_edge("D","G", fcosto= f2, flujo=0., costo=0.)	   #y
G.add_edge("G","E", fcosto= f1, flujo=0., costo=0.)	   #z


def costo(ni,nf,attr):
	#print(f"ni= {ni} nf= {nf} attr={attr}")
	funcosto_arco=attr["fcosto"]
	flujo_arco=attr["flujo"]
	return funcosto_arco(flujo_arco)

C_arc=[]

#demanda=1000.
while True:

	se_asigno_demanda=False

	for key in OD:
		origen= key[0]
		destino=key[1]
		demanda_actual=OD[key]
		demanda_objetivo=OD_target[key]


		if demanda_actual>0:

			#RUTA MÌNIMA PARA LLEGAR DE A A E
			path=dijkstra_path(G,origen,destino, weight=costo)



			#PARA UN GRAFO GRANDE USAR ASTAR_PATH


			#INCREMENTAMOS FLUJO EN LA RUTA MÌNIMA
			Nparadas=len(path)
			#print(Nparadas)

			for i_parada in range(Nparadas-1):
				#print(f" i_parada= {i_parada}")
				o=path[i_parada]
				d=path[i_parada+1]

				#print(f"o={o} d={d}")

				flujo_antes=G.edges[o,d]["flujo"]
				#print(f"incrementamos de {o} a {d} flujo era {flujo_antes}")
				G.edges[o,d]["flujo"]+=0.01
				#print(G.edges[o,d]["flujo"])

			#print(f"{origen}- {destino}: demanda {demanda_actual} {path}")
			#print(OD[key])
			OD[key]-=0.01 #DECREMENTAR PROPORCIONAL A LA DEMANDA ACTUAL
			se_asigno_demanda=True

	if not se_asigno_demanda:
		break

#print(G.edges)
#SOLO PARA VER COSTOS
for ni,nf in G.edges:
	arco=G.edges[ni,nf]
	funcosto_arco=arco["fcosto"]
	flujo_arco=arco["flujo"]
	arco["costo"]= funcosto_arco(flujo_arco)
	C_arc.append(arco["costo"])

#print(C_arc)
#print(Costos_final)	

#VERIFICAR EQUILIBRIO
#Evaluamos costos 
Cost_arcos=[37.25, 63.79, 76.64, 15.83, 42.38, 39.39, 18.14, 18.04, 57.42, 36.19]
nodos_cost=["A-C","A-D","A-E", "B-C","B-D","C-E", "C-G", "D-C", "D-E", "D-G"]
rutas=[["s, r-t"],["r-u"],["s-w, s-x-z, r-t-w, r-t-x-z"],["t"],["u"],["w, x-z"],["x"],["v"],["y-z, v-x-z, v-w"],["y, v-x"]]
#print(rutas[0])
Costos_arcos_ob=[C_arc[1], C_arc[0]+C_arc[2], C_arc[1]+C_arc[5], C_arc[3], C_arc[2], C_arc[5], C_arc[4], C_arc[6], C_arc[7]+C_arc[8], C_arc[7]]
error=[]
for i in range(len(Costos_arcos_ob)):
	a=((abs(Cost_arcos[i]-Costos_arcos_ob[i]))/Cost_arcos[i])*100
	error.append(a)
#print(error)

for j in range(len(error)):
	print(f"Origen-Destino= {nodos_cost[j]}  rutas {rutas[j]} Costo de pauta= {round(Cost_arcos[j],2)} Costo Obtenido= {round(Costos_arcos_ob[j],2)} Error={round(error[j],2)}%")
	print("")
	print("")


#PLOTEO DE FIGURA 1 (FLUJO)
plt.figure(1)
ax1=plt.subplot(111)
pos=nx.get_node_attributes(G,"pos")
nx.draw(G,pos,with_labels=True, font_weight="bold")
labels=nx.get_edge_attributes(G,"flujo")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.suptitle(f"FLUJOS")


#PLOTEO FIGURA 2 (COSTO)
plt.figure(2)
ax1=plt.subplot(111)
pos=nx.get_node_attributes(G,"pos")
nx.draw(G,pos,with_labels=True, font_weight="bold")
labels=nx.get_edge_attributes(G,"costo")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.suptitle(f"COSTOS")


r = f'10 + f/120'
s = f'14 + 3*f/240'
t = f'10 + f/240'
u = s
v = r
w = s
x = t
y = s
z = r


plt.figure(3)
ax1 = plt.subplot(111)
pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos,with_labels=True,font_weight="bold",arrows= False)
labels = nx.get_edge_attributes(G,'flujo') 
nx.draw_networkx_edge_labels(G,pos,
							edge_labels={('A', 'B'): r, 
						                 ('A', 'C'): s, 
						                 ('B', 'C'): t,
						                 ('B', 'D'): u, 
						                 ('C', 'D'): v, 
						                 ('C', 'E'): w,
						                 ('C', 'G'): x, 
						                 ('D', 'G'): y, 
						                 ('E', 'G'): z}) #en este pongo el label de funcion

plt.suptitle(f"FUNCION DE COSTO POR ARCO")





##########
plt.show()
##########

