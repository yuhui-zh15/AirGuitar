# AirGuitar
## Introduction
AirGuitar = guitar + leap

## Documentation
Can be found at [AirGuitar Doc](https://yuhui-zh15.github.io/AirGuitar/).

## Setup
### Python and Leap Motion SDK
Python2.7 is required.

1. Download [LeapSDK v2.3.1](https://developer.leapmotion.com/sdk/v2) and add `lib` folder to python path.

```bash
export PYTHONPATH=$PYTHONPATH:<path/to/LeapSDK/lib>
# Do this everytime when you open a terminal or add this line to ~/.profile
```

2. Add the project root path to python2 sys.path, for example, on unix:

```bash
export PYTHONPATH=$PYTHONPATH:<path/to/AirGuitar>
```

Now you should import Leap and the AirGuitar modulesproperly.

```python
import Leap
import sound
```

If not, inspect your sys.path to see if the `AirGuitar` and `LeapSDK/lib` folder is included.

```python
import sys
print(sys.path)
```

### fluidsynth and mingus
To produce musical instrument sounds in python, we need the [FluidSynth library](https://github.com/FluidSynth/fluidsynth) and a python package named mingus.
1. Install fluidsynth by yourself. This step is necessary.
2. Install python packages.

```bash
cd <path/to/AirGuitar>
pip install -r requirements.txt
```

3. Pull the SoundFont file to get the instruments. If you cannot connect to dropbox for some reason, please open `raw/pull.sh` and download the file by hand and put it under `raw/`.

```bash
cd raw/
bash pull.sh
```

4. Finally you can play sounds with python.

```python
from mingus.midi import fluidsynth
fluidsynth.init('raw/FluidR3_GM.sf2')
fluidsynth.play_Note(60)
```

