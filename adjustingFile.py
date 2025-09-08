import pandas as pd
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

timestamp = datetime.now().strftime("%d-%m-%Y")
#read file
df = pd.read_csv("/Users/danito/ProyectoPersonal/Proyectos/Profiling/data.txt", sep='\t', index_col=False)

#how many rows the document has?
qtty_rows=str(len(df)+1)

#Create the pdf "Reporting_date"
doc = SimpleDocTemplate("./Reporting_"+timestamp+"/reporte_nombres.pdf", pagesize=letter)
story = []
styles = getSampleStyleSheet()
#Set title
story.append(Paragraph("<b>Reporte de deltas " + timestamp + "</b>",  styles['Title']))
story.append(Spacer(3, 12))
story.append(Paragraph("A continuación se muestra un perfilado que resume la calidad de los <b>" + qtty_rows + "</b> deltas.", styles['Normal']))
story.append(Spacer(1, 12))
 
#Create graphics and tables for each COLUMN in data.txt file 
def analizingColumns(df , )



#group by name
fq_names= df.groupby("NOMBRE")["NOMBRE"].count().sort_values(ascending=False)
fq_names_df = fq_names.reset_index(name='FRECUENCIA')
df_names=df["NOMBRE"]
null_names_df = pd.DataFrame({
    'NOMBRE' : ["NULL"],
    'FRECUENCIA' : [df_names.isnull().sum()]
})
df_fq_names_final = pd.concat([fq_names_df, null_names_df], ignore_index=True)
df_names_frequency=df_fq_names_final.sort_values(by='FRECUENCIA', ascending=False)
print(df_names_frequency)


#####Crear el docto con esta tabla

story.append(Paragraph("<b>Reporte de Nombres</b>", styles['Title']))
story.append(Spacer(1, 12)) # Espacio en blanco

# Párrafo de texto
story.append(Paragraph("A continuación se muestra una tabla con los nombres y su frecuencia encontrados en el documento de deltas 'data.txt'.", styles['Normal']))
story.append(Spacer(1, 12))

# Convertir el DataFrame a un formato de lista para la tabla
# Primero las cabeceras, luego los datos
data_to_table = [list(df_names_frequency.columns)] + df_names_frequency.values.tolist()
table = Table(data_to_table)

# Aplicar estilo a la tabla
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkslategray),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.azure),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.azure),
    ('GRID', (0, 0), (-1, -1), 1, colors.darkslategray)
]))
story.append(table)

# 4. Construir el PDF
doc.build(story)

print("PDF 'reporte_nombres.pdf' creado exitosamente.")