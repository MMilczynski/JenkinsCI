CALL %USERPROFILE%\Py37Env\Scripts\activate.bat
ECHO "activated"
SET WORKSPACE=%USERPROFILE%\.jenkins\workspace\SimplePythonProject
SET PYENV_HOME=%WORKSPACE%\JenkinsPyEnv
ECHO %PYENV_HOME%

IF EXIST "%PYENV_HOME%" ( 
    RMDIR "%PYENV_HOME%" /s /q
)

:: Create virtualenv and install necessary packages
python -m venv %PYENV_HOME%

:: deactivate env required for setting up current env
TIMEOUT /T 10
CALL %USERPROFILE%\Py37Env\Scripts\deactivate.bat

CALL %PYENV_HOME%/Scripts/activate.bat
:: pip install --quiet nosexcover
:: pip install --quiet pylint
:: pip install --quiet pytest
:: pip install --quiet numpy
:: pytest tests