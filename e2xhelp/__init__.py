import os

def _jupyter_nbextension_paths():
    paths = [
        dict(
            section='tree',
            src=os.path.join('nbextensions', 'help_tab'),
            dest='help_tab',
            require='help_tab/main'
        )
    ]
    return paths

def _jupyter_server_extension_paths():
    paths = [
        dict(module='e2xhelp.server_extensions.help')
    ]
    return paths