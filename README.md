# intelli-agent-rag

#Local Run
    ## Cloning the repository
    ```
        git clone https://github.com/debdutta-chatterjee/intelli-agent-rag.git
    ```
    ## Create venv
    ```
        python -m venv .venv
    ```
    ## Install dependencies
    ```
        pip install -r requirements.txt
    ```
    ## Start app
    ```
        uvicorn main:app --reload
    ```
    ## Build image
    ```
        docker build -t intelli-agent .
        docker run -p 8000:8000 intelli-agent
    ```