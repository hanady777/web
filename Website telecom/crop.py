import pandas as pd


df_tracks1= pd.read_csv(r'tracks.csv', thousands=',').loc[0:250000]
df_tracks2= pd.read_csv(r'tracks.csv', thousands=',').loc[250000:]

df_tracks1.to_csv (r'tracks1.csv', index = False, header=True)
df_tracks2.to_csv (r'tracks2.csv', index = False, header=True)
