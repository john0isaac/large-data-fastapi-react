# large data fastapi react

A simple example of a FastAPI backend with a React frontend that can handle large data.

## Installation

- Create a virtual environment

    ```bash
    python3 -m venv .venv
    ```

- Activate the virtual environment

    ```bash
    # On Unix or MacOS
    source .venv/bin/activate

    # On Windows
    .venv\Scripts\activate
    ```

- Install the development dependencies

    ```bash
    pip install -e 'src[dev]'
    ```

- Run the FastAPI backend

    ```bash
    uvicorn src.large_data_api.main:create_app --factory --reload
    ```
