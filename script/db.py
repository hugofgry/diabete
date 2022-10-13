import psycopg2 as psp
import pandas as pd

conn = psp.connect(
          database="diabete",
          user = "hugofugeray",
          password = "postgres",
          host = "localhost",
          port = "5432"
      )
c = conn.cursor()

data = pd.read_csv('../archive/diabetes_binary_health_indicators_BRFSS2015.csv')

# try:



#   c.execute(' CREATE TABLE IF NOT EXISTS patient (id SERIAL PRIMARY KEY, diabete_binary INTEGER)')
#   conn.commit()
#   print('create')

# except:

#   print('error')



# diabete = data['Diabetes_binary'].astype('int')
# # #diabete_binary = int(diabete)


# for row in diabete:


#   c.execute(''' INSERT INTO patient (diabete_binary ) VALUES (%s) ''', [row])
#   conn.commit()




  #c.execute('DROP TABLE patient')

# c.execute(''' CREATE TABLE IF NOT EXISTS symptomes (id SERIAL PRIMARY KEY,
#   facteur VARCHAR(255) )''')
# conn.commit()
# print('create')


# dataX = data.drop(columns = 'Diabetes_binary')

# facteur = dataX.columns


# for column in facteur :

#   c.execute(''' INSERT INTO symptomes (facteur) VALUES (%s) ''', (column,))
#   conn.commit()








c.execute(''' CREATE TABLE IF NOT EXISTS valeurs (id SERIAL PRIMARY KEY,
  valeur INTEGER,
  patient_id INTEGER,
  symptome_id INTEGER,
  FOREIGN KEY (patient_id) REFERENCES patient(id),
  FOREIGN KEY (symptome_id) REFERENCES symptomes(id))''')
conn.commit()
print('create')

# diabete_feat = data[['HighBP','HighChol','CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits','Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost','GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income']].astype('int')

# for row_feat in diabete_feat.values:


#   c.execute(''' INSERT INTO symptome (HighBP,HighChol,CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack,PhysActivity, Fruits,Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost,GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ''', (int(row_feat[0]),int(row_feat[1]),int(row_feat[2]),int(row_feat[3]),int(row_feat[4]),int(row_feat[5]),int(row_feat[6]),int(row_feat[7]),int(row_feat[8]),int(row_feat[9]),int(row_feat[10]),int(row_feat[11]),int(row_feat[12]),int(row_feat[13]),int(row_feat[14]),int(row_feat[15]),int(row_feat[16]),int(row_feat[17]),int(row_feat[18]),int(row_feat[19]),int(row_feat[20])))
#   conn.commit()
