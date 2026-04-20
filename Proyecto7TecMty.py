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
for df in [df_test, df_test2, df_train2, df_train]:
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

"""verificamos resultados"""
print(df_test2.columns.tolist())
print(df_train2.columns.tolist())

"""2. Se concatenan los 4 df's"""
df_full = pd.concat([df_train, df_train2, df_test, df_test2], axis=0, ignore_index=True)
df_full = df_full.groupby("employee_id").first().reset_index()

"""3. Aqui movemos las dos columnas que se indica en las instrucciones"""
df_full["computer_os"] = df_full["computer_os"].fillna("no registrado")
df_full["mobile_os"] = df_full["mobile_os"].fillna("no registrado")

"""4. calculamos los promedios de uso de cada sistema operativo"""
porcentajes_os = df_full["computer_os"].value_counts(normalize=True) * 100
print(porcentajes_os)
"""comprobamos que la suma de todo de 100"""
print(porcentajes_os.sum())

"""calculamos los promedios de uso de sistemas operativos de celular"""
porcentaje_cel = df_full["mobile_os"].value_counts(normalize=True) * 100
print(porcentaje_cel)

"""5. sacamos la edad promedio de la gente que usa el OS"""
promedio_edad_os = df_full.groupby("computer_os")["age"].mean()
print(promedio_edad_os)

"""6. sacamos el nivel educativio promedio de la gente que usa el OSde esccritorio"""
educacion_os = df_full.groupby("computer_os")["education_level"].mean()
print(educacion_os)

"""7. ticket sgenerados por cada OS de esccritorio"""
tickets_generados = df_full.groupby("computer_os")["computer_tickets"].sum()
print(tickets_generados)

with pd.ExcelWriter("resultados_consultas.xlsx", engine="xlsxwriter") as writer:
    porcentajes_os.to_excel(writer, sheet_name="porcentaje_uso_OS")
    porcentaje_cel.to_excel(writer, sheet_name="porcentaje_uso_CEL")
    promedio_edad_os.to_excel(writer, sheet_name="edad computer_OS")
    educacion_os.to_excel(writer, sheet_name="education_level_OS")
    tickets_generados.to_excel(writer, sheet_name="computer_tickets_OS")