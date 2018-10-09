import os
import json
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/news/USAEvents_OnlyUnigrams_2018_08_02_02_27_59/eventassignment.txt", sep="\t", header=None, names=[
                 "EventID", "publication", "pubid", "seqid", "canonicalUrl", "title", "text", "titleFingerprintJSON", "textFingerprintJSON", "cleanedTitle"])

df.head()

df.columns

df["publication"].describe()

publisher_size = df.groupby("publication").size()

ax = publisher_size.plot.kde()
publisher_size.plot.hist(ax=ax, secondary_y = True, title="Histogram")

plt.hist(publisher_size, log = True)
plt.title("Log Histogram of Publisher Size")

publisher_size.nlargest(15).plot.bar(title="Top 15 largest publishers")

publisher_size[publisher_size > 50].count()

df["EventID"].describe()

event_size = df.groupby("EventID").size()

ax = event_size.plot.kde()
event_size.plot.hist(ax=ax, secondary_y = True, title="Histogram")

plt.hist(event_size, log = True)
plt.title("Log Histogram of Event Size")

event_size.nlargest(15)
