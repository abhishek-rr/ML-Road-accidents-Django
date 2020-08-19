from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from efficient_apriori import apriori
import random

'''
def hello(request):
	housing = pd.read_csv('assets/data12.csv')
	X=housing.drop('MEDV',axis=1)
	Y=housing['TAX']
	X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.33,random_state=42)
	GaussNB=GaussianNB()
	GaussNB.fit(X_train,Y_train)
	pred_tr=GaussNB.predict(X_test)
	context = {'pred': pred_tr,}


	return render(request, 'analysis.html', context)


'''
def hello (request):
	val1=int(request.GET['num1'])
	val2= int(request.GET['num2'])
	df = pd.read_csv('assets/accident2.csv')

	#X=df.drop('MEDV', axis=1)
	X = df.iloc[:, [2,3]].values  # X is the features in our dataset
	y = df['TOTAL']

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.24, random_state=17)

	model = GaussianNB()
	model.fit(X_train, y_train)
	predicted_y = model.predict(X_train)

    # now calculating that how much accurate our model is with comparing our predicted values and y_test values
   # accuracy_score = accuracy_score(y_test, predicted_y)
   # print(accuracy_score)
    # df.columns
	person = pd.DataFrame()

    # Create some feature values for this single row

	person['JANUARY'] = [val1]
	person['FEBRUARY'] = [val2]

    # View the data
    # person
    # the data is stored in Datadrame person
	predicted_y = model.predict(person)
	predicted_y1=int(predicted_y)
	context = {'pred': predicted_y1,}
	return render(request, 'nb.html', context)

def trial (request):
	return render(request, 'trial.html',{})



def group(request):
	data = pd.read_csv('assets/accident.csv')

	#CATEGORIZE STATE-WISE DATA INTO DIFFERENT BASKETS
	basket_Andaman = data[data['State'] =="Andaman_Nicobar"]
	basket_Assam = data[data['State'] =="Assam"]
	basket_Chandigarh = data[data['State'] =="Chandigarh"]
	basket_Delhi = data[data['State'] =="Delhi"]
	basket_Goa = data[data['State'] =="Goa"]

	#MAKE A LIST OF BUCKETS SO THAT WE CAN ITERATE THROUGH THE LIST FOR ANALYSIS OF EACH STATE
	state_list = [basket_Andaman,basket_Assam,basket_Chandigarh,basket_Delhi,basket_Goa]

	#LIST OF ATTRIBUTES. JUST SOME IMPLEMENTATION PART, YOU CAN IGNORE
	attributes_list=['Midnight','Dawn','Early_Morning','Morning','Midday','Afternoon','Evening','Night']


	#THIS LOOP PERFORMS ANALYSIS FOR EACH STATE
	for basket in state_list:
	    list = basket.values.tolist()
	    itemset=[]
	    for i in list:
	        item_list=[]
	        for attr in range(1,9):
	            if (i[attr]/i[9])*100 > 15:     #ONLY SELECT THOSE ATTRIBUTES WHICH ARE AT LEAST 15% OF THE TOTAL VALUE
	                item_list.append(attributes_list[attr-1])
	        itemset.append(item_list)

	    itemsets, rules = apriori(itemset, min_confidence = 1)

	    x=list[0][0]
	    y=rules[0]
	    a=rules[1]
	    b=rules[2]
	    c=rules[3]
	    d=rules[4]
		  #rules[0] CONTAINS THE TOPMOST ITEMSET HAVING HIGHEST SUPPORT COUNT. IF YOU WANT TO PRINT ALL THE ITEMSETS, SIMPLY print(rules)
	    context={'li':x , 'ru':y , 'a':a , 'b':b , 'c':c ,'d':d,}
	    return render(request, 'group.html', context)


#return render(request,'analysis.html',context)
