# LLM-Apps

Welcome to LLM-Apps, a collection of applications which leverage the power of the OpenAI language model, Langchain, Chainlit, and other tools for various tasks. Below, you'll find a brief overview of each app:

## 1. Research Agent (research_agent.py)

The Research Agent is an app for conducting research, utilizing OpenAI API, Langchain, and Chainlit. It makes use of tools such as "arxiv" and "llm-math" to assist you in your research endeavors. Acting as a virtual research assistant, this app simplifies the process of gathering information from diverse sources.

## 2. YouTube Search Agent (my_youtube_search.py)

The YouTube Search Agent is designed to simplify your video discovery process. Powered by OpenAI API and Langchain, specifically the YouTubeSearchTool, this app allows you to search for YouTube videos based on a given topic. Input your desired topic, and let the agent fetch relevant videos for you.

## 3. Document Question Answering (documents_qa.py)

The Document Question Answering is an app for interacting with textual content. It leverages the OpenAI language model, Langchain RetrievalQAWithSourcesChain, Chainlit, and the Chroma vector store for efficient document retrieval. This app provides an interactive environment where users can upload files, ask questions related to the content of those files, and receive detailed answers along with source information.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/tjdharani/LLM-Apps.git
   ```

2. Navigate to the project directory:

   ```bash
   cd LLM-Apps
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Set up your OpenAI API key:

   - Create a file named `apikey.py` in the root directory.
   - Inside `apikey.py`, define a variable named `OPENAI_API_KEY` and set it to your OpenAI API key:

     ```python
     OPENAI_API_KEY = 'your-api-key'
     ```

## Usage

Now that you have the repository installed and the OpenAI API key set up, you can explore and use the applications:

### Research Agent (research_agent.py)

Run the following command to start the Research Agent:

```bash
chainlit run research_agent.py
```

### YouTube Search Agent (my_youtube_search.py)

Execute the following command to launch the YouTube Search Agent:

```bash
python my_youtube_search.py
```

### Document Question Answering (documents_qa.py)

To use the Document Question Answering app, run:

```bash
chainlit run documents_qa.py
```

Feel free to experiment with different inputs and explore the capabilities of each application. If you encounter any issues or have suggestions, don't hesitate to reach out.

Happy coding! 🚀
