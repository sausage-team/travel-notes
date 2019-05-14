from logging import getLogger
from base64 import b64encode
from core.bean.wrapper import Wrapper, SUCCESS, FAIL
logger = getLogger(__name__)

class ImageTransfer(object):
  def img2base64(self, img):
    try:
      b64_img = str(b64encode(img.read()), 'utf-8')
    except:
      b64_img = ""
    return b64_img
    