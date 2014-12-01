from django.conf import settings
from django.core.files.storage import Storage
from owncloud import ResponseError

import os
import owncloud


class OwnCloudStorage(Storage):
    def __init__(self, options=None):
        if not options:
            options = settings.OWNCLOUD_STORAGE_OPTIONS

        self.oc = owncloud.Client(options['url'], verify_certs=False)
        self.oc.login(options['user'], options['password'])

    def _open(self, name, mode='rb'):
        self.oc.get_file_contents(name)

    def _save(self, name, content):
        self.oc.put_file_contents(name, content)
        return name

    def exists(self, name):
        try:
            a = self.oc.file_info(name)
            return a.get_name()

        except ResponseError:
            return False

    def delete(self, name):
        try:
            self.oc.delete(name)
            return True

        except ResponseError:
            return False

    def listdir(self, path):
        directories, files = [], []

        for e in self.oc.list(path):
            if e.file_type == 'dir':
                directories.append(os.path.join(path, e.name))
            else:
                files.append(os.path.join(path, e.name))

        return directories, files


    def size(self, name):
        data = self.oc.file_info()
        return data.get_size()

    def url(self, name):
        data = self.oc.share_file_with_link(name)
        return '%s%s' % (data.link, '&download')
