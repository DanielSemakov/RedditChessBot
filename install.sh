cd ~/RedditChessBot || { echo "Project folder not found"; exit 1; }

echo "Updating the server..."
sudo apt-get update -y
sudo apt-get upgrade -y

echo "Installing required packages..."
sudo apt-get install -y python3-pip python3-venv git git-lfs
git lfs install

echo "Pulling Git LFS objects..."
git lfs pull || echo "Git LFS pull failed or not needed"

# Create virtual environment if missing
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setup complete. To run your bot:"
echo "source .venv/bin/activate && python bot.py"



