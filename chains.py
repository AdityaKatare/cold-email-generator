import os
import pathlib
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

# Load .env file from the app directory
env_path = pathlib.Path(__file__).parent / '.env'
load_dotenv(env_path)

__all__ = ["Chain"]

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            model = 'llama-3.3-70b-versatile',
            temperature = 0,
            max_tokens = None,
            timeout = None,
            max_retries = 2,
            groq_api_key=os.getenv('GROQ_API_KEY'))
    
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            Scraped text from website
            {page_data}
            Instruction:
                The scraped text is from the career's page of a website.
                Your job is to extract the job postings and return them in JSON format containing
                following keys: 'role', 'experience', 'skills' and 'description'.
                Only return in valid JSON format.
            No preamble just JSON
            """
        )

        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke({"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException as exc:
            raise OutputParserException("Context too big. Unable to parse jobs.") from exc
        return res if isinstance(res, list) else [res]
    
    def write_mail(self, job, links):
        email_prompt_template = """
        Job description
        {job_description}

        Instruction:
        Your experience is in the portfolio: {link_list}


Your job is to write a cold email to the company regarding the job mentioned above. Be as convincing as possible
with a natural tone
Do not provide a preamble
email-nopreamble
        """
        
        prompt_email = PromptTemplate.from_template(email_prompt_template)
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content
    
