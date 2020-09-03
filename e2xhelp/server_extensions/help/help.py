import os
from tornado import web
from notebook.utils import url_path_join as ujoin
from traitlets.config import LoggingConfigurable, Config
from traitlets import Unicode, Bool
from textwrap import dedent
from ...config import ConfigManager

class Help(LoggingConfigurable):

    static_path = Unicode(os.path.join(os.path.dirname(__file__), 'static'), help=dedent(
        'path to static files shipped with package'
    ))

    use_shared_path = Bool(False, help=dedent(
        'Whether to use static files from the shared_path'
    )).tag(config=True)

    shared_path = Unicode('', help=dedent(
        'path to extra files served under /e2xhelp/shared'
    )).tag(config=True)

    def __init__(self):
        self.config = ConfigManager().get_config()

    def get_handlers(self):
        handlers = [
            (r"/e2xhelp/base/(.*)", web.StaticFileHandler, {
                'path': self.static_path, 
                'default_filename': 'index.html'
            })
        ]
        if self.use_shared_path:
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