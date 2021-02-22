import os
import json
from tornado import web

from notebook.base.handlers import IPythonHandler

class ListFilesHandler(IPythonHandler):

    def list_files(self, path):
        if path is None:
            return []
        file_list = []
        exclude_dirs = []
        
        for root, dirs, files in os.walk(path):
            root = os.path.relpath(root, path)
            for name in dirs:
                if name.startswith('.'):
                    exclude_dirs.append(name)
                elif os.path.isfile(os.path.join(root, name, 'index.html')):
                    exclude_dirs.append(name)
                    file_list.append((os.path.join(root, name), os.path.join(root, name, 'index.html')))

            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for name in files:
                if name == 'index.html':
                    exclude_dirs.append(dirs)
                file_list.append((os.path.join(root, name), os.path.join(root, name)))
                
        return file_list

    @web.authenticated
    def get(self):
        files = self.list_files(self.settings['e2xhelp_shared_dir'])
        self.write(json.dumps(files))

default_handlers = [
    (r"/e2xhelp/api/files", ListFilesHandler)
]



