declare -a dirsToRemove=("__pycache__" "build" "dist" "lib\__pycache__" ".pytest_cache" "test_dir")

for dir in ${dirsToRemove[@]}; do
    if [ -d $dir ]; then
	    # remove if directory exists #
	    rm -r $dir
    fi
done
