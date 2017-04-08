# StudentIT Roster Uploader
## Description
Uploading the roster can take a very long time if done manually, and it tends to be mistake-prone.
This program is designed to automate the process.

## Prerequisites
* Python 3

## Installation
Execute the following commands. This will only work on Linux.

```
python -m venv env
. env/bin/activate
pip install -r requirements.txt
```

## Usage

```
. env/bin/activate
python -m studentit.roster.cli [command] [arguments]
```

## Tests
From inside the main repository directory run the following commands. This will only work on Linux.

```
export PYTHONPATH=`pwd`
py.test --cov=studentit tests
```

