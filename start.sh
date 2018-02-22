cd "$(dirname "$0")"
make venv
source local_env.sh
TOKEN=`cat TOKEN` python app.py
