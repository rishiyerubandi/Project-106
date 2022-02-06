import numpy as np 
import csv
import pandas as pd 
import plotly.express as px

with open("Student Marks vs Days Present.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Marks In Percentage", y="Days Present")
    fig.show()

def getDataSource(data_path):
    marks = []
    daysPresent = []
    with open(data_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            marks.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
    return {"x":marks, "y":daysPresent}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation Between Days Present and Marks:- \n---", correlation[0,1])

def setUp():
    data_path = "Student Marks vs Days Present.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

setUp()