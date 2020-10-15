# e2x-help

Jupyter Notebook server extension that serves static files such as documentation files.

## Base files 

The basic e2x help in English and German is served under ```/e2xhelp/base/html/en``` and ```/e2xhelp/base/html/de```.

## Shared files

By creating the config ```e2xhelp_config.py``` you can serve additonal files.
These files will be served under ```/e2xhelp/shared/```.
The ```e2xhelp_config.py``` should be located in any of the Jupyter config directories. You can find out which directories these are by executing ```jupyter --paths``` in the terminal and look at the directories under config.

Example config:

```
# ex2help_config.py

c = get_config()

# Specifiy the path to your extra files
c.Help.shared_path = '/srv/shared_dir'
```
