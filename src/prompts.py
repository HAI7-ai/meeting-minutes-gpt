""" A python file to define prompts for various tasks with GPT models"""
from langchain.prompts import PromptTemplate

def summarize_text(text_input: str, word_limit: int=250):    
    """A prompt template to summarize the given text content."""
    delimitter = "####"
    system_message = f"""You are an helpful assistant and follows given instructions. \
        Summarize the text content provided in between {delimitter} characters. \
        Summarized content should be not more than {word_limit} words. \
        Summarized content must has key points present in the provided text.
        """
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"{delimitter}{text_input}{delimitter}"},
        {"role": "assistant", "content": "Helpful Summarized content:\n"}
    ]

    return messages

def prompt_doc_qa():
    """A prompt template to define a prompt template for Question and Answering of a document."""

    template = """Use the following pieces of context and answer the question at the end. \
        If you don't know the answer, just say you don't know. \
        Do not try to make up an answer. \
        Follow the query instructions carefully while answering the query. \
        Use maximum of ten to fifteen sentences if user does not provide any limitation on completion length. \
        Keep the answer concise as possible and should be helpful. \
        Answer should not contain any harmful language. \
        Context: {context} \
        Question: {question} \
        Helpful Answer: \
        """
    
    qa_chain_prompt = PromptTemplate(input_variables=["context", "question"],template=template)

    return qa_chain_prompt