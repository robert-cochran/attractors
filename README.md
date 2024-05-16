# Attractors

Using the PyGame library to visualise attractors in chaotic systems

![lorrenz gif](./strange-attractors/lorrenz.gif)

## How To Run

### venv
```python3
# uses 'venv' module to create a venv in the venv dir. pip's also copied in.
python3 -m venv venv

# activates virtual environment by editing PATH to first look in venv/bin/
# pip now installs modules to local repo under venv/lib/python3.x/site-packages/
source venv/bin/activate

# modules listed in requirements.txt install to venv
pip --require-virtualenv install --requirement requirements.txt

python3 src/main.py

# deactivates venv and resets PATH back. this (should) work anywhere
deactive
```

### pipx
for auto-managed venv use pipx (installable through brew)


python3 main.py 
python3 main_working.py

##### Related Repo's
- https://github.com/BrutPitt/glChAoS.P
- https://github.com/cimi/many-worlds
- https://github.com/MarioAriasGa/lorenz
- https://www.youtube.com/watch?v=f0lkz2gSsIk&ab_channel=TheCodingTrain
- https://github.com/jonnyhyman/Chaos
- https://github.com/liabru/matter-attractors
- https://github.com/anuraghazra/EvolutionAquerium
