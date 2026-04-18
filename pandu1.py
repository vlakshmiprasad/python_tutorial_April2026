import pandas as pd
d={"name":["viraj","naveen","neeraj","vinay"],"roll number":[50,60,70,80],"percentage":[60,70,80,90]}
df=pd.DataFrame(d)
#df.head()
#df.tail()
#df.describe()
#df.shape() 
#df[0:3:1]
#df["name","percentage"]
#df[["name","percentage"]][0,3,1]
#df.iterrows()
#df.loc(1)
#df.loc(3,"name")
#df.loc(1:2,"name")
#df.loc(1:2["name","roll number"])
#df.iloc()
#df.iloc(0:2,["neeraj","roll number"])
#df.iloc(0:2,["naveen","percentage"])
#df.iloc(0:1,["prasad","name"])
#df.iloc(0:2,["praveen","percentage"])
#df.sort_values("name")
#df.sort_values("name",ascending=False)
#df.sort_values("name","roll number")
#df.sort_values("name","percentage")
#df.set_index("name")
df.set_index("roll number")
df.loc("names")
df.loc("percentage")

print(df)    