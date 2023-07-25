import freeGPT
import asyncio
import streamlit as st

st.title("Testing GPT - 4")



async def main():
    while True:
        prompt = st.text_input("Enter the question: " , 'hi')
        try:
            resp = await getattr(freeGPT, "gpt4").Completion.create(prompt)

            st.write(f"🤖: {resp}")
        except Exception as e:
            st.warning(f"🤖: {e}")


asyncio.run(main())