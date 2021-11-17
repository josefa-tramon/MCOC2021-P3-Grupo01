# MCOC2021-P3-Grupo01

Integrantes:

- Sofía Astraín
- Bastian Pavez
- Josefa Tramon

**ENTREGA 2**

                                                Figura 1

<div align="center">
<img src=https://user-images.githubusercontent.com/88339083/140987664-9cffc893-c697-4c4d-a431-eda5eef753c3.png >
</div>



                                                Figura 2 
<div align="center">
<img src=https://user-images.githubusercontent.com/62305749/141021100-a1365dd9-a0e8-4fc4-8c8c-9f900af8bf37.png >
</div>


                                                             
                                                Figura 3
<div align="center">
<img src=https://user-images.githubusercontent.com/88339083/140987867-1f26aa7a-8f9c-45ad-9253-89fcaa950387.png >
</div>                                               


                                                Figura 4                              
<div align="center">      
<img src=https://user-images.githubusercontent.com/88339083/140987888-392371ad-ebde-490f-aa2b-df9bed5c6ae9.png >
</div> 


* Para calcular las rutas más eficientes, se realizaron los supuestos de que en todo momento se viaja a velocidad máxima permitida sin demoras ni tiempos de espera por congestión. Lo cual es un escenario poco realistas, pero para fines prácticos, ayuda a comprender el  manejo de los grafos.

**ENTREGA 3**

Mapa - Sofía Astrain Verdugo

![Figure_1](https://user-images.githubusercontent.com/88336928/141456651-61ae4bda-7545-40c4-ab7e-225dab7c091b.png)

Mapa - Josefa Tramon

![Plano entrega 3](https://user-images.githubusercontent.com/62305749/141600357-f84a619a-3fe2-41f7-8b67-1884c30bb424.png)

Mapa - Bastian Pavez

![WhatsApp Image 2021-11-12 at 22 36 06](https://user-images.githubusercontent.com/88339083/141600923-52cae84b-c348-4640-8f15-7692c56e712d.jpeg)

**ENTREGA 4**

Para esta entrega nos pedian el equilibrio de Wardrop, a partir de del siguiente diagrama de red, con sus respectivas funciones de costos en cada arco:

                                               		 Figura 1

![Funciones](https://user-images.githubusercontent.com/62305749/142085506-985af2a0-65d8-4f94-a045-cb1e9602329e.png)


Luego se procedio a generar el algoritmo para resolver el equiibro de Wardrop, presente a continuación: (CAMBIAR CODIGO)

Funcion Costos: En este código se establece una función que estima el costo de circular por ese arco en base al flujo de vehículos que tiene.

```
	def costo(ni,nf,attr):
	#print(f"ni= {ni} nf= {nf} attr={attr}")
	funcosto_arco=attr["fcosto"]
	flujo_arco=attr["flujo"]
	return funcosto_arco(flujo_arco)

``` 

Función para equilibrio de Wardrop: Se realizan iteraciones en las cuales se incrementa paulatinamente el flujo de vehículos en los arcos asociados a una ruta mínima encontrada por la función "dijkstra_path()" correspondiente a la librería NetworkX, definiendo así de apoco un equilibrio de flujo tal que los costos de las distintas rutas para un par Origen Destino sea igual o lo más cercano a una igualdad posible. 

```
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

``` 

A partir de lo anterior se obtienen los siguientes resultados en los flujos finales por arco, para todo el sistema Origen Destino, el cual se presenta como Grafo a continuación:

                                               		 Figura 2

![Flujos](https://user-images.githubusercontent.com/62305749/142085111-93c6ee95-98e6-4105-8ce8-03780231130c.png)


Estos se puede ver con mayor detalle en la impresión que hace nuestro código en el terminal, al terminar de iterar los calculos de equilibrio para nuestra matriz OD evaluada:

                                               		 Figura 3

![WhatsApp Image 2021-11-16 at 20 50 10](https://user-images.githubusercontent.com/62305749/142085188-fbd62b5f-9438-40ee-9726-22a930296958.jpeg)

En esta se puede apreciar que el mayor porcentaje de error obtenido fue de un 12,4 %, y el menor fue de un 0,61 %. Estos de puede deber a la falta de exactitud de los valores en la convergencia al realizar la iteración en el incremento de los flujos en los arcos, y posterior calculo de costos, para luego rencontrar una nueva ruta mínima correspondiente a los nuevos valores otorgados.


