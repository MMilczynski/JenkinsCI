CALL %USERPROFILE%\Py38\Scripts\activate.bat
SET PYENV_HOME=%WORKSPACE%\JenkinsPyEnv
ECHO %PYENV_HOME%

IF EXIST "%PYENV_HOME%" ( 
    RMDIR "%PYENV_HOME%" /s /q
)

:: Create virtualenv and install necessary packages
python -m venv %PYENV_HOME%

:: deactivate env required for setting up current env
CALL %USERPROFILE%\Py37Env\Scripts\deactivate.bat

CALL %PYENV_HOME%/Scripts/activate.bat
python -m pip install --upgrade pip
pip install --quiet nosexcover
pip install --quiet pylint
pip install --quiet pytest
pip install --quiet "numpy==1.18.4"
pip install --quiet pytest-cov
CALL %WORKSPACE%\clean_project.bat

IF NOT EXIST "%WORKSPACE%\junitxml\" ( 
    MKDIR "%WORKSPACE%\junitxml"
) 

pytest tests --cov-report=xml:coverage_results\coverage.xml --cov=lib --junitxml=junitxml\test_results.xml
CALL %PYENV_HOME%/Scripts/deactivate.bat