import csv
import numpy as np
import pandas as pd

pyScore=[]
aptScore=[]
sqlScore=[]
comScore=[]
totalScoreSum=[]
with open("placement_readiness.csv","r",encoding="utf-8") as file:
    reader=csv.DictReader(file)
    for i in list(reader):
        pyScore.append(int(i["Python_Score"]))
        aptScore.append(int(i["Aptitude_Score"]))
        comScore.append(int(i["Communication_Score"]))
        sqlScore.append(int(i["SQL_Score"]))

# numpy operations
pyArray=np.array(pyScore)
sqlArray=np.array(sqlScore)
comArray=np.array(comScore)
aptArray=np.array(aptScore)

totalScoreSum=pyArray+sqlArray+comArray+aptArray
avgPyScore=pyArray.mean()
maxAptScore=aptArray.max()
minAptScore=aptArray.min()
comMoreThan70=(comArray>70).sum()
gap=np.maximum.reduce([pyArray,sqlArray,comArray,aptArray])-np.minimum.reduce([pyArray,sqlArray,comArray,aptArray])

#pandas operations
df=pd.read_csv("placement_readiness.csv")
top5=df.head(5)
last5=df.tail(5)
colNames=df.columns
descDf=df.describe()
pyAbove75=df[df["Python_Score"]>75]
aptSort=df.sort_values(by="Aptitude_Score",ascending=False)
pySort=df.sort_values(by="Python_Score",ascending=False)
pyTop10=pySort.head(10)
strPylowCom=df[(df["Python_Score"]>75) & (df["Communication_Score"]<50)]