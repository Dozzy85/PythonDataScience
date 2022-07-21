import inline as inline
import matplotlib
import pandas as pd #miglio package per lavorare con data frames

#Metodo 1: Specificare il percorso completo del file
#Per catturare il contenuto
#In Windows
from pyasn1_modules.rfc2251 import Filter

stats = pd.read_csv('C:\\Users\\Dell\\PycharmProjects\\PythonDataScience\\1.1 DemographicData.csv')

#In Mac stats = pd.read_csv('/Users/Dell/PycharmProjects/PythonDataScience/1.1 DemographicData.csv')

print(stats)

#Metodo 2: Cambiando directory di lavoro
import  os

print(os.getcwd())

#Windows
os.chdir('C:\\Users\\Dell\\PycharmProjects\\PythonDataScience')

#In Mac os.chdir('/Users/Dell/PycharmProjects/PythonDataScience')

stats2 = pd.read_csv('1.1 DemographicData.csv')

print(os.getcwd())
print(stats2)

#Esplorare i dati

#Numero di righe
print(len(stats))

#Vedere le colonne
print(stats.columns)

#Il numero di colonne
print(len(stats.columns))

#Vedere le righe più in alto
print(stats.head()) #oppure per specificare il numero di righe da vedere stats.head(6)

#Vedere le righe in fondo
print(stats.tail()) #oppure per specificare il numero di righe da vedere stats.tail(6)

#Leggere informazioni sulle colonne
print(stats.info())

#Vedere le statistiche delle colonne
print(stats.describe())
print(stats.describe().transpose())

#Rinominare le colonne del Data Frame
print(stats.columns)
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']
print(stats.head())

#Creare dei sotto insiemi di Data Frame
#Righe
#Colonne
#RIghe e Colonne
#Parte 1: Sotto insieme delle righe
print(stats[21:26])

#Esercizio: Rovesciare il Data Frame
print(stats[ : : -1])

#Esercizio: Ogni 20 righe prendiamo il record
print(stats[ : : 20])

#Parte 2: Sotto insieme delle colonne
print(stats['CountryName'].head())

print(stats[['CountryName', 'BirthRate']].head())

print(stats[['BirthRate', 'CountryName']].head())

#Accesso Veloce: rihciede che il nome sia una sola parola
print(stats.BirthRate.head())

#Parte 3: Sotto insieme di righe e colonne
df1 = stats[4:8][['CountryName', 'BirthRate']]
print(df1)

#Operazioni basi con i dataframe di matematica
result = stats.BirthRate*stats.InternetUsers
print(result.head())

#Aggiungere una colonna
stats['MyCalc'] = stats.BirthRate*stats.InternetUsers
print(stats.head())

#Rimuovere una colonna
print(stats.head())
stats = stats.drop('MyCalc', 1)
print(stats.head())

#Filtrare i Dataframes
#Filtrare le righe
Filter = stats.InternetUsers < 2
print(Filter)
print(stats[Filter])

Filter2 = stats.BirthRate > 40
print(stats[Filter2])

stats[Filter & Filter2]
print(stats[Filter & Filter2])

stats[stats.IncomeGroup == 'High income']
print(stats[stats.IncomeGroup == 'High income'])

#Come prendere tutte le categorie ma in maniera univoca
stats.IncomeGroup.unique()
print(stats.IncomeGroup.unique())

#Esercizio filtrare tutto per il paese Malta
print(stats.CountryName.unique())
Filter3 = stats[stats.CountryName == 'Malta']
print(Filter3)

#Accesso individuale ad un elemento
#.at per le etiohette, importante anche i valori integer sono trattati come etichette
#.iat solo per posizioni integer
stats.iat[3,4]
print(stats.iat[3,4])
stats.iat[0,1]
print(stats.iat[0,1])

stats.at[2,'BirthRate']
print(stats.at[2,'BirthRate'])

sub10 = stats[::10]
print(sub10)
sub10.iat[10,0]
print(sub10.iat[10,0])
sub10.at[10,'CountryName']
print(sub10.at[10,'CountryName'])

#Introduzione a Seaborn package per la visualizzazione
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['figure.figsize'] = 8,4
import warnings
warnings.filterwarnings('ignore')

#Distribuzione
vis1 = sns.displot(stats['InternetUsers'])
vis1 = sns.distplot(stats["InternetUsers"], bins=30)

#Bosxplots
vis2 = sns.boxplot(data=stats, x='InternetUsers', y='BirthRate')
