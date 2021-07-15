# python.flask.sqlalchemy
A python api template using flask, sqlalchemy

to install dependencies, run ```pipenv install```

to install the postgres driver run ```pipenv run i_pgdriver```

to start the server, run ```pipenv run start``` at the root directory


## vscode settings ##
to gain import intellisense, add the following to either your local or global settings.json

```json
{
  "python.analysis.extraPaths":["app","app/main"]
}
```

make sure to set the python interpreter in the bottom left of vscode to the virtual environment's installation of python.


