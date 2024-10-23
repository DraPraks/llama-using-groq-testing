import streamlit as st
from langchain_community.document_loaders import WebBaseLoader


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("Mail Gen")
    url_input = st.text_input("Enter a URL:", value="https://boards.greenhouse.io/spacex/jobs/7514164002?gh_jid=7514164002")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


# if __name__ == "__main__":
    # chain = Chain()
    # portfolio = Portfolio()
    # st.set_page_config(layout="wide", page_title="Mail Gen", page_icon="📧")
    # create_streamlit_app(chain, portfolio, clean_text)

