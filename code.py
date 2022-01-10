import pandas as pd
import plotly.express as px
import plotly.figure_factory as pf
import random
import statistics as st
df=pd.read_csv("studentMarks.csv")
marks=df["Math_score"].tolist()


finallist=[]
def sampling():
    dataset=[]
    for i in range(0,100):
        random_index=random.randint(0,len(marks)-1)
        data = marks[random_index]
        dataset.append(data)
    mean=st.mean(dataset)
    finallist.append(mean)

for i in range(0,1000):
    sampling()
graph=pf.create_distplot([finallist],["finaldata"],show_hist=False)
graph.show()