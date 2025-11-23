
# 1) Clone the repository
git clone https://github.com/heisenberg0123/Resume-Category-Prediction-App.git
cd "Resume-Category-Prediction-App"

# 2) Create virtual environment
python -m venv venv

# 3) Activate virtual environment
.\venv\Scripts\Activate.ps1

# 4) Upgrade pip
python -m pip install --upgrade pip

# 5) Install dependencies
python -m pip install -r .\reqiurements.txt

# 6) Recreate model pickles (recommended for binary compatibility)
python .\recreate_pickles.py

# 7) Run the Streamlit app
streamlit run .\app.py  
