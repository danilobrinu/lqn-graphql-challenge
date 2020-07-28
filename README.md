# Create dependencies for Development Workflow

```sh
pip-compile -r requirements/develop.in -o requirements.develop
```

```sh
pip install -r requirements.develop
```

# Create dependencies for Production Workflow

```sh
pip-compile -r requirements/production.in -o requirements.production
```

```sh
pip install -r requirements.production
```

> **Note:** if you need to update the pip package use the next command `python -m pip install --upgrade pip`.
> For the first time use `pip install pip-tools`.
