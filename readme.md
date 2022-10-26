# DVC - DL - TF - AIOPS demo

dowmload data --> [source](https://drive.google.com/drive/u/5/folders/1tz4IOoJKdi999IRdqJY04VOifyllRzj1)

## commands -

### create a new env
```bash
conda create --prefix ./env python=3.7 -y
```

### activate new env
```bash
source activate ./env
```

### init DVC & git
```bash
git init
dvc init
```

### create empty files -
```bash
touch readme.md .gitignore setup.py dvc.yaml param.yaml
mkdir -p config src/utils/__init__.py src/__init__.py
touch config/config.yaml config/secrets.yaml
```
