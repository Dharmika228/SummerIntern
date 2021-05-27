// saving the model

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
if "N" in c:
    break    

