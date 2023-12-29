# GPT Use Cases
Document Q&A using OpenAI's GPT models. 

To use this application, you must create an API Key with Open AI and configure in the UI. The deployment steps are mentioned below:

1. In your terminal, create an virtual environment and install requirements from requirements file by running following command.
   `python -m pip install -r requirements.txt --no-cache-dir`

2. Run following command from the project root directory to launch the streamlit application.
   `streamlit run frontend/main.py`

3. Browse `http://localhost:8501/` to see the application.

4. Optionally, you can build a docker image and deploy as a container after step 1.

5. To build, docker image, execute following in the project root directory.
    `docker build -t gpt-qna-app .`
    
6. To run, the container, execute the command: `docker run -d -e OPENAI_API_KEY="your-api-key" -p 80:8501 gpt-qna-app`

