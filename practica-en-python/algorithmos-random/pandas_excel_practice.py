import pandas as pd 
import numpy as np

#####
##### FIRST EXCERCISE WITH PANDAS-EXCEL
#####
with pd.ExcelFile("C:\\Users\\asus 2020\\Desktop\\LITO-CLASES\\LITO-U\\FINAL-DEL-CICLO.xlsx") as f:
    df = pd.read_excel(f)
    df_excel = pd.read_excel(f)
    df2 = pd.DataFrame([[int(b*100) for b in np.random.rand(6,)] for a in range(10116)],
                        columns=[a for a in df.columns])
    df3 = df.append(df2,ignore_index=True)  
    time = np.random.randn(1,)[0]
    time2 = np.random.randn(2,)[1]
    df3.to_excel("C:\\Users\\asus 2020\\Desktop\\LITO-CLASES\\LITO-U\\RANDOM_EXAMPLE_{}.xlsx".format(str(time)[:5]))
#####
##### SECOND EXCERCISE WITH PANDAS-EXCEL
#####
another_path = "C:\\Users\\asus 2020\\Desktop\\LITO-CLASES\\python-command-terminal-stuff\\python-finantial-skills\\"
df_guide = pd.read_csv(another_path+"sp500_joined_closes.csv",index_col=0)
path = "C:\\Users\\asus 2020\\Desktop\\LITO-CLASES\\LITO-U\\TRADE_EXCEL_{}.xlsx".format(str(time2)[:5])

writer = pd.ExcelWriter(path,engine="xlsxwriter")

for a in df_guide.columns:
    try:
        df_csv = pd.read_csv(another_path+"{}.csv".format(a))
        df_describe = df_csv.describe()
        df_describe.to_excel(writer,sheet_name="{}_stats".format(a))
        df_csv.to_excel(writer,sheet_name="{}".format(a),float_format="%.2f")
    except:
        continue
writer.save()
writer.close()
