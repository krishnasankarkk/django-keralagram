echo "BUILD START"
python3 -m venv .venv
./venv/scripts/activate 
python3 -m pip install -r requirements.txt
python3 -m manage collectstatic --noinput --clear
echo "BUILD END"