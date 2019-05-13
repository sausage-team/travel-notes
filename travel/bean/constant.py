import base64
import os
module_dir = os.path.dirname(__file__)
assets_path = os.path.join(module_dir, 'assets')

class Role(object):
    SYSTEM = 0
    ADMIN = 1
    NORMAL = 2

class ArticleStatus(object):
    BAN = 0
    WAIT = 1
    PASS = 2

defaultIcon = ''
with open(os.path.join(assets_path, 'icon.png'), 'rb') as fin:
    defaultIcon = str(base64.b64encode(fin.read()), 'utf-8')

class Icon(object):
    DEFAULT_ICON = defaultIcon
