# MCOC2021-P3-Grupo01

Integrantes:

- Sofía Astraín
- Bastian Pavez
- Josefa Tramon

**ENTREGA 2**

                                                Figura 1

<div align="center">
<img src=https://user-images.githubusercontent.com/88339083/140987664-9cffc893-c697-4c4d-a431-eda5eef753c3.png width="350">
</div>



                                                Figura 2 
<div align="center">
<img src=https://user-images.githubusercontent.com/62305749/141021100-a1365dd9-a0e8-4fc4-8c8c-9f900af8bf37.png width="350">
</div>


                                                             
							Figura 3
<div align="center">
<img src=https://user-images.githubusercontent.com/88339083/140987867-1f26aa7a-8f9c-45ad-9253-89fcaa950387.png width="350">
</div>                                               


                                                Figura 4                              
<div align="center">      
<img src=https://user-images.githubusercontent.com/88339083/140987888-392371ad-ebde-490f-aa2b-df9bed5c6ae9.png width="350">
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


**ENTREGA 5**
A continuación, se presentan 3 grafos con diferentes demarcaciones, en los que se usarán los siguientes colores, según la jerarquía vial:
	1.-AVO=ROJO
	2.-MOTORWAY=NARANJO
	3.-PRIMARY= AMARILLO
	4.-SECONDARY= VERDE
	5.-TERTIARY= AZUL
	Imagen 1: Grafo con demarcación de calles, AVO y zonas de origen y destino 
	![WhatsApp Image 2021-11-19 at 8 32 27 PM (1)](https://user-images.githubusercontent.com/88339083/142704032-9552b134-16aa-406f-99ac-60f8313efa0e.jpeg)

	Imagen 2: Grafo con demarcación de calles, AVO y sus zonas influyentes, y zonas de origen y destino.
	![WhatsApp Image 2021-11-19 at 8 32 27 PM](https://user-images.githubusercontent.com/88339083/142704038-c9cab158-e1a6-4268-aa54-354bafc2a524.jpeg)

	Imagen 3: Grafo con demarcación de calles en zonas de origen y destino, y demarcación de AVO(ROJO).
	![WhatsApp Image 2021-11-19 at 8 32 28 PM](https://user-images.githubusercontent.com/88339083/142704051-be0370d3-ed78-43da-9270-50e235599c0b.jpeg)


¿Cómo seleccionó las zonas a incluir?
	Las zonas para incluir fueron todas aquellas por las que pasa el proyecto AVO, además de todas las que están lo más paralelas posibles a la construcción, puesto que, considerando temas de accesibilidad, aquellas que presenten esta condición (y por tanto una menor ortogonalidad), generarán un mayor flujo de vehículos puesto que su acceso será más expedito. 
Otro criterio, es que se trató de incluir zonas en las que existen lugares más concurridos, tales como colegios, malls y otros. 

¿Cuántas zonas quedaron seleccionadas son?
	Al considerar las zonas por las que pasa AVO y aquellas que muestras menor ortogonalidad, se seleccionaron un total de 55 correspondientes a  
598, 599, 146, 590, 587, 591, 506, 515, 506, 683, 666, 682, 677, 668, 306, 320, 321, 300, 669, 312, 296, 293, 269, 266, 292, 303, 304, 291, 307, 287, 288, 289, 290, 512, 505, 504, 513, 496, 507, 508, 498, 499, 500, 497, 503, 510, 511, 516, 434, 514, 267, 684,313,299,502
Luego, del total de zonas seleccionadas se eligieron 2 entre las cuales se realizarán los viajes a analizar. Que será desde la zona 502 a las 299 que considera viajes entre providencia y Las Condes, hasta el mall alto las Condes ubicados en la comuna de Las Condes. 
 
 ![image](https://user-images.githubusercontent.com/88339083/142703678-2c1862b2-771d-43fb-90d9-be529dcda306.png)

¿Cuántos viajes deberá asignar?
	Considerando que se contemplará como origen y destinos las zonas 508 y 299 respectivamente, en base a los dato de “Encuesta de origen destino” se deberá asignar un total de 5.332.656.104 viajes
 
 ![image](https://user-images.githubusercontent.com/88339083/142703686-0df7c771-bdf4-4f87-8f0f-442b64e0f168.png)
 
¿Cuáles son los pares OD que espera Ud. que generen mayor flujo en AVO?
	Los nodos para considerar los viajes serán los siguientes:

		Destino 1: Mall alto Las Condes
 
 ![image](https://user-images.githubusercontent.com/88339083/142703703-9037c084-6843-433a-89ff-e7cfeccaf36e.png

			Número de nodo: 98; Av. Padre Hurtado Central 
			Latitud: -33,3942
			Longitud: -70,54531

		Origen 1:

![image](https://user-images.githubusercontent.com/88339083/142703716-b77453dc-adff-4b3b-b53c-9d46bd107a21.png)

			Número de nodo: 3063; Las Achiras
			Latitud: -33,43164
			Longitud: -70,58603
		
		Origen 2:
 
![image](https://user-images.githubusercontent.com/88339083/142703723-fa6adf78-fc11-4409-a838-65a49d9a00f4.png)

			Número de nodo: 2999; Los tulipanes 
			Latitud: -33,43247
			Longitud: -70,58799
		
		Origen 3:

![image](https://user-images.githubusercontent.com/88339083/142703739-a85759c3-237b-4a41-bd9a-6102aceb2e0f.png)

			Número de nodo: 2069; Las Amapolas 
			Latitud: -33,43414
			Longitud: -70,58887

De lo anterior, se analizarán los nodos Origen-Destino según las combinaciones:
		Origen 1 - Destino 1
		Origen 2 - Destino 1
		Origen 3 - Destino 1
Esperando que la mayor realización de viajes ocurra según Origen 1 – Destino 1, puesto que en esa intersección nos encontramos cercanos a dos avenidas importantes, que corresponden a Tobalaba y Francisco Bilbao.









