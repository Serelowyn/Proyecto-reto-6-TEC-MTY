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

"""2. Se concatenan los 4 df's"""
df_full = pd.concat([df_test, df_test2, df_train2, df_train], ignore_index=True)