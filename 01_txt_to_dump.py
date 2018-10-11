import pickle
import uuid
import pandas as pd

## Data Preparation
df1 = pd.read_csv("data/news/USAEvents_OnlyUnigrams_2018_08_02_02_27_59/eventassignment.txt", sep="\t", header=None, names=[
                 "EventID", "publication", "pubid", "seqid", "canonicalUrl", "title", "text", "titleFingerprintJSON", "textFingerprintJSON", "cleanedTitle"])
# if csv file is read with automatic header an error occurs. Therefore explicit header and then remove first row by index
df1 = df1.iloc[1:,]
df1["date"] = pd.to_datetime('2018-08-02')
event_ids = df1.EventID.unique()

for id in event_ids:
    df1.loc[df1["EventID"] == id, "EventID"] = str(uuid.uuid4())

df2 = pd.read_csv("data/news/USAEvents_OnlyUnigrams_2018_08_03_09_35_50/eventassignment.txt", sep="\t", header=None, names=[
                 "EventID", "publication", "pubid", "seqid", "canonicalUrl", "title", "text", "titleFingerprintJSON", "textFingerprintJSON", "cleanedTitle"])
df2 = df2.iloc[1:,]
df2["date"] = pd.to_datetime('2018-08-03')
event_ids = df2.EventID.unique()

for id in event_ids:
    df2.loc[df2["EventID"] == id, "EventID"] = str(uuid.uuid4())

df3 = pd.read_csv("data/news/USAEvents_OnlyUnigrams_2018_08_04_15_58_03/eventassignment.txt", sep="\t", header=None, names=[
                 "EventID", "publication", "pubid", "seqid", "canonicalUrl", "title", "text", "titleFingerprintJSON", "textFingerprintJSON", "cleanedTitle"])
df3 = df3.iloc[1:,]
df3["date"] = pd.to_datetime('2018-08-04')
event_ids = df3.EventID.unique()

for id in event_ids:
    df3.loc[df3["EventID"] == id, "EventID"] = str(uuid.uuid4())


articles = df1.append([df2,df3], sort=True)

# articles.head()
# articles.describe()

pickle.dump(articles, open("data/news/articles.wtf", "wb"))
