
# installer folder venv

1/python -m venv venv

venv\Scripts\Activate.ps1   




# open venv 

2/   python -m venv venv           





# install requirements 

3/  python -m pip install --upgrade pip

python -m pip install -r reqiurements.txt





# Recreate model artifacts inside this environment
This ensures binary-compatibility with NumPy/pandas/scikit-learn used here.

4/  python .\recreate_pickles.py





# executer l'application

5/streamlit run .\app.py   
