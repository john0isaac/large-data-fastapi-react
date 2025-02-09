# large data fastapi react

A simple example of a FastAPI backend with a React frontend that can handle large data.

![Screenshot of the App](https://github.com/user-attachments/assets/3134f59a-8657-4455-bdba-f49e9e152dfc)

## Installation

1. Create a virtual environment

    ```bash
    python3 -m venv .venv
    ```

1. Activate the virtual environment

    ```bash
    # On Unix or MacOS
    source .venv/bin/activate

    # On Windows
    .venv\Scripts\activate
    ```

1. Install the development dependencies

    ```bash
    pip install -e 'src[dev]'
    ```

1. Run the FastAPI backend

    ```bash
    uvicorn src.large_data_api.main:create_app --factory --reload
    ```

1. Install the frontend dependencies

    ```bash
    cd frontend
    yarn install
    ```

1. Run the React frontend

    ```bash
    yarn start
    ```
