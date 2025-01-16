# python_cli_macros

Handy macros that can be called from command line anywhere.

* downloader will empty the most recently downloaded files from %USERPROFILE%/Downloads into the current working directory or a specified path. With optional args -d DESTINATION, -n NUM_FILES -m MKDIR
* zipit can unzip/zip files. when called without arguments it searches for zip files in the cwd and unzips the first one found.
* showdir prints the expanded tree from the cwd or a directory of your choosing. 


once cloned, the parent directory of the repo must be added to %PYTHONPATH% to work anywhere.

reason for repo is to easily sync between personal pc and work pc. I'm sure there'll be more to add.
