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