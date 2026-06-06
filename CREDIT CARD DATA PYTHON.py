# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:55:31 2026

@author: Sandeep Katta
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\Sandeep Katta\OneDrive\Documents\application_record.csv")

print(df.head())
#CHECK DATASET SIZE 
print(df.shape)
#CHECK COLUMNS 
print(df.columns)
#CHECK DATA TYPE 
print(df.info())
#CHECK MISSING VALUES 
print(df.isnull().sum())
#CREATE AGE GROUP 
df['Age'] = abs(df['DAYS_BIRTH']) / 365
print(df[['DAYS_BIRTH','Age']].head())
#CREATE AGE GROUP COLUMN 
df['Age_Group'] = pd.cut(
    df['Age'],
    bins=[0,30,50,100],
    labels=['Young','Mid Age','Senior']
)

print(df['Age_Group'].value_counts())
#CREATE INCOME CATEGORY 
df['Income_Category'] = pd.cut(
    df['AMT_INCOME_TOTAL'],
    bins=[0,100000,300000,10000000],
    labels=['Low Income','Medium Income','High Income']
)

print(df['Income_Category'].value_counts())

#GENDER DISTRIBUTION CHART 
df['CODE_GENDER'].value_counts().plot(kind='bar')
plt.title('Gender Distribution')
plt.show()
#AGE GROUP DISRTRIBUTION BAR CHART 
df['Age_Group'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Age Group Distribution')
plt.show()

#INCOME CATEGORY DISTRIBUTION 
df['Income_Category'].value_counts().plot(kind='bar')
plt.title('Income Category Distribution')
plt.show()

#Average Income by Gender
df.groupby('CODE_GENDER')['AMT_INCOME_TOTAL'].mean().plot(kind='bar')
plt.title('Average Income by Gender')
plt.show()

#Education Distribution
df['NAME_EDUCATION_TYPE'].value_counts().plot(kind='bar')
plt.title('Education Distribution')
plt.xticks(rotation=45)
plt.show()

# Income Type Distribution
df['NAME_INCOME_TYPE'].value_counts().plot(kind='bar')
plt.title('Income Type Distribution')
plt.xticks(rotation=45)
plt.show()

# Housing Type Distribution
df['NAME_HOUSING_TYPE'].value_counts().plot(kind='bar')
plt.title('Housing Type Distribution')
plt.xticks(rotation=45)
plt.show()

# Occupation Distribution
df['OCCUPATION_TYPE'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Occupations')
plt.xticks(rotation=45)
plt.show()