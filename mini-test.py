import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

timestamp = datetime.now().strftime("%d-%m-%Y")

def defTableStyle(table):
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkslategray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.azure),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.azure),
        ('GRID', (0, 0), (-1, -1), 1, colors.darkslategray)
    ]))
    return table

def defPieStyle(table, columna):
    plt.pie(table['FRECUENCIA'], 
            labels=table[columna], # Etiquetas para cada porción
            autopct='%1.1f%%', # Formato para mostrar el porcentaje
            startangle=90)
        # Añadir un título y asegurar un aspecto circular
    plt.title(f'Frecuencia de valores en la columna: "{columna}"', fontsize=16)
    plt.axis('equal')  # Asegura que el pastel sea un círculo        
    plt.tight_layout()
    plt.savefig('grafico_' + columna + '.png')
    plt.close()
    

#Function for NAMES and LASTNAMES
# def analyzingColumns(df, columna):
#     #Values and frequency
#     df_columns_frequency = (
#     df[columna].value_counts(dropna=False)
#     .reset_index(name='FRECUENCIA')
#     .rename(columns={'index': columna})
#     )
#     #Write down to file
#     #Set the title
#     story.append(Paragraph("<b>Reporte de " + columna + "</b>", styles['Title']))
#     story.append(Spacer(1, 12)) # Espacio en blanco
#     # Paragraph
#     story.append(Paragraph("A continuación se muestra una tabla con los valores y su frecuencia encontrados en el documento de deltas 'data.txt'.", styles['Normal']))
#     story.append(Spacer(1, 12))
#     # Transform dataframe into a list for table 
#     # First, titles, then data
#     data_to_table = [list(df_columns_frequency.columns)] + df_columns_frequency.values.tolist()
#     table = Table(data_to_table)
#     # Table style
#     defTableStyle(table)
#     story.append(table)
#     story.append(Spacer(1, 12))

#     #Build graphics
#     ten_values_df=df_columns_frequency.head(10)
#     plt.figure(figsize=(10, 6))
#     x_labels = ten_values_df[columna].astype(str)
#     plt.bar(x_labels, ten_values_df['FRECUENCIA'], color='purple')
#     #Graphic style
#     plt.title(f'Frecuencia de valores en la columna: "{columna}"', fontsize=16)
#     plt.xlabel(columna, fontsize=12)
#     plt.ylabel('Frecuencia', fontsize=12)
#     plt.xticks(rotation=45, ha='right')
#     plt.tight_layout() # Adjust to see everything in labels
#     # Write the graphic down
#     plt.savefig('grafico_' + columna + '.png')
#     plt.close()
#     story.append(Paragraph("A continuación se muestra una gráfica con la distribución de los 10 valores más frecuentes.", styles['Normal']))
#     story.append(Spacer(1, 12))
#     img = Image("grafico_"+columna+".png", width=400, height=300)
#     story.append(img)
#     story.append(Spacer(1, 12))


def reviewColumns(df , columna):
    #Write down to file
    #Set the title
    story.append(Paragraph("<b>Reporte de " + columna + "</b>", styles['Title']))
    story.append(Spacer(1, 12)) # Espacio en blanco
    # Paragraph
    story.append(Paragraph("A continuación se muestra un resumen de la columna, con material de apoyo visual.", styles['Normal']))
    story.append(Spacer(1, 12))

    #How is distributed the lenght 
    df['LONGITUD'] = df [columna].str.len()
    df_longitud_frequency = (
    df['LONGITUD'].value_counts(dropna=False)
    .reset_index(name='FRECUENCIA')
    .rename(columns={'index': columna})
    )
    #TABLE
    #Transform dataframe into a list for table 
    # First, titles, then data
    data_to_table = [list(df_longitud_frequency.columns)] + df_longitud_frequency.values.tolist()
    table = Table(data_to_table)
    defTableStyle(table)
    story.append(table)
    story.append(Spacer(1, 12))

    #GRAPHIC
    defPieStyle(df_longitud_frequency, columna)
    # Write the graphic down
    story.append(Paragraph("A continuación se muestra una gráfica con la distribución de la longitud de los valores en la columna.", styles['Normal']))
    story.append(Spacer(1, 12))
    img = Image("grafico_"+columna+".png", width=400, height=300)
    story.append(img)
    story.append(Spacer(1, 12))

    #It's a valid column?
    # df['cumple_patron'] = df[columna].str.match(regex_curp) 
    # df_patron_frequency = (
    # df['cumple_patron'].value_counts(dropna=False)
    # .reset_index(name='FRECUENCIA')
    # .rename(columns={'index': columna})
    # )
    # #TABLE
    # data_to_table = [list(df_patron_frequency.columns)] + df_patron_frequency.values.tolist()
    # table = Table(data_to_table)
    # story.append(table)
    # story.append(Spacer(1, 12))
    # #GRAPHIC
    # plt.pie(df_longitud_frequency['FRECUENCIA'], 
    #         labels=df_longitud_frequency[columna], # Etiquetas para cada porción
    #         autopct='%1.1f%%', # Formato para mostrar el porcentaje
    #         startangle=90)
    #     # Añadir un título y asegurar un aspecto circular
    # plt.title(f'Frecuencia de longitud en la columna: "{columna}"', fontsize=16)
    # plt.axis('equal')  # Asegura que el pastel sea un círculo        plt.tight_layout()
    # # Write the graphic down
    # plt.savefig('grafico_' + columna + '.png')
    # plt.close()
    # story.append(Paragraph("A continuación se muestra una gráfica con la distribución de la longitud de los valores en la columna.", styles['Normal']))
    # story.append(Spacer(1, 12))
    # img = Image("grafico_"+columna+".png", width=400, height=300)
    # story.append(img)
    # story.append(Spacer(1, 12))

    # #Are there any duplicated?
    # mascara_duplicados = df.duplicated(subset=[columna], keep=False).sum()
    # if mascara_duplicados!=0:
    #     smt= df.duplicated(subset=[columna], keep=False)
    #     registros_duplicados = df[smt].sort_values(columna, ascending=False)
    #     #TABLE
    #     data_to_table = [list(registros_duplicados.columns)] + registros_duplicados.values.tolist()
    #     table = Table(data_to_table)
    #     story.append(table)
    #     story.append(Spacer(1, 12))
        
    # else:
    #     print("No duplicated")
        



#Open data.txt    
df = pd.read_csv("/Users/danito/ProyectoPersonal/Proyectos/Profiling/data.txt", sep='\t', index_col=False)

qtty_rows=str(len(df)+1)#how many deltas
regex_curp=r'^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|MT|OC|PL|QT|QR|SP|SL|SR|TC|TL|TS|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d]\d)$'

#Create file
doc = SimpleDocTemplate("./Reporting_"+timestamp+"/reporte_data.pdf", pagesize=letter)    
story = []
styles = getSampleStyleSheet()
#Set title into the file
story.append(Paragraph("<b>Reporte de deltas " + timestamp + "</b>",  styles['Title']))
story.append(Spacer(3, 12))
story.append(Paragraph("A continuación se muestra un perfilado que resume la calidad de los <b>" + qtty_rows + "</b> deltas.", styles['Normal']))
story.append(Spacer(1, 12))

#Analyzing-profiling and creating report for each column
#For simple columns:
# sc=["NOMBRE", "APELLIDO", "GENERO"]
# for columna in sc:
#     analyzingColumns(df , columna)
#     print("Creando el reporte de " + columna)

#For structure review columns:
src=["CURP"]
for columna in src:
    reviewColumns(df , columna)
    print("Creando el reporte de " + columna)
doc.build(story)