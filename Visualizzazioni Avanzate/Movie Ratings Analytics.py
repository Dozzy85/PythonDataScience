import pandas as pd
import os

print(os.getcwd())

movies = pd.read_csv('C:\\Users\\Dell\\PycharmProjects\\PythonDataScience\\1.1 Movie-Ratings.csv')

print(len(movies))
print(movies.head())
print(movies.columns)

movies.columns = ['Film', 'Genere', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']
print(movies.head())
print(movies.info())
print(movies.describe())
movies.Film = movies.Film.astype('category')
print(movies.info())
movies.Genere = movies.Genere.astype('category')
movies.Year = movies.Year.astype('category')
print(movies.info())
print(movies.Genere.cat.categories)
print(movies.describe())

#Visualizzazione
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#Jointplots
j = sns.jointplot(data=movies, x='CriticRating', y='AudienceRating')
plt.show()
j = sns.jointplot(data=movies, x='CriticRating', y='AudienceRating', kind='hex')
plt.show()
