# e2x-help

Jupyter Notebook server extension that serves static files such as documentation files.

## Base files 

The basic e2x help in English and German is served under ```/e2xhelp/base/html/en``` and ```/e2xhelp/base/html/de```.

## Shared files

By creating the config ```e2xhelp_config.py``` under ```/share/e2xhelp/``` you can serve additonal files.
These files will be served under ```/e2xhelp/shared/```.

Example config:

```
# ex2help_config.py

c = get_config()

# Make sure the shared path is added to the app
c.Help.use_shared_path = True
# Specifiy the path to your extra files
c.Help.shared_path = '/srv/shared_dir'
```
