# Cold Email Generator

This project is a Streamlit web application that scrapes job postings from a given URL, analyzes the content using an LLM (via Groq API), and generates personalized cold emails for job applications based on your portfolio.

## Features

- **Web Scraping:** Enter a URL to a careers page and extract job postings automatically.
- **LLM Integration:** Uses Groq's Llama-3 model for job extraction and email generation.
- **Portfolio Matching:** Matches your skills/tech stack from a CSV portfolio to relevant job postings.
- **Cold Email Generation:** Automatically writes convincing cold emails tailored to each job.

## Project Structure

```
.
├── __init__.py
├── .env
├── .gitignore
├── chains.py
├── main.py
├── portfolio.py
├── utils.py
└── resource/
    └── portfolio.csv
```

- [`main.py`](main.py): Streamlit app entry point.
- [`chains.py`](chains.py): LLM prompt chains for job extraction and email writing.
- [`portfolio.py`](portfolio.py): Portfolio management and vector search.
- [`utils.py`](utils.py): Utility functions (e.g., text cleaning).
- [`resource/portfolio.csv`](resource/portfolio.csv): Your tech stack and links (CSV format).

## Setup

1. **Clone the repository**

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory with your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Prepare your portfolio**

   Edit `resource/portfolio.csv` to include your tech stack and relevant links.

## Running the App

```sh
streamlit run main.py
```

## Usage

1. Open the Streamlit app in your browser.
2. Enter the URL of a careers or jobs page.
3. The app will extract job postings, match your skills, and generate cold emails for you to use.


---

**APIs required!!!** This project uses [LangChain](https://github.com/langchain-ai/langchain), [Streamlit](https://streamlit.io/),and [Groq API](https://groq.com/).
