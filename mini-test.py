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
    #Write down to file

    doc = SimpleDocTemplate("./Reporting_"+timestamp+"/reporte_nombres.pdf", pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    #Set title
    story.append(Paragraph("<b>Reporte de deltas " + timestamp + "</b>",  styles['Title']))
    story.append(Spacer(3, 12))
    story.append(Paragraph("A continuación se muestra un perfilado que resume la calidad de los <b>" + qtty_rows + "</b> deltas.", styles['Normal']))
    story.append(Spacer(1, 12))
 

    ten_values_df=df_columns_frequency.head(10)
    plt.figure(figsize=(10, 6))
    x_labels = ten_values_df[columna].astype(str)
    plt.bar(x_labels, ten_values_df['FRECUENCIA'], color='purple')
    
    # Paso 3: Añadir detalles al gráfico
    plt.title(f'Frecuencia de valores en la columna: "{columna}"', fontsize=16)
    plt.xlabel(columna, fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout() # Ajusta el gráfico para evitar que las etiquetas se corten
    
    # Paso 4: Mostrar el gráfico
    plt.show()





#Open data.txt    
df = pd.read_csv("/Users/danito/ProyectoPersonal/Proyectos/Profiling/data.txt", sep='\t', index_col=False)

#Analyzing-profiling and creating report for each column
#For simple columns:
sc=["NOMBRE", "APELLIDO"]
for columna in sc:
    analyzingColumns(df , columna)
    print("Creando el reporte de " + columna)
