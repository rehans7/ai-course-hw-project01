import csv
import numpy as np
import pandas as pd
def rating(score):
    if score>=90:
        return "Ready"
    elif score>=50 and score<90:
        return "Almost Ready"
    else:
        return "Needs Work"

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

#new knowledge/columns
df["Total_Score"]=df["Python_Score"]+df["Communication_Score"]+df["Aptitude_Score"]+df["SQL_Score"]
df["Average_Score"]=df["Total_Score"]/4
df["Weakest_Skill_Score"]=df[["Python_Score","Communication_Score","Aptitude_Score","SQL_Score"]].min(axis=1).astype(int)
df["Readiness_Score"]=(df["Average_Score"]+2*df["Projects_Completed"]+df["Mock_Interviews_Attended"]).clip(upper=100)
df["Readiness_Band"]=df["Readiness_Score"].map(rating)

#pushing new columns to our csv file
df.to_csv("placement_readiness.csv",index=False)

readyCnt=(df["Readiness_Band"]=="Ready").sum()
aReadyCnt=(df["Readiness_Band"]=="Almost Ready").sum()
nwCnt=(df["Readiness_Band"]=="Needs Work").sum()



