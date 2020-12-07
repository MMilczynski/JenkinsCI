#!/bin/bash
. $USERPROFILE/Py37Env/Scripts/activate.bat
PYENV_HOME=$WORKSPACE/JenkinsPyEnv

# Delete previously built virtualenv
if [ -d $PYENV_HOME ]; then
    rm -rf $PYENV_HOME
fi

# Create virtualenv and install necessary packages
python -m venv $PYENV_HOME

# deactivate env required for setting up current env
. $USERPROFILE/Py37Env/Scripts/deactivate.bat

$PYENV_HOME/Scripts/activate.bat
pip install --quiet nosexcover
pip install --quiet pylint
pip install --quiet pytest
pip install --quiet numpy
pytest