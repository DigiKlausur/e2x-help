import os
from tornado import web
from notebook.utils import url_path_join as ujoin
from jupyter_core.paths import jupyter_config_path
from traitlets.config.loader import PyFileConfigLoader
from traitlets.config import LoggingConfigurable, Config
from traitlets import Unicode, Bool
from textwrap import dedent

class Help(LoggingConfigurable):

    static_path = Unicode(os.path.join(os.path.dirname(__file__), 'static'), 
        help='path to static files shipped with package'
    )

    shared_path = Unicode(None, 
        help='path to extra files served under /e2xhelp/shared',
        allow_none=True
    ).tag(config=True)

    def __init__(self):
        self.config = self.load_config('e2xhelp_config.py')

    def load_config(self, config_name):
        cfg = Config()
        for path in jupyter_config_path():
            file = os.path.join(path, config_name)
            if os.path.isfile(file):
                new_cfg = PyFileConfigLoader(file).load_config()
                cfg.merge(new_cfg)
        return cfg

    def get_handlers(self):
        handlers = [
            (r"/e2xhelp/base/(.*)", web.StaticFileHandler, {
                'path': self.static_path, 
                'default_filename': 'index.html'
            })
        ]
        if self.shared_path:
            handlers.append(
                (r"/e2xhelp/shared/(.*)", web.StaticFileHandler, {
                    'path': self.shared_path, 
                    'default_filename': 'index.html'
                })
            )
        return handlers

def init_handlers(webapp):
    h = Help().get_handlers()

    def rewrite(x):
        pat = ujoin(webapp.settings['base_url'], x[0].lstrip('/'))
        return (pat, ) + x[1:]

    webapp.add_handlers('.*$', [rewrite(x) for x in h])

def load_jupyter_server_extension(nbapp):
    webapp = nbapp.web_app
    init_handlers(webapp)