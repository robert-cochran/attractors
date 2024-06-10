
## WASM Compile
NOTE: not working

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
