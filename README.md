 crete env
 ```bash
 cada create -n wineq python=3.7
 ```

activate env
```bash
conda activate wineq
```

install requirements.txt
```bash 
pip install -r requirements.txt
```

Download the data from Kaggle
https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009

now push code to github
```bash
git init
git add .
git commit -m "inital commit"
git remote add origin <your git https address>
git branch -M main
git push origin master
```

tox command -
```bash
tox
```
rebuilding
```bash
tox -r
```

pytest
```bash
pytest -v
```
setup commands
```bash
pip install - e.
```

build your own package
```bash
touch setup.py 
python snippet
from setuptools import setup,find_packages
setup(your package details)
```
after building in cli
```bash
python setup.py sdist bdist_wheel
```
the above will build tar.ghz file