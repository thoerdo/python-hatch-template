# Learning Python packaging

## To be run before every commit

1)  Run *pytest* to ensure all tests are properly executed

    ```bash
    (.venv): python -m pytest
    ```

2)  Check *pytest* coverage

    ```bash
    (.venv): python -m <package-name> --cov=arithmetic tests
    ```

    Should by 100%, ensuring all source code is tests

3) Check *pre-commit' hooks

    ```bash
    (.venv): pre-commit run --all-files
    ```

    After that make sure to check for changes which might have to be added to git staging area

## Setup

1) Create a virtual Python environment and activate it

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2) Make sure you are using the Python app of thevirtual Python environment

    ```bash
    (.venv): which python3
    ```

    Should be something like `~/.venv/bin/python3`

3) Install the required Python libraries to manage the package

    ```bash
    (.venv): python -m pip install -r requirements.txt
    ```

4) Install 'pre-commit'

    ```bash
    (.venv): pre-commit install

    ```
