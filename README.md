# Pasar un csv a un archivo xml
## Archivos:
- pizzas_to_xml.py: script de python que contiene el código que transforma el csv a xml
- order_details.csv: fichero que contiene información sobre la cantidad de pizzas ordenadas en un pedido y el identificador del pedido.
- orders.csv: fichero que contiene información sobre las fechas del pedido, al igual que el identificador del pedido.
- pizza_types.csv: fichero que contiene información sobre cada tipo de pizza, como una descripción y los ingredientes que la conforman.
- pizzas.csv: fichero que contiene información sobre el precio de cada pizza en relación a su tamaño.
- 2017_predictions.xml: fichero que contiene la predicción de ingredientes de cada semana para un año.
- 2017_prediction.csv: fichero que contiene las predicciones de ingredientes de "Maven-pizzas-2".
- requirements.txt: fichero que contiene las librerías necesarias y sus versiones para la ejecución del script.

## Descripción del script
En la elaboración del programa se ha seguido una estructura ETL. Los datos que contiene el .xml son las predicciones calculadas en Maven-pizzas-2, además de un informe de los datos contenidos en los ficheros csv (número de NaN, Null, tipo de cada columna, ...). Para la construcción del .xml se ha utilizado la librería lxml. En dicho árbol, se han creado dos ramas principales: una para la predicción que se divide en tantas subramas como semanas de un año, que contienen sus respectivas predicciones; y otra rama que contiene el informe de datos, que tiene a su vez como subrama la el informe de cada fichero csv.

Por último, basta con aplicar una función y tenemos el fichero .xml.
