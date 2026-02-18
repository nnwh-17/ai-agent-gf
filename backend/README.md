# Setup
cd backend
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt

# Health Check
fastapi dev main.py
