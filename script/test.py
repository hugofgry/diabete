import pandas as pd
import psycopg2 as psp
df = pd.read_csv("/Users/hugofugeray/Desktop/diabetCO/archive/diabetes_binary_health_indicators_BRFSS2015.csv")


def get_symptomes_from_DB():
    conn = psp.connect(
          database="diabete",
          user = "hugofugeray",
          password = "postgres",
          host = "localhost",
          port = "5432"
      )
    c = conn.cursor()
    c.execute(''' SELECT * FROM symptomes; ''')
    conn.commit()
    data = c.fetchall()
    conn.close()

    data = dict(data)
    return data

def insert_value_in_DB(value):
    conn = psp.connect(
          database="diabete",
          user = "hugofugeray",
          password = "postgres",
          host = "localhost",
          port = "5432"
      )
    c = conn.cursor()
    c.execute(''' SELECT * FROM symptomes; ''')
    conn.commit()


def insert_df_in_DB(df):

    conn = psp.connect(
          database="diabete",
          user = "hugofugeray",
          password = "postgres",
          host = "localhost",
          port = "5432"
      )
    c = conn.cursor()


    counter_row = 1
    counter_value = 1
    symptome_key = 1


    for row in df.iterrows():

          symptome_key = 1

          for value in row[1][1:]:
            value_tuple = (counter_value,value,symptome_key,counter_row)
            print("Now inserting value :" + str(value_tuple))
            c.execute(""" INSERT INTO Valeurs (id,valeur,symptome_id,patient_id) VALUES (%s, %s, %s, %s) """, value_tuple)
            counter_value += 1
            symptome_key += 1
            conn.commit()

          counter_row += 1


insert_df_in_DB(df)
