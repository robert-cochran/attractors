# Attractors

Using the PyGame library to visualise strange attractors.

![lorrenz gif](./lorrenz.gif)

For more info and examples see:
- https://en.wikipedia.org/wiki/Attractor
- https://en.wikipedia.org/wiki/Lorenz_system
- https://www.behance.net/gallery/7618879/Strange-Attractors
- http://www.3d-meier.de/tut19/Seite3.html
- http://paulbourke.net/fractals/sprott/
- https://examples.pyviz.org/attractors/attractors.html

## Run Instructions

```bash
# uses 'venv' module to create a venv in the venv dir. pip's also copied in.
python3 -m venv venv

# activates virtual environment by editing PATH to first look in venv/bin/
# pip now installs modules to local repo under venv/lib/python3.x/site-packages/
source venv/bin/activate

# modules listed in requirements.txt install to venv
pip --require-virtualenv install --requirement requirements.txt

# to manually install a new module later
pip --require-virtualenv install <module_name>

python3 src/main.py

# deactivates venv and resets PATH back. this (should) work anywhere
deactive
```

NOTE: for auto-managed venv use pipx (installable through brew)

## WASM Compile

```bash
# Uses py2wasm (see: https://news.ycombinator.com/item?id=40114567)
# NOTE: if py2wasm requires a specific version of python then
# - brew install specific python version (e.g. brew install python@3.11),
# - create the venv with the binary of that python version 
#   (e.g /opt/homebrew/Cellar/python@3.11/3.11.9/bin/python3.11 -m venv venv)

pip install py2wasm
py2wasm src/main.py -o wasm/main.wasm
brew install wasmer
wasmer run myprogram.wasm
```

##### Related Repo's
- https://github.com/BrutPitt/glChAoS.P
- https://github.com/cimi/many-worlds
- https://github.com/MarioAriasGa/lorenz
- https://www.youtube.com/watch?v=f0lkz2gSsIk&ab_channel=TheCodingTrain
- https://github.com/jonnyhyman/Chaos
- https://github.com/liabru/matter-attractors
- https://github.com/anuraghazra/EvolutionAquerium
