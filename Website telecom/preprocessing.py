import pandas as pd
import numpy as np

def convert(amount,currency):
  if (currency=='NAN'):
    return amount*(-1)
  elif (currency=='USD'):
    return amount
  elif (currency=='ITL'):
    return amount*0.000612862
  elif (currency=='ROL'):
    return amount*0.24
  elif (currency=='SEK'):
    return amount*0.12
  elif (currency=='FRF'):
    return amount*0.180904
  elif (currency=='NOK'):
    return amount*0.12
  elif (currency=='GBP'):
    return amount*1.38
  elif (currency=='DEM'):
    return amount*0.61
  elif (currency=='PTE'):
    return amount*0.00591818
  elif (currency=='FIM'):
    return amount*0.199512
  elif (currency=='CAD'):
    return amount*0.81
  elif (currency=='INR'):
    return amount*0.013
  elif (currency=='CHF'):
    return amount*1.08
  elif (currency=='ESP'):
    return amount*0.0071168154
  elif (currency=='JPY'):
    return amount*0.0090289296
  elif (currency=='DKK'):
    return amount*0.15924798
  elif (currency=='NLG'):
    return amount*0.5373718
  elif (currency=='PLN'):
    return amount*0.26300904
  elif (currency=='RUR'):
    return amount*0.55865922
  elif (currency=='AUD'):
    return amount*0.75768154
  elif (currency=='KRW'):
    return amount*0.0008818992
  elif (currency=='BEF'):
    return amount*0.029352519
  elif (currency=='XAU'):
    return amount*1807.086
  elif (currency=='HKD'):
    return amount*0.12875892
  elif (currency=='NZD'):
    return amount*0.70857269
  elif (currency=='CNY'):
    return amount*0.15466283
  elif (currency=='EUR'):
    return amount*1.1841424
  elif (currency=='PYG'):
    return amount*0.00014717065
  elif (currency=='ISK'):
    return amount*0.0080491345
  elif (currency=='IEP'):
    return amount*1.503564
  elif (currency=='TRL'):
    return amount*0.00000011531695 
  elif (currency=='HRK'):
    return amount*0.15814896
  elif (currency=='SIT'):
    return amount*0.0049409511
  elif (currency=='PHP'):
    return amount*0.020162609
  elif (currency=='HUF'):
    return amount*0.0033508116
  elif (currency=='DOP'):
    return amount*0.01759143
  elif (currency=='JMD'):
    return amount*0.0066731323
  elif (currency=='CZK'):
    return amount*0.04622792
  elif (currency=='SGD'):
    return amount*0.74349639
  elif (currency=='BRL'):
    return amount*0.1963829
  elif (currency=='BDT'):
    return amount*0.011808504
  elif (currency=='ATS'):
    return amount*0.086045077
  elif (currency=='BND'):
    return amount*0.74349344
  elif (currency=='EGP'):
    return amount*0.06375525
  elif (currency=='THB'):
    return amount*0.031056313
  elif (currency=='GRD'):
    return amount*0.0034747334
  elif (currency=='ZAR'):
    return amount*0.070221751
  elif (currency=='NPR'):
    return amount*0.0083463958
  elif (currency=='IDR'):
    return amount*0.000069065533
  elif (currency=='PKR'):
    return amount*0.0062853033
  elif (currency=='MXN'):
    return amount*0.050412501
  elif (currency=='BGL'):
    return amount*0.61
  elif (currency=='EEK'):
    return amount*0.075669051
  elif (currency=='YUM'):
    return amount*1.5
  elif (currency=='MYR'):
    return amount*0.2406386
  elif (currency=='IRR'):
    return amount*0.00002379518
  elif (currency=='CLP'):
    return amount*0.001357972
  elif (currency=='SKK'):
    return amount*0.039302392
  elif (currency=='LTL'):
    return amount*0.34290923
  elif (currency=='TWD'):
    return amount*0.035761891
  elif (currency=='MTL'):
    return amount*2.7579711
  elif (currency=='LVL'):
    return amount*1.6846855
  elif (currency=='COP'):
    return amount*0.00026718998
  elif (currency=='ARS'):
    return amount*0.010428046
  elif (currency=='UAH'):
    return amount*0.036664588
  elif (currency=='RON'):
    return amount*0.24032882
  elif (currency=='ALL'):
    return amount*0.009681646
  elif (currency=='NGN'):
    return amount*0.0024330767
  elif (currency=='ILS'):
    return amount*0.30642726
  elif (currency=='VEB'):
    return amount*0.0000000000000030681445
  elif (currency=='VND'):
    return amount*0.000043396416
  elif (currency=='TTD'):
    return amount*0.1474552
  elif (currency=='JOD'):
    return amount*1.4104372
  elif (currency=='LKR'):
    return amount*0.005012586
  elif (currency=='GEL'):
    return amount*0.31797029
  elif (currency=='MNT'):
    return amount*0.00034997449
  elif (currency=='AZM'):
    return amount*0.00011771768
  elif (currency=='AMD'):
    return amount*0.0020206044
  elif (currency=='AED'):
    return amount*0.27229408
  else:
    return amount*(-2)

df_movies = pd.read_csv(r'IMDb movies.csv', thousands=',')
#df_names1= pd.read_csv(r'IMDb names1.csv', thousands=',').loc[:157200].reset_index()
df_names1= pd.read_csv(r'IMDb names1.csv', thousands=',').loc[157300:].reset_index()
df_names2= pd.read_csv(r'IMDb names2.csv', thousands=',').reset_index()
#df_names3= pd.read_csv(r'IMDb names1.csv', thousands=',').loc[0:15700].reset_index()
df_names=pd.concat([df_names1,df_names2],axis=0)
df_names.reset_index()
df_names=df_names.drop(columns=['birth_details','death_details'])
df_ratings= pd.read_csv(r'IMDb ratings.csv', thousands=',')
df_ratings=df_ratings.drop(columns=['votes_1','votes_2','votes_3','votes_4','votes_5','votes_10', 'votes_9',
       'votes_8', 'votes_7', 'votes_6'])
df_title_principals= pd.read_csv(r'IMDb title_principals.csv', thousands=',')

df_names['year of birth']=pd.to_numeric(df_names['date_of_birth'].fillna('9999').apply(lambda x: str(x)[:4] if (str(x)[0]=='1' or str(x)[0]=='2') else '9999')).replace(9999, np.nan)
df_names['year of death']=pd.to_numeric(df_names['date_of_death'].fillna('9999').apply(lambda x: str(x)[:4] if ((str(x)[0]=='1' or str(x)[0]=='2') and str(x)[2]!=' ') else '9999')).replace(9999, np.nan)
df_names['country of birth']=df_names['place_of_birth'].fillna(' ').apply(lambda x: x.split(",")[-1] if len(x)>2 else ' ').replace(' ', np.nan)
df_names['country of death']=df_names['place_of_death'].fillna(' ').apply(lambda x: x.split(",")[-1] if len(x)>2 else ' ').replace(' ', np.nan)
df_names['first spouse']=df_names['spouses_string'].fillna(' ').apply(lambda x: x.split("(")[0] if len(x)>2 else ' ').replace(' ', np.nan)
df_names=df_names.drop(columns=['bio','date_of_birth','date_of_death','place_of_birth','spouses_string','place_of_death'])

money_list=['budget','usa_gross_income','worlwide_gross_income']
for c in money_list:
  df_movies[c]=df_movies[c].fillna('NAN 1').str.replace('$', 'USD')
  df_movies[c+' Currency']=df_movies[c].apply(lambda x: x[:3])
  df_movies[c+' Amount']=pd.to_numeric(df_movies[c].apply(lambda x: x[4:]))
  df_movies[c+' USD'] = df_movies.apply( lambda x: convert(x[c+' Amount'],str(x[c+' Currency']) ), axis = 1)
  df_movies=df_movies.drop(columns=[c,c+' Amount'])
  df_movies[c+' Currency']=df_movies[c+' Currency'].replace('NAN', np.nan)
  df_movies[c+' USD']=df_movies[c+' USD'].replace('NAN', np.nan)

df_movies_na=df_movies.isna().sum().tolist()
order_movies=sorted(range(len(df_movies_na)), key=lambda k: df_movies_na[k])
cols_movies = df_movies.columns.tolist()
cols_movies = [cols_movies[i] for i in order_movies]
df_movies=df_movies[cols_movies]

df_names_na=df_names.isna().sum().tolist()
order_names=sorted(range(len(df_names_na)), key=lambda k: df_names_na[k])
cols_names = df_names.columns.tolist()
cols_names = [cols_names[i] for i in order_names]
df_names=df_names[cols_names]

df_ratings_na=df_ratings.isna().sum().tolist()
order_ratings=sorted(range(len(df_ratings_na)), key=lambda k: df_ratings_na[k])
cols_ratings = df_ratings.columns.tolist()
cols_ratings = [cols_ratings[i] for i in order_ratings]
df_ratings=df_ratings[cols_ratings]

df_title_principals_na=df_title_principals.isna().sum().tolist()
order_title_principals=sorted(range(len(df_title_principals_na)), key=lambda k: df_title_principals_na[k])
cols_title_principals = df_title_principals.columns.tolist()
cols_title_principals = [cols_title_principals[i] for i in order_title_principals]
df_title_principals=df_title_principals[cols_title_principals]

#Pour voir le lieu des Nan

# %matplotlib inline
# msno.matrix(df_movies)
# msno.matrix(df_names)
# msno.matrix(df_ratings)
# msno.matrix(df_title_principals)

df_wo_actors_details = pd.merge(df_movies, df_ratings, on='imdb_title_id',  how='outer')

df_wo_actors_details=df_wo_actors_details.rename(columns={'year': 'year of release' })
df_names=df_names.rename(columns={'spouses': 'number of spouses', 'divorces' : 'number of divorces','spouses_with_children':'number of spouses with children','children':'number of children'})


column_10=['avg_vote','weighted_average_vote','mean_vote','median_vote','allgenders_18age_avg_vote','allgenders_30age_avg_vote','allgenders_45age_avg_vote','males_allages_avg_vote','males_allages_votes','males_0age_avg_vote','males_18age_avg_vote','males_30age_avg_vote','males_45age_avg_vote','females_allages_avg_vote','females_0age_avg_vote','females_18age_avg_vote','females_30age_avg_vote','females_45age_avg_vote','top1000_voters_rating','us_voters_rating','non_us_voters_rating']

#On multiplie par 10 les colonnes avec exactitude d'ordre **0.1**



df_wo_actors_details[column_10]=df_wo_actors_details[column_10]*10

output= pd.merge(df_wo_actors_details, df_title_principals, on='imdb_title_id',  how='outer')

df= pd.merge(output, df_names, on='imdb_name_id',  how='outer')

df_wo_actors_details['index']=[i for i in range(len(df_wo_actors_details))]
df_names['index']=[i for i in range(len(df_names))]

s='genre'

df_wo_actors_details

#df_wo_actors_details['year'] = df_wo_actors_details.apply (lambda row: int(row['year']), axis=1)

#non_numerical_col=df_wo_actors_details.select_dtypes(exclude='number').columns

# A REVOIR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# non_numerical_col=['genre','country','language']

# for s in non_numerical_col:
#   L=df_wo_actors_details[s].value_counts()
#   df_wo_actors_details[s+'_numerical']=df_wo_actors_details.apply (lambda row: int(L.index.tolist().index(row[s])) if row[s]==row[s] else len(L), axis=1)

#Création des colonnes rangs pour les colonnes numériques

numerical_col=df_wo_actors_details.select_dtypes(include='number').columns

numerical_col

numerical_col=df_wo_actors_details.select_dtypes(include='number').columns
for c in numerical_col:
  df_wo_actors_details['rank_'+c]=df_wo_actors_details[c].rank()
  inv=df_wo_actors_details[c]*(-1)
  df_wo_actors_details['invrank_'+c]=inv.rank()

numerical_col_actors=df_names.select_dtypes(include='number').columns
for c in numerical_col_actors:
  df_names['rank_'+c]=df_names[c].rank()
  inv=df_names[c]*(-1)
  df_names['invrank_'+c]=inv.rank()

df_wo_actors_details.sort_values("index", inplace = True)


df_wo_actors_details_na=df_wo_actors_details.isna().sum().tolist()
order_wo_actors_details=sorted(range(len(df_wo_actors_details_na)), key=lambda k: df_wo_actors_details_na[k])
cols_wo_actors_details = df_wo_actors_details.columns.tolist()
cols_wo_actors_details = [cols_wo_actors_details[i] for i in order_wo_actors_details]
df_wo_actors_details=df_wo_actors_details[cols_wo_actors_details]

df_names_na=df_names.isna().sum().tolist()
order_names=sorted(range(len(df_names_na)), key=lambda k: df_names_na[k])
cols_names = df_names.columns.tolist()
cols_names = [cols_names[i] for i in order_names]
df_names=df_names[cols_names]

df_names_names=[df_names['name'].loc[i] for i in range(len(df_names))]

# df_names.apply (lambda row: int(number_hits(row['name'])), axis=1)

L_genre=df_wo_actors_details['genre'].value_counts()

df_wo_actors_details['genre_numerical']=df_wo_actors_details.apply(lambda row: L_genre.index.tolist().index(row['genre']) if row['genre']==row['genre'] else len(L_genre), axis=1)



df_tracks1 = pd.read_csv(r'tracks1.csv', thousands=',')
df_tracks2 = pd.read_csv(r'tracks2.csv', thousands=',')
df_tracks=pd.concat([df_tracks1,df_tracks2],axis=0)
df_tracks.reset_index()
df_artists = pd.read_csv(r'artists.csv', thousands=',')
df_tracks['index']=[i for i in range(len(df_tracks))]
df_artists['index']=[i for i in range(len(df_artists))]

df_tracks['id_artists']=df_tracks['id_artists'].fillna('   ').apply(lambda x: x[2:-2]).replace('   ', np.nan)
df_tracks['artists']=df_tracks['artists'].fillna('   ').apply(lambda x: x[2:-2]).replace('   ', np.nan)
df_tracks['year of release']=pd.to_numeric(df_tracks['release_date'].fillna('9999').apply(lambda x: str(x)[:4] if (str(x)[0]=='1' or str(x)[0]=='2') else '9999')).replace(9999, np.nan)
df_tracks=df_tracks.drop(columns=['release_date'])

numerical_col=df_tracks.select_dtypes(include='number').columns
for c in numerical_col:
  df_tracks['rank_'+c]=df_tracks[c].rank()
  inv=df_tracks[c]*(-1)
  df_tracks['invrank_'+c]=inv.rank()
numerical_col_artists=df_artists.select_dtypes(include='number').columns
for c in numerical_col_artists:
  df_artists['rank_'+c]=df_artists[c].rank()
  inv=df_artists[c]*(-1)
  df_artists['invrank_'+c]=inv.rank()

df_artists_na=df_artists.isna().sum().tolist()
order_artists=sorted(range(len(df_artists_na)), key=lambda k: df_artists_na[k])
cols_artists = df_artists.columns.tolist()
cols_artists = [cols_artists[i] for i in order_artists]
df_artists=df_artists[cols_artists]

df_tracks_na=df_tracks.isna().sum().tolist()
order_tracks=sorted(range(len(df_tracks_na)), key=lambda k: df_tracks_na[k])
cols_tracks = df_tracks.columns.tolist()
cols_tracks = [cols_tracks[i] for i in order_tracks]
df_tracks=df_tracks[cols_tracks]

df_wo_actors_details['title']=df_wo_actors_details['title'].str.lower()
df_wo_actors_details['original_title']=df_wo_actors_details['original_title'].str.lower()
df_wo_actors_details['genre']=df_wo_actors_details['genre'].str.lower()
df_wo_actors_details['production_company']=df_wo_actors_details['production_company'].str.lower()
df_names['name']=df_names['name'].str.lower()
df_names['birth_name']=df_names['birth_name'].str.lower()
df_names['name']=df_names['name'].str.lower()
df_names['first spouse']=df_names['first spouse'].str.lower()
df_tracks['name']=df_tracks['name'].str.lower()
df_tracks['artists']=df_tracks['artists'].str.lower()

#df_wo_actors_details=df_wo_actors_details.rename(columns={'year': 'year of release', 'original_title'='original title', 'date_published'='date published','avg_vote'='average vote'  })
df_wo_actors_details=df_wo_actors_details.drop(columns={'date_published','year of release'})
# df_tracks=df_tracks.drop(columns='index')
# df_names=df_names.drop(columns='index')
# df_artists=df_artists.drop(columns='index')
