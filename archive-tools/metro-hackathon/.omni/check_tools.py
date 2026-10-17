try:
    import qrcode; print('qrcode OK')
except ImportError: print('qrcode MISSING')
from PIL import Image; print('PIL OK')
import pptx; print('pptx', pptx.__version__)
