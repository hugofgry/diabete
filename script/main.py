import modeleRF
import modeleClust
import api




data = modeleRF.get_data()
# Train = modeleRF.create_train_data(data)
# X = modeleRF.transform_date(Train)
# my_rf = modeleRF.model(Train,X)
# modeleRF.extract_model(my_rf)




# df = modeleClust.transform_data(data)
# kmeans = modeleClust.modeleClust(df)
# modeleClust.saveModel(kmeans)



api.create_X_prediction('2009-04-27 08:10:00',data)
