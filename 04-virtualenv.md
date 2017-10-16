# virtualenv a Flask

Na přednášce jsme ukazovali vlastní moduly, jak použít
moduly z PyPI a jak použít virtualenv.

Zkuste se podívat, zdali vůbec kde je na Vašem počítači modul 
[`flask`][flask] a v jaké je verzi a která verze je aktuální.

Pokud modul flask nebude v poslední verzi, nainstalujte ji
do [virtualenv][venv-guide].  Alternativně můžete použít 
i modernější [pipenv][pipenv-guide]. 

## Testovací aplikace

```python
import flask

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask! (flask v.{})".format(flask.__version__)
    
if __name__ == '__main__':
    app.run()
```

[flask]: http://flask.pocoo.org
[venv-guide]: http://docs.python-guide.org/en/latest/dev/virtualenvs/#lower-level-virtualenv
[pipenv-guide]: http://docs.python-guide.org/en/latest/dev/virtualenvs/
