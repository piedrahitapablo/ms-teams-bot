# Melt template for Python API's

Template repository for Python API's using [fastapi](https://fastapi.tiangolo.com/)

## How to use

1. Click on the top right `+` button on GitHub
1. Select `New repository`
1. On Repository template select `MeltStudio/melt-python-api-template`
1. Create the new repository
1. Open [`setup.py`](setup.py) and edit the fields with the
   `__CHANGE__` value
1. Run `pipenv install --dev`
1. Run `pipenv run install-git-hooks` to install all the git hooks
1. Run `pipenv run start` to check that everything is running as expected
1. Start developing!

## Scripts

This template includes some basic `pipenv` scripts:

- **`install-git-hooks`:** Installs all the git hooks from [`pre-commit`](https://pre-commit.com/)
- **`start`:** Starts a development server using [`uvicorn`](https://www.uvicorn.org/)
- **`test`:** Runs tests using [`pytest`](https://docs.pytest.org)
- **`type-check`:** Runs [`mypy`](https://mypy.readthedocs.io) to check the type
  annotations

## VS Code configuration

To enable autocompletion, formatting and linting:

1. Install the [VS code extension for python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
1. Add the following settings:

   ```json
   {
     "python.formatting.provider": "black",
     "python.linting.flake8Enabled": true,
     "python.linting.flake8Path": "<VIRTUAL_ENV_PATH>/bin/flake8helled",
     "python.linting.mypyEnabled": true,
     "python.linting.pylintEnabled": false,
     "python.pythonPath": "<VIRTUAL_ENV_PATH>/bin/python"
   }
   ```

   To get the value for `<VIRTUAL_ENV_PATH>`, run:

   ```
   $ pipenv --venv
   ```

## TODO

- Add basic flow for GitHub actions
- Add checks on GitHub config for branches
- Add `semantic-release`
- Add a code quality tool
