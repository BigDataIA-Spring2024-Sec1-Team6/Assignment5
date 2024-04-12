import streamlit as st
from pages import create_summaries, generate_qa, find_answers, use_summaries

# Define the multipage class to manage the multiple apps in our program
class MultiPage:
    def __init__(self):
        self.pages = []

    def add_page(self, title, func):
        self.pages.append({
            "title": title,
            "function": func
        })

    def run(self):
        page = st.sidebar.selectbox(
            'Select a page:',
            self.pages,
            format_func=lambda page: page['title']
        )
        page['function']()

app = MultiPage()

# Add all your application here
app.add_page("Create Knowledge Summaries", create_summaries.app)
app.add_page("Generate Q/A", generate_qa.app)
app.add_page("Find and Answer Questions", find_answers.app)
app.add_page("Use Knowledge Summaries", use_summaries.app)

# The main app
app.run()