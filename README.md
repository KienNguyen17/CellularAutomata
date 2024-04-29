# CellularAutomata
Author: Kien Nguyen, Justin Chalichemala, Malcolm Rousseau
## Installation
After cloning the repo, change directory into src
```
cd src
```

Create and activate a virtual environment .venv

- for Windows
```
python -m venv .venv
.venv\Scripts\activate 
```

- for MacOS
```
python3 -m venv .venv
source .venv/bin/activate 
```

Install the required packages in requirements.txt by running the following line in terminal
```
pip3 install -r requirements.txt
```

If the installation does not work, just ensure you have matplotlib installed.

## Usage
You can now run the automata.py file to generate the automata, changing the variable HEIGHT to the desired number of layers, and commenting either the animation or image code.

automata.gif is a gif animation of 128 layers of cellular automata.