import requests
import os
import json
import openai
from openai import OpenAI
import streamlit as st
import anthropic
from anthropic import HUMAN_PROMPT, AI_PROMPT
import random
import mysql.connector

#CREATING THE MYSQL CONNECTION
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1611bobo",
    database="votes"
)

cursor = conn.cursor()

#PRINT THE MOST POPULAR BOT

cursor.execute("SELECT vote, COUNT(vote) as vote_count FROM chat_bot_votes GROUP BY vote ORDER BY vote_count DESC LIMIT 1")
most_popular_bot = cursor.fetchone()

# conn.close()
if most_popular_bot:
    bot_name, bot_count = most_popular_bot
    # print(f"The most popular bot is {bot_name} with {bot_count} votes.")
    st.text_area("The most popular bot is:", value=f"{bot_name} with {bot_count} votes.", height=30, disabled=True)

#GETTING THE API KEYS
APIKEY_CHAT_GPT = os.getenv('OPENAI_API_KEY')
CLAUDE_API = os.getenv('CLAUDE_API_KEY')

if APIKEY_CHAT_GPT and CLAUDE_API is not None:
    print("API Keys retrieved successfully!")
    # You can now use your API key for further operations
else:
    print("Please check the environment variable name.")

#WORKING WITH OPENAI API
# openai.api_key = APIKEY
client= OpenAI(api_key = APIKEY_CHAT_GPT)

def chat_gpt_output(message):
    output = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        max_tokens= 100,
        messages=[{"role": "user","content":f"{message}"}]
    )

    return output.choices[0].message.content

#WORKING WITH CLAUDE API
def claude_output(message):
    output = anthropic.Anthropic(api_key=CLAUDE_API).completions.create(
        model="claude-2.1",
        max_tokens_to_sample=100,
        prompt=f"{HUMAN_PROMPT} {message} {AI_PROMPT}",
    )
    return output.completion

#STREAMLIT APP
st.title("💬 Chatbot Playground")
message = st.text_input("Let's see which AI is better. Write something:")
if message:
    first_one = random.choice([1,2,3,4,5,6])
    if first_one>3:
        response1 = chat_gpt_output(message)
        response2 = claude_output(message)
    else:
        response1 = claude_output(message)
        response2 = chat_gpt_output(message)

    col1, col2 = st.columns(2)
    with col1:
        st.text_area("Bot 1 Response:", value=response1, height=150,disabled=True)
        if st.button("Select Bot 1 Response", key='select1'):
            st.session_state.selected = "Bot 1"
    with col2:
        st.text_area("Bot 2 Response:", value=response2, height=150, disabled=True)
        if st.button("Select Bot 2 Response", key='select2'):
            st.session_state.selected = "Bot 2"

    if 'selected' in st.session_state:
        if first_one>3:
            st.success(f"You selected Chat GPT's response.")
            cursor.execute("INSERT INTO chat_bot_votes (vote) VALUES ('Chat GPT')")
            conn.commit()
            conn.close()

        else:
            st.success(f"You selected Claude's response.")
            cursor.execute("INSERT INTO chat_bot_votes (vote) VALUES ('Claude')")
            conn.commit()
            conn.close()

