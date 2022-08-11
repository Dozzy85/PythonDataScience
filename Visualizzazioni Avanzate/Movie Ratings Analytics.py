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

#Istogrammi
m1 = sns.displot(movies.AudienceRating, bins=15)
plt.show()
m2 = sns.displot(movies.CriticRating, bins=15)
plt.show()
n1 = plt.hist(movies.AudienceRating, bins=15)
plt.show()
n2 = plt.hist(movies.CriticRating, bins=15)
plt.show()

#Grafici a barre impilate
plt.hist([movies[movies.Genere == 'Drama'].BudgetMillions, movies[movies.Genere == 'Action'].BudgetMillions, movies[movies.Genere == 'Thriller'].BudgetMillions], bins=15, stacked=True)
plt.show()

for gen in movies.Genere.cat.categories:
    print(gen)

list1 = list()
mylabels = list()
for gen in movies.Genere.cat.categories:
    list1.append(movies[movies.Genere == gen].BudgetMillions)
    mylabels.append(gen)


h = plt.hist(list1, bins=30, stacked=True, rwidth=1, label=mylabels)
plt.legend()
plt.show()
