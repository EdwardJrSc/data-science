import pandas as pd

# Es creado por columnas, es una tabla
pd.DataFrame({
  'Yes': [1,2],
  'No': [4,5]
})

# Es una sola columna de un DF
pd.Series([212,221,321],
          index = ['Picanto - Octubre',
                   'Picanto - Noviembre',
                   'Picanto - Diciembre'],
          name = 'Kia ultimo semestre')

wine_reviews = pd.read_csv('../../resources/winemag-data_first150k.csv'
                           ,index_col = 0)

# Usamos el .shape para saber de que tamano es el archivo
#print(wine_reviews.shape)

# El head se usa para agarrar las columnas que querramos
#print(wine_reviews.head(10))

# El .review me permite obtener un valor especifico usando el indice
#(wine_reviews.country[4])

# Nos permite obtener el registro completo especificado
#print(wine_reviews.iloc[4])

# Me trae todos las datos de la columna especificada
#print(wine_reviews.iloc[:,0])

# Me trae la cantidad de registros especificados sobre la columna deseada
# NOTA: Trabaja con la posicion del registro en el DataFrame
#print(wine_reviews.iloc[:5,0])

# Nos devuelve las valores de los indices especificados del 1 sin meter el 3
# Me devuelve los valores con los indices especificados en la columna
# NOTA: Trabaja con indice del registro en el DataFrame
#print(wine_reviews.iloc[1:3,0])
#print(wine_reviews.iloc[[0,1,2,3],0])

# Ultimos 5 registros
#print(wine_reviews.iloc[-5:])

# Me trae el valor de la columna del registro indexado
#print(wine_reviews.loc[4,'country'])
#print(wine_reviews.loc[4,['country','points']])

# Me retorna true or false si el vamor es igual al string
#print(wine_reviews.country == 'France')

# Me retorna todos los datos de los registros cuyo country is France
#print(wine_reviews.loc[(wine_reviews.country == 'France') & or | (wine_reviews.points >= 80)])

# Me regresa los registros que cumplen con las criterios
#print(wine_reviews.loc[wine_reviews.country.isin(['Italy', 'France', 'US'])])
#print(wine_reviews.loc[(wine_reviews.country == 'Italy') | (wine_reviews.country == 'France')])

# Me devuelven los registros a partir si el valor es null o fill
#print(wine_reviews.loc[wine_reviews.price.notnull()])
#print(wine_reviews.loc[wine_reviews.price.isnull()])

# .describe me retorna un resumen detallado sobre el atributo que es especificado
#print(wine_reviews.points.describe())
#(wine_reviews.country.describe())

# Me retorna el promedio del atributo en el DF
#print(wine_reviews.points.mean())

# Retorna los valores unicos de los registro que tenga el especificado
#print(wine_reviews.country.unique())

# Me retorna las veces que se repite cada valor
#print(wine_reviews.country.value_counts())