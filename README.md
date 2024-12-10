# Learning Python packaging

## To be run before every commit

1)  Run *tox* to ensure all tests, lintings etc. are properly executed and Sphinx docs are build

    ```bash
    (.venv): tox
    ```

### Recommended: Run after staging your changes

1) Check *pre-commit' hooks

    ```bash
    (.venv): git add <files to add to staging area>
    (.venv): pre-commit run --all-files
    ```

    After that make sure to check for changes which might have to be added to git staging area

## Build the project

1) Build the project in *development mode*

    ```bash
    (.venv): python3 -m pip install -e .
    ```

2) Build the release package

    ```bash
    (.venv): python3 -m build
    ```

## Initial setup

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
