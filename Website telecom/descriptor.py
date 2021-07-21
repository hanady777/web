import numpy as np
import pandas as pd

def contrast(dataframe_0,entity_row, column_considered, rows_considered ):
  dataframe=dataframe_0[column_considered]
  a=((dataframe.loc[entity_row]-dataframe.loc[rows_considered].mean())/dataframe.loc[rows_considered].std()).abs().dropna()
  col=dataframe.columns[[i  for i in range(len(a)) if a[i]==a.max(axis=0) ]]
  return col

def isinbase(entity,df_wo_actors_details,df_names,df_tracks,df_artists):
  desc=Descriptor(entity,df_wo_actors_details,df_names,df_tracks,df_artists)
  liste=desc.find_row()
  if (len(liste)==0):
    return False
  else:
    return True


class Descriptor:

# to initialize we need the received query and all the data bases we need
  def __init__(self,query,df_wo_actors_details,df_names,df_tracks,df_artists,context=[],max_complexity=10,min_length_description=4):
    self.query=query.lower()
    self.moviedb=df_wo_actors_details
    self.castdb=df_names
    self.tracksdb=df_tracks
    self.artistsdb=df_artists
    self.dblist=[self.moviedb,self.castdb,self.tracksdb,self.artistsdb]
    self.context=context
    self.max_complexity=max_complexity
    self.min_length_description=min_length_description
    self.dblist_names=['movie','cast','track','artist']

#find row and data base number in which our query appear
  def find_row(self):
    a=[]
    name_list=['title','name','name','name']
    id_list=['imdb_title_id','imdb_name_id','id','id']
    for i in range(len(self.dblist)):
      a.append(self.dblist[i][self.dblist[i][name_list[i]]==self.query]['index'].tolist())
    b=[(a[i][j],i,self.query) for i in range(len(a)) for j in range(len(a[i]))]
    return b


  def find_row_item(self,item):
    a=[]
    name_list=['title','name','name','name']
    id_list=['imdb_title_id','imdb_name_id','id','id']
    for i in range(len(self.dblist)):
      a.append(self.dblist[i][self.dblist[i][name_list[i]]==item]['index'].tolist())
    b=[(a[i][j],i,item) for i in range(len(a)) for j in range(len(a[i]))]
    return b
  
  
  def complexity_row_column(self,query,index_of_db,entity_row,total_complexity=0,rows_considered=[],columns_considered=[],context=[],description='',initialisation=False, max_complexity=0, min_length_description=0, max_length_description=0):
    df=self.dblist[index_of_db]
    # on a deja entierement decrit l'objet mais on donne plus de phrases
    l=df.columns.tolist()

    all_columns=[l[i] for i in range(len(l)) if not (l[i][0:4]=='rank' or l[i][0:7]=='invrank')]

    if (initialisation==False):
      description=query+': '
      columns_considered=all_columns
      rows_considered=np.arange(len(df)).tolist()
      max_complexity=self.max_complexity
      min_length_description=self.min_length_description
      max_length_description=self.min_length_description+4
    
    if (len(rows_considered)==1 and min_length_description>0 ):
      rows_considered=np.arange(len(df)).tolist()
      description+='|'
      print("min_length_description",min_length_description)

    else:
      if (len(rows_considered)==1):
        return (description,total_complexity)


    if (max_length_description<=0):
      return (description,total_complexity)



    all_numerical_columns = df.select_dtypes(include='number').columns.to_list()

    # Know which columns to use and their type
    numerical_columns_considered=[c for c in columns_considered if(c in all_numerical_columns and 'index' not in c)]
    non_numerical_columns_considered=[c for c in columns_considered if (c not in all_numerical_columns and 'id' not in c)]

    #choose between numerical and non numerical
    list_non_numerical=[] #considered column with their discriminability


    for c in non_numerical_columns_considered:

      value=df[c].loc[entity_row]

      #pas nan
      if value==value:
        list_value=df[c].value_counts().index.to_list()
        added_description='The '+str(c)+' is '+str(value)
        remaining_rows=df.loc[df[c] == value].index
        new_rows_considered=[value for value in rows_considered if value in remaining_rows]
        col_cons=columns_considered.copy()
        col_cons.remove(c)

        #context is used to make non numerical entities less complex
        for cont in context:
          cont_row=self.find_row_item(cont)
          added_complexity=np.ceil(np.log2(all_columns.index(c)+1))
          new_complexity=total_complexity+added_complexity
          cont_row=cont_row[0]

          # cas 1 la valeur est le context ds ce cas la valeur est gratuite et le cout est le cout de la colonne, ou la valeur est la meme qu'un objet ds le contexte
          value=str(value)
          cont=str(cont)


          if ((cont in value) or (cont_row[1]==index_of_db and df[c].loc[cont_row[0]]==value and len(value)>2 )):
            #in not == bc of spaces
            if (cont in value):
              added_description+=' which we already talked about '
            else:
              added_description+=' which is like '+cont_row[2]+'.'
            return self.complexity_row_column(query,index_of_db,entity_row,new_complexity,rows_considered=new_rows_considered,columns_considered=col_cons,context=context,max_complexity=max_complexity,description=description+added_description,initialisation=True, min_length_description=min_length_description-1, max_length_description=max_length_description-1)
        
        o=[]
        added_complexity=np.ceil(np.log2(all_columns.index(c)+1))+np.ceil(np.log2(list_value.index(value)+1))
        new_complexity=total_complexity+added_complexity
        added_description+='. '

        if (added_complexity>max_complexity):
          continue
        else:
          list_non_numerical.append((c,len(new_rows_considered),new_complexity))

      else:
        continue

    contrast_c=contrast(df,entity_row,numerical_columns_considered,rows_considered).tolist()
    list_non_numerical.sort(key=lambda x:x[1])


    if (len(contrast_c)==0 and len(list_non_numerical)==0 ):
      return (description,total_complexity)  #plus de colonnes c la fin

    if (len(contrast_c)>0):

      contrast_c=contrast_c[0]
      value=df[contrast_c].loc[entity_row]
      list_value=df[contrast_c].value_counts().index.to_list()
      added_description='The '+str(contrast_c)+' is '+str(value)
      remaining_rows_contrast=df.loc[df[contrast_c] == value].index
      rank=df['rank_'+contrast_c].loc[entity_row]
      invrank=df['invrank_'+contrast_c].loc[entity_row]
      added_complexity_contrast_rank=np.ceil(np.log2(all_columns.index(contrast_c)+1))+np.ceil(np.log2(rank+1))
      added_complexity_contrast_invrank=np.ceil(np.log2(all_columns.index(contrast_c)+1))+np.ceil(np.log2(invrank+1))
      if (added_complexity_contrast_rank< added_complexity_contrast_invrank):
        added_complexity_contrast=added_complexity_contrast_rank
      else:
        added_complexity_contrast=added_complexity_contrast_invrank
      if (len(list_non_numerical)>0):  # les 2 non vides 

        if (list_non_numerical[0][2]<added_complexity_contrast):
          c=list_non_numerical[0][0]  # nominatif discrimine plus
          added_complexity=list_non_numerical[0][2]

        else:
          c=contrast_c   #numerique discrimine plus
          added_complexity=added_complexity_contrast

      else:
        c=contrast_c # nominatif est vide
        added_complexity=added_complexity_contrast

    else:
      c=list_non_numerical[0][0] # numerique est vide
      added_complexity=list_non_numerical[0][2]
      # if (value)
      # added_complexity
    # return (df,entity_row,columns_considered,rows_considered)
    #return (numerical_columns_considered,non_numerical_columns_considered)

    #added complexity est trop grand, mieux vaut arrêter
    cost_uncertainty=np.ceil(np.log2(len(rows_considered)+1)) # a enlever
    if (cost_uncertainty+4<added_complexity):
      if (min_length_description<=0):
        return (description,total_complexity)
      else:
        description+='||'
        print("added_complexity",added_complexity)
        print("cost_uncertainty",cost_uncertainty)
        return (description,total_complexity)
        # rows_considered=np.arange(len(df)).tolist()
        # return self.complexity_row_column(query,index_of_db,entity_row,new_complexity,rows_considered=rows_considered,columns_considered=columns_considered,context=context,description=description,initialisation=True, min_length_description=min_length_description-1, max_length_description=max_length_description-1)
    else:
      if (added_complexity-np.ceil(np.log2(all_columns.index(c)+1))-5>max_complexity  and max_complexity<12):
        description+='If I continue my explanation you may not understand ....'
        return (description,total_complexity)
      else:
        value=df[c].loc[entity_row]
        list_value=df[c].value_counts().index.to_list()
        added_description='The '+str(c)+' is '+str(value)
        remaining_rows=df.loc[df[c] == value].index
        new_rows_considered=[value for value in rows_considered if value in remaining_rows]
        col_cons=columns_considered.copy()
        col_cons.remove(c)
        new_complexity=total_complexity+added_complexity
        added_description+='. '

        return self.complexity_row_column(query,index_of_db,entity_row,new_complexity,rows_considered=new_rows_considered,columns_considered=col_cons,max_complexity=max_complexity,context=context,description=description+added_description,initialisation=True, min_length_description=min_length_description-1, max_length_description=max_length_description-1)

  def complexity(self):
    liste=self.find_row()
    descriptor=[]
    strings=''
    iter=0
    for s in liste:
      descriptor.append(self.complexity_row_column(s[2],s[1],s[0],context=self.context,min_length_description=self.min_length_description))
      iter+=1
      if (len(descriptor[-1][0])>11):
        strings+=descriptor[-1][0]+'Type of the entity: '+str(self.dblist_names[s[1]])+'_________________________________________________'
    descriptor.sort(key = lambda x: x[1])
    return strings