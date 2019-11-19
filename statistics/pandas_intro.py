import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as pp

print('--------------------------DataFrame-------------------------')
planets = pd.read_csv('Planets.csv')
print(planets)

print('--------------------------DataFrame with specific columns-------------------------')
print(pd.read_csv('Planets.csv', usecols=[1, 2, 3]))

print('--------------------------Mass Column-------------------------')
print(planets['Mass'])  # or planets.Mass

print('--------------------------1st row only-------------------------')
print(planets.loc[0])
