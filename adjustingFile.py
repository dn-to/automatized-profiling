import pandas as pd

df = pd.read_csv("/Users/danito/ProyectoPersonal/Proyectos/Profiling/data.txt", sep='\t', index_col=False)
#print(df)

#how many rows the document has
#print(len(df) + 1 )

#group by name
fq_names= df.groupby("NOMBRE")["NOMBRE"].count().sort_values(ascending=False)
fq_names_df = fq_names.reset_index(name='Frecuencia')
df_names=df["NOMBRE"]
null_names_df = pd.DataFrame({
    'NOMBRE' : ["NULL"],
    'Frecuencia' : [df_names.isnull().sum()]
})
df_fq_names_final = pd.concat([fq_names_df, null_names_df], ignore_index=True)

df_names_freqcuency=df_fq_names_final.sort_values(by='Frecuencia', ascending=False)
df_final=df_names_freqcuency.to_html
print(df_final)
