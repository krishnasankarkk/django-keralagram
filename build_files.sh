echo "BUILD START"
python3 -m pip install -r requirements.txt
python3 -m manage collectstatic
echo "BUILD END"