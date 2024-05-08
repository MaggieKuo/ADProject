import streamlit as st
import openai

# 設置您的 OpenAI API 密鑰
openai.api_key = 'sk-Your-OpenAI-API-Key'
# Streamlit 應用介面
st.title("OpenAI GPT-3.5-turbo Demo")

# 創建兩個輸入框讓使用者輸入系統提示和使用者提示
system_prompt = st.text_area("System Prompt", "You are a helpful assistant.")
user_prompt = st.text_area("User Prompt", "Explain how blockchain technology works.")

# 創建一個按鈕，當被按下時執行模型呼叫
if st.button("Submit"):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    # 將結果顯示在前端畫面
    st.write(response['choices'][0]['message']['content'])


