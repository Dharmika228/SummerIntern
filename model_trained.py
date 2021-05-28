import pandas
ds = pandas.read_csv('SalaryData.csv') #used to load the csv file

print("Dataset collected")

ds.info() # gives the details of dataset
print("the details\n")

x = ds['YearsExperience']
y = ds['Salary']

x = ds['YearsExperience'].values.reshape(30,1) #.values converts in pandas to numpy array

from sklearn.linear_model import LinearRegression
#takes the dataset and trains the model using Linear_function()

model = LinearRegression()

print("Model has been trained\n")

model.fit(x,y)  #uses Linear_Function=> y = c + wx

print("The predicted value of salary with x=2.5 is",model.predict([[2.5]]))


print("the co-efficient found",model.coef_)

import joblib

joblib.dump(model,'SalaryData.pk1')

print("model has been saved successfully")

# saving the model

print(""" 
	to save the model:
	  Y for yes
	  N for no
	""")
c = input("enter your choice")
if "Y" in c:
    import joblib
    m1 = joblib.load('SalaryData.pk1')
    print("successfully built")
else:
    print("bye")
