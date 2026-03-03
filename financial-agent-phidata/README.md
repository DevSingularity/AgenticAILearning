# Financial Agent using Phidata

## Folder Structure:

- financial_agent.py: conatins the level 1 of the agent
- main.py: contains the level 2 of the agent with efficient use of tokens and proper structure, but is accessible from cli using the following command.
    ```powershell
    python main.py
    ```
- playground.py: uses phidata's playground interface
    - Go to phidata website and login, insert your api keys and set it using `setx your-key` in cmd.
    - Then run file in cli `python playground.py` and set the localhost url `localhost:7777` in phidata.
    - Enjoy

## Setup:

- Create an env:

    ```powershell
    python -m venv .venv
    ```
- Activate the env:

    ```powershell
    .\.venv\Scripts\activate
    ```
- Installing the requirements:

    ```powershell
    pip install -r requirements.txt
    ```
