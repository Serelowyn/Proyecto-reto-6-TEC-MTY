# ------------- Importaciones

import pandas as pd

"""para el drive"""
# from google.colab import drive
# drive.mount("/content/gdrive")

# ------------- Fin de las importaciones

"""1. Se cargan los archivos csv, se cambian datos en el drive para que funcione"""
df_test = pd.read_csv(r"Test.csv")
df_test2 = pd.read_csv(r"test2.csv")
df_train2 = pd.read_csv(r"Train2.csv")
df_train = pd.read_csv(r"Train.csv")

"""se identifican los dataframe que posiblemente sean los causantes del problema del commit pasado"""
print(df_test2.columns)
print(df_train2.columns)

"""aqui eliminamos los espacios de todas las colunmnas"""
df_test2.columns = df_test2.columns.str.strip()
df_train2.columns = df_train2.columns.str.strip()

"""verificamos resultados"""
print(df_test2.columns.tolist())
print(df_train2.columns.tolist())

"""2. Se concatenan los 4 df's"""
df_full = pd.concat([df_test, df_test2, df_train2, df_train], ignore_index=True)

"""3. Aqui movemos las dos columnas que se indica en las instrucciones"""
df_full["Computer_OS"] = df_full["Computer_OS"].fillna("no registrado")
df_full["Mobile_OS"] = df_full["Mobile_OS"].fillna("no registrado")

"""4. calculamos los promedios de uso de cada sistema operativo"""
porcentajes_os = df_full["Computer_OS"].value_counts(normalize=True) * 100
print(porcentajes_os)
"""comprobamos que la suma de todo de 100"""
print(porcentajes_os.sum())

"""calculamos los promedios de uso de sistemas operativos de celular"""
porcentaje_cel = df_full["Mobile_OS"].value_counts(normalize=True) * 100
print(porcentaje_cel)

"""5. sacamos la edad promedio de la gente que usa el OS"""
promedio_edad_os = df_full.groupby("Computer_OS")["Age"].mean()
print(promedio_edad_os)
df_full.columns.tolist()
df_full.groupby("Computer_OS")["Age"].count()
df_full.groupby("Mobile_OS")["Age"].count()