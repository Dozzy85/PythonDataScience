import pandas as pd #miglio package per lavorare con data frames

#Metodo 1: Specificare il percorso completo del file
#Per catturare il contenuto
#In Windows
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

