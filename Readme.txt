Para ejecutar cualquiera de los dos algoritmos es 
necesario usar los siguientes comandos:

 py Boruvka TestCases/test00.txt
 py Kruskal TestCases/test00.txt

En caso de necesitar un caso de prueba para el algoritmo de Boruvka,
el programa "randomGraphGenerator" generará un grafo conexo de entre 10
a 500 nodos de manera aleatoria y guardará la imagen del grafo en la carpeta
en la que se encuentre el .py. Para poder ejecutar este programa se necesitan
las siguientes librerias: networkx y matplotlib y se pueden instalar con los
siguientes comandos:

py -m pip install matplotlib
py -m pip install networkx

Una vez instaladas las librerias el programa se puede ejecutar con el siguiente
comando:

py randomGraphGenerator.py

La salida del grafo generado se guardará en un archivo .txt llamado "outFile.txt",
con el siguiente formato:

Primer nodo - Segundo nodo - Peso
Por ejemplo: Nodo 1 - Nodo 3 - 4 (1 - 3  4)

Si se desea visualizar el grafo, el programa guarda automaticamente el grafo 
generado como imagen en la carpeta donde se encuentra el .py, con el nombre de
"filename.png".

Tanto el programa de Kruskal como Boruvka dibujan los MST resultantes, pero está
mejora hizo que su tiempo de ejecución aumentara, por lo que si se desea obtener
mejores resultados, se recomienda comentar o borrar todas las líneas de código que
estén asociadas a la librería de Networkx y matploidlib.

Nota: Para una mejor visualización ambos algoritmos muestran el grafo en pantalla 
completa.

Si se desea visualizar alguno de los grafos de los casos de prueba, puede utilizar
el programa drawGraph con el siguiente comando:

py drawGraph.py TestCases/test00.txt
