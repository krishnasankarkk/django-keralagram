echo "BUILD START"
python3 -m venv .venv
source .venv/bin/activate  
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python -m manage collectstatic --noinput --clear
echo "BUILD END"