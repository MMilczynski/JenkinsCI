IF EXIST "__pycache__" (
    RMDIR "__pycache__"
)

IF EXIST "build" (
    RMDIR "build"
) 

IF EXIST "dist" (
    RMDIR "dist"
)

IF EXIST "main.spec" (
    DEL "main.spec"
)

IF EXIST "lib\__pycache__" (
    RMDIR "lib\__pycache__"
)

IF EXIST "tests\__pycache__" (
    RMDIR "tests\__pycache__"
)

IF EXIST ".pytest_cache" (
    RMDIR ".pytest_cache"
)

