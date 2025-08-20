import sys, pathlib
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader


PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:  
    from app.chains import Chain  
    from app.portfolio import Portfolio  
    from app.utils import clean_text  
except ImportError:  
    from chains import Chain  
    from portfolio import Portfolio  
    from utils import clean_text  

st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")

def create_streamlit_app(chain: Chain, portfolio: Portfolio):
    st.title('Cold Email Generator')
    url_input = st.text_input('Enter a URL:')
    if st.button('Submit'):
        raw_url = (url_input or '').strip()
        if not raw_url:
            st.warning('Please enter a URL.')
            return
        try:
            with st.spinner('Loading and analyzing page...'):
                loader = WebBaseLoader(raw_url)
                docs = loader.load()
                if not docs:
                    st.error('No content retrieved from that URL.')
                    return
                data = clean_text(docs[0].page_content)
                portfolio.load_portfolio()
                jobs = chain.extract_jobs(data)
                if not jobs:
                    st.info('No jobs/opportunities detected on that page.')
                    return
                for job in jobs:
                    skills = job.get('skills', [])
                    links = portfolio.query_links(skills)
                    email = chain.write_mail(job, links)
                    st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio)
