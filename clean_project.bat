IF EXIST "__pycache__" (
    RMDIR "__pycache__" /Q /S
)

IF EXIST "build" (
    RMDIR "build" /Q /S
) 

IF EXIST "dist" (
    RMDIR "dist" /Q /S
)

IF EXIST "main.spec" (
    DEL "main.spec"
)

IF EXIST "lib\__pycache__" (
    RMDIR "lib\__pycache__" /Q /S
)

IF EXIST "tests\__pycache__" (
    RMDIR "tests\__pycache__" /Q /S
)

IF EXIST ".pytest_cache" (
    RMDIR ".pytest_cache" /Q /S
)

