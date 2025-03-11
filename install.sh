cd RedditChessBot || exit

echo "Updating the server..."
sudo apt-get update -y

echo "Installing pip..."
sudo apt install python3-pip -y

echo "Installing python3-venv..."
sudo apt-get install python3-venv -y

echo "Installing Git LFS..."
sudo apt-get install -y git-lfs
git lfs install

echo "Pulling objects using Git LFS..."
git lfs pull

#Check if the virtual environment exists. If not, create it.
if [ ! -d ".venv" ]; then
    echo "Creating a new virtual environment..."
    python3 -m venv .venv
else
    echo "Virtual environment already exists. Skipping creation."
fi

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirements.txt

cd ..
echo "Setup complete..."




