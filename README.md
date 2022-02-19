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