
# coding: utf-8

# # Practice notebook for univariate analysis using NHANES data
# 
# This notebook will give you the opportunity to perform some univariate analyses on your own using the NHANES.  These analyses are similar to what was done in the week 2 NHANES case study notebook.
# 
# You can enter your code into the cells that say "enter your code here", and you can type responses to the questions into the cells that say "Type Markdown and Latex".
# 
# Note that most of the code that you will need to write below is very similar to code that appears in the case study notebook.  You will need to edit code from that notebook in small ways to adapt it to the prompts below.
# 
# To get started, we will use the same module imports and read the data in the same way as we did in the case study:

# In[30]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import numpy as np

da = pd.read_csv("https://raw.githubusercontent.com/kshedden/statswpy/master/NHANES/merged/nhanes_2015_2016.csv")


# ## Question 1
# 
# Relabel the marital status variable [DMDMARTL](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#DMDMARTL) to have brief but informative character labels.  Then construct a frequency table of these values for all people, then for women only, and for men only.  Then construct these three frequency tables using only people whose age is between 30 and 40.

# In[31]:


# insert your code here
da["RIAGENDR"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
da["DMDMARTL"] = da.DMDMARTL.replace({1: "Married", 2: "Widowed", 3: "Divorced", 4: "Separeted",
5: "Never Married", 6: "Living with partner", 77: "Refused", 99: "Don´t know"})
da2 = da["DMDMARTL"].loc[(da["RIAGENDR"]=="Female"),].value_counts()
da3 = da["DMDMARTL"].loc[(da["RIAGENDR"]=="Male"),].value_counts()
da4 = da["DMDMARTL"].loc[(da["RIDAGEYR"]>=30) & (da["RIDAGEYR"]<=40) & (da["RIAGENDR"]=="Female"),].value_counts()
da5 = da["DMDMARTL"].loc[(da["RIDAGEYR"]>=30) & (da["RIDAGEYR"]<=40) & (da["RIAGENDR"]=="Male"),].value_counts()
print("Female\n")
print(da2)
print("\nMale\n")
print(da3)
print("\nBoths\n")
print(da.DMDMARTL.value_counts())
print("\n30 =< Female >= 40\n")
print(da4)
print("\n30 =< Male > 40\n")
print(da5)


# __Q1a.__ Briefly comment on some of the differences that you observe between the distribution of marital status between women and men, for people of all ages.
#We got more men married than women, if we have compered them for all ages. (1477 and 1303 respectively).
# __Q1b.__ Briefly comment on the differences that you observe between the distribution of marital status states for women between the overall population, and for women between the ages of 30 and 40.
#There are more women than men married between the ages of 30 and 40. (285 and 275 respectively).
# __Q1c.__ Repeat part b for the men.
#Married 275, Never Married 101, Living with partner 78, Divorced 24, Separeted 12, Widowed 3 and Refused 1.
# ## Question 2
# 
# Restricting to the female population, stratify the subjects into age bands no wider than ten years, and construct the distribution of marital status within each age band.  Within each age band, present the distribution in terms of proportions that must sum to 1.

# In[32]:


# insert your code here
import pandas as pd
da = pd.read_csv("https://raw.githubusercontent.com/kshedden/statswpy/master/NHANES/merged/nhanes_2015_2016.csv")
da['DMDMARTLx'] = da.DMDMARTL.replace({1: 'Married', 2: 'Widowed', 3: 'Divorced',
                                       4: 'Separated', 5: 'Never Married', 
                                       6: 'Living with Partner',
                                       77: 'Refused', 99: 'Don\'t Know'})
da['RIAGENDRx'] = da.RIAGENDR.replace({1: 'Male', 2: 'Female'})

da1 = da.loc[(da["RIAGENDRx"]=="Female"),]

da1["agegrp"] = pd.cut(da.RIDAGEYR, [20,30,40,50,60,70,80])

dx = da1.loc[~da.DMDMARTLx.isin(["Don't know", "Missing"]), :]
dx = dx.groupby(["agegrp"])["DMDMARTLx"]
dx = dx.value_counts()
dx = dx.unstack()
dx = dx.apply(lambda x: x/x.sum(),axis=0)
print(dx.to_string(float_format="%.3f"))


# __Q2a.__ Comment on the trends that you see in this series of marginal distributions.
#The range with most common divorced is between 50 and 70 of age and almost all the widowed exists on 70 to 80
# __Q2b.__ Repeat the construction for males.

# In[33]:


# insert your code here
import pandas as pd
da = pd.read_csv("https://raw.githubusercontent.com/kshedden/statswpy/master/NHANES/merged/nhanes_2015_2016.csv")
da['DMDMARTLx'] = da.DMDMARTL.replace({1: 'Married', 2: 'Widowed', 3: 'Divorced',
                                       4: 'Separated', 5: 'Never Married', 
                                       6: 'Living with Partner',
                                       77: 'Refused', 99: 'Don\'t Know'})
da['RIAGENDRx'] = da.RIAGENDR.replace({1: 'Male', 2: 'Female'})

da1 = da.loc[(da["RIAGENDRx"]=="Male"),]

da1["agegrp"] = pd.cut(da.RIDAGEYR, [20,30,40,50,60,70,80])

dx = da1.loc[~da.DMDMARTLx.isin(["Don't know", "Missing"]), :]
dx = dx.groupby(["agegrp"])["DMDMARTLx"]
dx = dx.value_counts()
dx = dx.unstack()
dx = dx.apply(lambda x: x/x.sum(),axis=0)
print(dx.to_string(float_format="%.3f"))


# __Q2c.__ Comment on any notable differences that you see when comparing these results for females and for males.
#The range of refused between man and women change a lot because the only range with refused for women exist between 50 and 60, but for the men is between 30 and 40.
# ## Question 3
# 
# Construct a histogram of the distribution of heights using the BMXHT variable in the NHANES sample.

# In[34]:


# insert your code here
import pandas as pd
import seaborn as sns
da = pd.read_csv("https://raw.githubusercontent.com/kshedden/statswpy/master/NHANES/merged/nhanes_2015_2016.csv")
da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
sns.distplot(da["BMXHT"].dropna(), bins= 100, kde=False).set_title("Total Heights")

plt.show()


# __Q3a.__ Use the `bins` argument to [distplot](https://seaborn.pydata.org/generated/seaborn.distplot.html) to produce histograms with different numbers of bins.  Assess whether the default value for this argument gives a meaningful result, and comment on what happens as the number of bins grows excessively large or excessively small. 
#When i put a bin equal to one houndred the weight for any band turns excessively small
# __Q3b.__ Make separate histograms for the heights of women and men, then make a side-by-side boxplot showing the heights of women and men.

# In[35]:


# insert your code here
import pandas as pd
import seaborn as sns
da = pd.read_csv("nhanes_2015_2016.csv")
da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
df = da.loc[da.RIAGENDRx.isin(["Female"]), :]
dm = da.loc[da.RIAGENDRx.isin(["Male"]), :]
sns.boxplot(df["BMXHT"]).set_title("Total Heights Female")
plt.show()
sns.boxplot(dm["BMXHT"]).set_title("Total Heights Male")

plt.show()


# __Q3c.__ Comment on what features, if any are not represented clearly in the boxplots, and what features, if any, are easier to see in the boxplots than in the histograms.
The difference between the first quartile and the third quartile its bigger in women than men
# ## Question 4
# 
# Make a boxplot showing the distribution of within-subject differences between the first and second systolic blood pressure measurents ([BPXSY1](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BPX_I.htm#BPXSY1) and [BPXSY2](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BPX_I.htm#BPXSY2)).

# In[45]:


# insert your code here
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
da = pd.read_csv("nhanes_2015_2016.csv")
da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
df = da.BPXSY1
df1 = da.BPXSY2
dff = df-df1
sns.boxplot(dff).set_title("Difference of pressure betwen BPXSY1 and BPXSY2")
plt.show()


# __Q4a.__ What proportion of the subjects have a lower SBP on the second reading compared to the first?

# In[54]:


# insert your code here
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
da = pd.read_csv("nhanes_2015_2016.csv")
da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
df = da.BPXSY1
df1 = da.BPXSY2
print(df1.describe()-df.describe())
print(df.describe()-df1.describe())


# __Q4b.__ Make side-by-side boxplots of the two systolic blood pressure variables.

# In[61]:


# insert your code here

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
da = pd.read_csv("nhanes_2015_2016.csv")
da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
sns.boxplot(data=da.loc[:, ["BPXSY1", "BPXSY2"]])
plt.show()


# __Q4c.__ Comment on the variation within either the first or second systolic blood pressure measurements, and the variation in the within-subject differences between the first and second systolic blood pressure measurements.
The difference between boths its too small -0.3 in the mean, but they have a big difference on counts.
# ## Question 5
# 
# Construct a frequency table of household sizes for people within each educational attainment category (the relevant variable is [DMDEDUC2](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#DMDEDUC2)).  Convert the frequencies to proportions.

# In[1]:


# insert your code here

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
da = pd.read_csv("nhanes_2015_2016.csv")
df = da["DMDEDUC2"].value_counts()
df1 = da["DMDEDUC2"].count()
df2 = df/df1


print(df2)


# __Q5a.__ Comment on any major differences among the distributions.
The distribution got the biggest proportion between 1 and 5 with just one outlier in 9.
# __Q5b.__ Restrict the sample to people between 30 and 40 years of age.  Then calculate the median household size for women and men within each level of educational attainment.

# In[21]:


# insert your code here
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
da = pd.read_csv("nhanes_2015_2016.csv")
df = da.loc[(da["RIDAGEYR"]>=30) & (da["RIDAGEYR"]<=40),]
da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
df1 = df.loc[(da["RIAGENDRx"]=="Male"),]
df2 = df.loc[(da["RIAGENDRx"]=="Female"),]
print("The median for men between 30 and 40 years of age is: ",df1["DMDEDUC2"].describe()["50%"])
print(df1["DMDEDUC2"].describe())
print("The median for women between 30 and 40 years of age is: ",df2["DMDEDUC2"].describe()["50%"])
print(df2["DMDEDUC2"].describe())
print(df["DMDEDUC2"].value_counts())
print(df ["DMDEDUC2"].count())


# ## Question 6
# 
# The participants can be clustered into "maked variance units" (MVU) based on every combination of the variables [SDMVSTRA](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#SDMVSTRA) and [SDMVPSU](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#SDMVPSU).  Calculate the mean age ([RIDAGEYR](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#RIDAGEYR)), height ([BMXHT](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BMX_I.htm#BMXHT)), and BMI ([BMXBMI](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BMX_I.htm#BMXBMI)) for each gender ([RIAGENDR](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#RIAGENDR)), within each MVU, and report the ratio between the largest and smallest mean (e.g. for height) across the MVUs.

# In[57]:


# insert your code here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
da = pd.read_csv("nhanes_2015_2016.csv")
da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
df = da.loc[(da["RIAGENDRx"]=="Male"),]
df1 = da.loc[(da["RIAGENDRx"]=="Female"),]

dff = df.groupby(["SDMVPSU", "SDMVSTRA"])["RIDAGEYR"].mean().max()
dffa = df.groupby(["SDMVPSU", "SDMVSTRA"])["RIDAGEYR"].mean().min() 
dff1 = df1.groupby(["SDMVPSU", "SDMVSTRA"])["RIDAGEYR"].mean().max()
dff1a = df1.groupby(["SDMVPSU", "SDMVSTRA"])["RIDAGEYR"].mean().min()

d_1 = df.groupby(["SDMVPSU", "SDMVSTRA"])["BMXHT"].mean().max()
d_2 = df.groupby(["SDMVPSU", "SDMVSTRA"])["BMXHT"].mean().min()
d_3 = df1.groupby(["SDMVPSU", "SDMVSTRA"])["BMXHT"].mean().max()
d_4 = df1.groupby(["SDMVPSU", "SDMVSTRA"])["BMXHT"].mean().min()

df_1 = df.groupby(["SDMVPSU", "SDMVSTRA"])["BMXBMI"].mean().max()
df_2 = df.groupby(["SDMVPSU", "SDMVSTRA"])["BMXBMI"].mean().min()
df_3 = df1.groupby(["SDMVPSU", "SDMVSTRA"])["BMXBMI"].mean().max()
df_4 = df1.groupby(["SDMVPSU", "SDMVSTRA"])["BMXBMI"].mean().min() 

print("The age mean  max for men is: ",dff)
print("The age mean min for men is: ",dffa)
print("The age mean max for women is: ",dff1)
print("The age mean min for women is: ",dff1a,"\n")
print("Male ratio is: ",dff/dffa)
print("Female ratio is: ",dff1/dff1a,"\n")

print("The height mean  max for men is: ",d_1)
print("The height mean min for men is: ",d_2)
print("The height mean max for women is: ",d_3)
print("The height mean min for women is: ",d_4,"\n")
print("Male ratio is: ",d_1/d_2)
print("Female ratio is: ",d_3/d_4,"\n")

print("The BMI mean  max for men is: ",df_1)
print("The BMI mean min for men is: ",df_2)
print("The BMI mean max for women is: ",df_3)
print("The BMI mean min for women is: ",df_4,"\n")
print("Male ratio is: ",df_1/df_2)
print("Female ratio is: ",df_3/df_4)


# __Q6a.__ Comment on the extent to which mean age, height, and BMI vary among the MVUs.
For men: The variation ratio between age is 1.31, height 1.04, and BMI 1.23.
In the cases for women: The variation ratio between age is 1.307, height 1.04, and BMI 1.24
# __Q6b.__ Calculate the inter-quartile range (IQR) for age, height, and BMI for each gender and each MVU.  Report the ratio between the largest and smalles IQR across the MVUs.

# In[84]:


# insert your code here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
da = pd.read_csv("nhanes_2015_2016.csv")
da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
df = da.loc[(da["RIAGENDRx"]=="Male"),]
df1 = da.loc[(da["RIAGENDRx"]=="Female"),]

dff = df.groupby(["SDMVPSU", "SDMVSTRA"])["RIDAGEYR"].describe().max()[4]
dff32 = df.groupby(["SDMVPSU", "SDMVSTRA"])["RIDAGEYR"].describe().max()[6]
dffa = df.groupby(["SDMVPSU", "SDMVSTRA"])["RIDAGEYR"].describe().min()[4]
dffb = df.groupby(["SDMVPSU", "SDMVSTRA"])["RIDAGEYR"].describe().min()[6]

dff1 = df1.groupby(["SDMVPSU", "SDMVSTRA"])["RIDAGEYR"].describe().max()[4]
dff1_ = df1.groupby(["SDMVPSU", "SDMVSTRA"])["RIDAGEYR"].describe().max()[6]
dff1a = df1.groupby(["SDMVPSU", "SDMVSTRA"])["RIDAGEYR"].describe().min()[4]
dff1a_ = df1.groupby(["SDMVPSU", "SDMVSTRA"])["RIDAGEYR"].describe().min()[6]

d_1 = df.groupby(["SDMVPSU", "SDMVSTRA"])["BMXHT"].describe().max()[4]
d_11 = df.groupby(["SDMVPSU", "SDMVSTRA"])["BMXHT"].describe().max()[6]
d_2 = df.groupby(["SDMVPSU", "SDMVSTRA"])["BMXHT"].describe().min()[4]
d_21 = df.groupby(["SDMVPSU", "SDMVSTRA"])["BMXHT"].describe().min()[6]

d_3 = df1.groupby(["SDMVPSU", "SDMVSTRA"])["BMXHT"].describe().max()[4]
d_31 = df1.groupby(["SDMVPSU", "SDMVSTRA"])["BMXHT"].describe().max()[6]
d_4 = df1.groupby(["SDMVPSU", "SDMVSTRA"])["BMXHT"].describe().min()[4]
d_41 = df1.groupby(["SDMVPSU", "SDMVSTRA"])["BMXHT"].describe().min()[6]

df_1 = df.groupby(["SDMVPSU", "SDMVSTRA"])["BMXBMI"].describe().max()[4]
df_11 = df.groupby(["SDMVPSU", "SDMVSTRA"])["BMXBMI"].describe().max()[6]
df_2 = df.groupby(["SDMVPSU", "SDMVSTRA"])["BMXBMI"].describe().min()[4]
df_21 = df.groupby(["SDMVPSU", "SDMVSTRA"])["BMXBMI"].describe().min()[6]

df_3 = df1.groupby(["SDMVPSU", "SDMVSTRA"])["BMXBMI"].describe().max()[4]
df_31 = df1.groupby(["SDMVPSU", "SDMVSTRA"])["BMXBMI"].describe().max()[6]
df_4 = df1.groupby(["SDMVPSU", "SDMVSTRA"])["BMXBMI"].describe().min()[4]
df_41 = df1.groupby(["SDMVPSU", "SDMVSTRA"])["BMXBMI"].describe().min()[6]


print("The age IQR  max for men is: ",dff32-dff)
print("The age IQR min for men is: ",dffb-dffa)
print("The age IQR max for women is: ",dff1_-dff1)
print("The age IQR min for women is: ",dff1a_-dff1a,"\n")

print("The height IQR  max for men is: ",d_11-d_1)
print("The height IQR min for men is: ",d_21-d_2)
print("The height IQR max for women is: ",d_31-d_3)
print("The height IQR min for women is: ",d_41-d_4,"\n")

print("The BMI IQR  max for men is: ",df_11-df_1)
print("The BMI IQR min for men is: ",df_21-df_2)
print("The BMI IQR max for women is: ",df_31-df_3)
print("The BMI IQR min for women is: ",df_41-df_4,"\n")


# __Q6c.__ Comment on the extent to which the IQR for age, height, and BMI vary among the MVUs.
The max IQR between  men and women vary: on age 3.5, on height 1.3, and on BMI 2.2. 
The min IQR between  men and women vary: on age 0.75, on height 2.02, and on BMI 2.9. 