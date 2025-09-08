import pandas as pd
import matplotlib.pyplot as plt
#Function 
def analyzingColumns(df, columna):
    #Values and frequency
    df_columns_frequency = (
    df[columna].value_counts(dropna=False)
    .reset_index(name='FRECUENCIA')
    .rename(columns={'index': columna})
    )
    plt.bar(float('FRECUENCIA'), labels=columna, autopct="%1.1f%%")
    plt.title("Frecuencia en gráficos")
    plt.show()
    #print(df_columns_frequency)






#Open data.txt    
df = pd.read_csv("/Users/danito/ProyectoPersonal/Proyectos/Profiling/data.txt", sep='\t', index_col=False)

#Analyzing-profiling and creating report for each column
#For simple columns:
sc=["NOMBRE", "APELLIDO"]
for columna in sc:
    analyzingColumns(df , columna)
    print("Creando el reporte de " + columna)
