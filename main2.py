import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode
import ask_openai as ao

st.set_page_config(layout="wide")
st.header("ChatGPT")

# df = pd.read_export("ta_feng_pchome_sample.xlsx", engine='openpyxl')
df = pd.read_parquet("ta_feng_pchome_sample.parquet", engine='pyarrow')
customer_list = df['CUSTOMER_ID'].values.tolist()[0:10]
# customer_list = df['CUSTOMER_ID'].to_numpy()[:10]
col1, col2 = st.columns([1, 4])
with col1:
    st.write("## 顧客選擇")
    customer = st.selectbox("customer", customer_list)

with col2:
    df = df[df['CUSTOMER_ID'] == customer][['CUSTOMER_ID', 'PRODUCT_SUBCLASS', 'PRODUCT_NAME', 'SALES_PRICE']]
    option = GridOptionsBuilder.from_dataframe(df)
    option.configure_selection(selection_mode="multiple", use_checkbox=True)
    gridOptions = option.build()
    selection_item = AgGrid(df,
           gridOptions=gridOptions,
           coumns_auto_sizing_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
           height=500)
# st.write(selection_item['selected_rows'])
item_list = list()
for item in selection_item['selected_rows']:
    item_list.append(item['PRODUCT_NAME'])
# st.write(item_list)
promotion_item = st.text_input(label='想推銷商品')
if st.button(label='清除詢問結果'):
    st.session_state.clear()
    st.session_state['ask_list'] = list()
    # st.session_statetate['ask_list'].append({'role': 'system', 'content': 'You are a helpful building advertisements assistant.'})

st.write('---')
contain_1 = st.container()
with contain_1:
    text_ask1 = f"請告訴我{"、".join(item_list)}和{promotion_item}的相似的性質，請列舉三項，直接給我答案即可。"
    st.subheader('提問一')
    st.write(text_ask1)
    content = text_ask1
    if  st.button(label='回應', key=1):
        st.session_state['ask_list'].append({'role': 'user', 'content': content})
        ans_1 = ao.ask_chatGPT(st.session_state['ask_list'])
        st.session_state['ans_1'] = ans_1
        st.session_state['ask_list'].append({'role': 'assistant', 'content': ans_1})
    st.subheader('回答一')
    if 'ans_1' in st.session_state:
        st.write(st.session_state['ans_1'])

st.write('---')

contain_2 = st.container()
with contain_2:
    text_ask2 = f"請針對以上特點，撰寫出一篇符合目前季節的廣告文案，但重點著重在「{promotion_item}」"
    st.subheader('提問二')
    st.write(text_ask2)
    content = text_ask2
    if  st.button(label='回應', key=2):
        st.session_state['ask_list'].append({'role': 'user', 'content': content})
        ans_2 = ao.ask_chatGPT(st.session_state['ask_list'])
        st.session_state['ans_2'] = ans_2
        st.session_state['ask_list'].append({'role': 'assistant', 'content': ans_2})
    st.subheader('回答二')
    if 'ans_2' in st.session_state:
        st.write(st.session_state['ans_2'])

st.write('---')

contain_3 = st.container()
with contain_3:
    text_ask3 = f"請將上述內容濃縮在70個字以內。"
    st.subheader('提問三')
    st.write(text_ask3)
    content = text_ask3
    if  st.button(label='回應', key=3):
        st.session_state['ask_list'].append({'role': 'user', 'content': content})
        ans_3 = ao.ask_chatGPT(st.session_state['ask_list'])
        st.session_state['ans_3'] = ans_3
        st.session_state['ask_list'].append({'role': 'assistant', 'content': ans_3})
    st.subheader('回答三')
    if 'ans_3' in st.session_state:
        st.write(st.session_state['ans_3'])

st.write('---')
