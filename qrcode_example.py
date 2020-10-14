import pyqrcode
big_code = pyqrcode.create('http://www.fanyanlindsay.com', error='L', version=10, mode='binary')
big_code.png('code.png', scale=1, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
big_code.show()
