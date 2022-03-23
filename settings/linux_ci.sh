#!/bin/bash

source $HOME/Environments/Py38/bin/activate
export PYENV_HOME=$WORKSPACE/JenkinsPyEnv
echo $PYENV_HOME

if [ -d "$PYENV_HOME"]; then  
    rm -r "$PYENV_HOME"
fi

# Create virtualenv and install necessary packages
python -m venv $PYENV_HOME

# deactivate env required for setting up current env
deactivate

source $PYENV_HOME/bin/activate
python -m pip install --upgrade pip
pip install --quiet nosexcover
pip install --quiet pylint
pip install --quiet pytest
pip install --quiet "numpy==1.18.4"
pip install --quiet pytest-cov
$WORKSPACE/clean_project.sh

if [!-d "$WORKSPACE/junitxml" ]; then 
    mkdir "$WORKSPACE/junitxml"
fi

pytest tests --cov-report=xml:coverage_results/coverage.xml --cov=lib --junitxml=junitxml/test_results.xml
deactivate