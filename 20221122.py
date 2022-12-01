import streamlit as st
import pandas as pd

st.title('SAA Small System')
st.header('目標')
st.subheader('幫助迅得工令處理人員依照常見需求, 快速整理表單, 並提供結果表單線上瀏覽與下載服務. ')

st.header('規劃')
st.subheader('提供多種常見資料整合方法(Ex. concate, join, merge...), 供使用者快速檢視多筆資料之關聯. (以下 Demo 兩筆資料源與 3 種處理方法藉以說明)')

########################################



st.header('資料源')
st.subheader('Data1 (UserData1)')
uploaded_file = st.file_uploader("Choose your first file")
if st.checkbox('Data1 是否含 sheet name'):                                                                      # l1 = st.text_input(label='請輸入檔案一(YU)的絕對位置:', value=r'', placeholder=r'C:\Users\user\Desktop\excel_join_20221122/YM管制表 - 俊鴻.xlsx')
    s1 = st.text_input(label='請輸入檔案一(YU)的sheet name:', value=None, placeholder='若無，則不需填此欄位')   # data1 = pd.read_excel(io=l1, sheet_name=s1)     # data1.columns.values[0]
    if uploaded_file is not None:
        data1 = pd.read_excel(io=uploaded_file, sheet_name=s1)                                                                    
else:
    if uploaded_file is not None:                                                                               # l1 = st.text_input(label='請輸入檔案一(YU)的絕對位置:', value=r'', placeholder=r'C:\Users\user\Desktop\excel_join_20221122/YM管制表 - 俊鴻.xlsx')
        data1 = pd.read_excel(io=uploaded_file)                                                                 # data1 = pd.read_excel(io=l1) 
data1.columns = [i.replace('\n','') for i in data1.columns.values]                                              # 刪除有enter命名的欄位
st.dataframe(data1)
st.caption('shape:'+str(data1.shape))



st.subheader('Data2 (UserData2)')
uploaded_file2 = st.file_uploader("Choose your second file")
if st.checkbox('Data2 是否含 sheet name'):                                                                                  # l2 = st.text_input(label='請輸入檔案二(Tracy)的絕對位置:', value=r'', placeholder=r'C:\Users\user\Desktop\excel_join_20221122/YM廠機台物料未完全安裝表20221121 - Tracy.xlsx')
    s2 = st.text_input(label='請輸入檔案二(Tracy)的sheet name:', value='20221121更新', placeholder='若無，則不需填此欄位')  # data2 = pd.read_excel(io=l2, sheet_name=s2)                                                                     # data1.columns.values[0]
    if uploaded_file2 is not None:
        data2 = pd.read_excel(io=uploaded_file2, sheet_name=s2)  
else:
    if uploaded_file2 is not None:                                                                                          # l2 = st.text_input(label='請輸入檔案二(Tracy)的絕對位置:', value=r'', placeholder=r'C:\Users\user\Desktop\excel_join_20221122/YM廠機台物料未完全安裝表20221121 - Tracy.xlsx')
        data2 = pd.read_excel(io=uploaded_file2)                                                                            # data2 = pd.read_excel(io=l2)  
data2.columns = [i.replace('\n','') for i in data2.columns.values]                                                          # 刪除有enter命名的欄位
st.dataframe(data2)
st.caption('shape:'+str(data2.shape))




########################################
########################################


st.header('結果')
st.subheader('Data3 (Result1)')
# data3 = pd.merge(data1, data2, left_on="工令", right_on="工令")
st.markdown('#####  法1. 以Concat方式連接兩table, 將兩table快速合併成一檔案, 不按某欄位連接')
data3 = pd.concat([data1, data2], join="outer")
st.dataframe(data3)
st.caption('shape:'+str(data3.shape))
if st.button('Save data3 CSV'):
    data3.to_csv('data3.csv', index=False, encoding="utf_8_sig")     #繁體中文記得要加utf_8_sig



st.subheader('Data4 (Result2)')
st.markdown('#####  法2. 以Full Join方式連接兩table, 兩table按某欄位為準')
a1 = st.text_input(label='請輸入第一個待合併的欄位名稱', value='工令')
data4 = pd.merge(data1, data2, on=a1, how='outer')
st.dataframe(data4)
st.caption('shape:'+str(data4.shape))
if st.button('Save data4 CSV'):
    data4.to_csv('data4.csv', index=False, encoding="utf_8_sig")     #繁體中文記得要加utf_8_sig




st.subheader('Data5 (Result3)')
st.markdown('#####  法3. 和法2差異在合併時, 依據之欄位數由1個提升至2個')
a2 = st.text_input(label='請輸入第二個待合併的欄位名稱', value='機型')
data5 = data1.join(data2.set_index([a1, a2]), on = [a1, a2], how="outer", lsuffix='_l', rsuffix='_r')
st.dataframe(data5)
st.caption('shape:'+str(data5.shape))
if st.button('Save data5 CSV'):
    data5.to_csv('data5.csv', index=False, encoding="utf_8_sig")     #繁體中文記得要加utf_8_sig




###################################################################

# st.header('Data6 (LEFT OUTER JOIN)')
# st.subheader('以Left Join方式連接兩table: 旨意將兩table按某特一欄位連接, 且以左側資料表為主連接.')
# st.text('using SQLite (前面所有均使用 pandas)')

# import sqlite3
# conn = sqlite3.connect('vito.db')                                   #建立資料庫
# cursor = conn.cursor()
# cursor.execute('DROP TABLE yu')                                     #移除資料表
# conn.commit()
# cursor.execute(f"""CREATE TABLE yu{eval(str([i for i in data1.columns.values]).replace(']','').replace('[',''))}""")  #建立資料表
# conn.commit()
# data1.to_sql('yu', conn, if_exists='append', index=False)           #如果資料表存在，就寫入資料，否則建立資料表

# conn = sqlite3.connect('vito.db')                                   #建立資料庫
# cursor = conn.cursor()
# cursor.execute('DROP TABLE tracy')                                  #移除資料表
# conn.commit()
# cursor.execute(f"""CREATE TABLE tracy{eval(str([i for i in data2.columns.values]).replace(']','').replace('[',''))}""")  #建立資料表
# conn.commit()
# data2.to_sql('tracy', conn, if_exists='append', index=False)        #如果資料表存在，就寫入資料，否則建立資料表

# final_df = pd.read_sql('''  SELECT  yu.工令, yu.機型 as [機型(yu)], tracy.機型 as [機型(tracy)], yu.樓層, yu.產線, yu.Driver, yu.IEM, yu.DB, 
#                                     yu.Comment, tracy.實際樓層位置, tracy.電腦螢幕是否有安裝, tracy.SmartBox是否有安裝, 
#                                     tracy.[其他配件(HDMI、網路線、USB延長線、滑鼠、鍵盤、Dongle、插座)], tracy.[HDMI(配件)], tracy.[網路線(配件)],
#                                     tracy.[USB延長線(配件)], tracy.[滑鼠(配件)], tracy.[鍵盤(配件)], tracy.[Dongle(配件)], tracy.[插座(配件)], 
#                                     電源線, 是否可安裝, 掛架、掛架上讀頭, 機台內讀頭, 備註
#                             FROM yu 
#                             left OUTER JOIN tracy 
#                             ON yu.工令 = tracy.工令''', conn)       #sql查詢並轉dataframe

# st.dataframe(final_df)
# st.caption('shape:'+str(final_df.shape))

# if st.button('Save Final CSV'):
#     final_df.to_csv('final.csv', index=False, encoding="utf_8_sig")     #繁體中文記得要加utf_8_sig

