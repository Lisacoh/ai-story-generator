# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sznTkbrvoPgrfpIy2-iL2O0Mlc9sCMNz
"""



import streamlit as st
import openai
import os

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.set_page_config(page_title="AI Story Generator", page_icon="📚")
st.title("📖 AI-Powered Story Generator")
st.subheader("Create short educational stories for kids aged 11–13")

# Topic input
theme = st.text_input("Enter a topic (e.g. gravity, empathy, ancient Egypt):")

# Generate button
if st.button("Generate Story"):
    if theme.strip() == "":
        st.warning("Please enter a topic before generating.")
    else:
        with st.spinner("Generating your story..."):
            prompt = f"""
You are a friendly storyteller AI.
Create a short and engaging educational story (5–7 sentences) for a child aged 11 to 13.
The story must be simple, fun, and teach a concept related to this topic: "{theme}".
Use clear language and include a fictional character to guide the story.
End the story with a short message or reflection.

Story:
"""
            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",  # ✅ Remplace gpt-4 par gpt-3.5-turbo ici
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.8,
                    max_tokens=300
                )
                story = response.choices[0].message.content.strip()
                st.markdown("### ✨ Your Story")
                st.markdown(story)
            except Exception as e:
                st.error(f"Something went wrong: {e}")

