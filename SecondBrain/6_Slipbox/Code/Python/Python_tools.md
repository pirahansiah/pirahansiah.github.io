tags:
    - flake8
    - black
    - poetry
    - hooks
    - 

```py
docker run helm chart
```

problem with multiple related package in pip which one require another one. also, versioning. we can create environment based on the folder and each folder of source have won virtual environment . everything automatically pip install -r requirement.txt work from end of file so you manually must care about requirement

pyenv

pyenv install

pyenv install 3.7.5

cd folder

pyenv global 3.7.5

pyenv versions

python -> you can see this environments

poetry install (pyproject.toml) ~/.bash , .bash_profile , .zshrc

poetry run which python

poetry run jupyter lab

pipenv install requests

pyenv virtualenvs cv-endpoint

pyenv activate cv-endpoint

====================

black python [https://github.com/psf/black](https://www.google.com/url?q=https%3A%2F%2Fgithub.com%2Fpsf%2Fblack&sa=D&sntz=1&usg=AOvVaw2DSvjHmDvdtitO_AhjC1o1)

The Uncompromising Code Formatter

pip install black

====================

pre-commit A framework for managing and maintaining multi-language pre-commit hooks.

pip install pre-commit

brew install pre-commit

.pre-commit-config.yaml

repos:

- repo: [https://github.com/asottile/reorder_python_imports](https://www.google.com/url?q=https%3A%2F%2Fgithub.com%2Fasottile%2Freorder_python_imports&sa=D&sntz=1&usg=AOvVaw1gALoCbTPR6O-CSgrx7r5R)

rev: v1.8.0

hooks:

- id: reorder-python-imports

exclude: notebooks/

language_version: python3.7

- repo: [https://github.com/ambv/black](https://www.google.com/url?q=https%3A%2F%2Fgithub.com%2Fambv%2Fblack&sa=D&sntz=1&usg=AOvVaw0k7gFGFzE6MyOzqjVo8Jto)

rev: 19.10b0

hooks:

- id: black

exclude: notebooks/

language_version: python3.7

- repo: [https://github.com/pre-commit/pre-commit-hooks](https://www.google.com/url?q=https%3A%2F%2Fgithub.com%2Fpre-commit%2Fpre-commit-hooks&sa=D&sntz=1&usg=AOvVaw3OA6YG1PaCw-Mf9zuTPohi)

rev: v2.4.0

hooks:

- id: flake8

args: ['--ignore=E203,E266,E501,W503', '--max-line-length=88', '--max-complexity=15', '--select=B,C,E,F,W,T4,B9']

exclude: notebooks/

language_version: python3.7

pre-commit install

pre-commit run --all-files

git

make file

make check

code .

```

