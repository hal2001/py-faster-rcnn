import sys, os
sys.path.append('tools')
import demo as D
import numpy as np
import matplotlib.pyplot as plt
net = None

# Initialize caffe
prototxt = os.path.join(D.cfg.MODELS_DIR, D.NETS['vgg16'][0],
                        'faster_rcnn_alt_opt', 'faster_rcnn_test.pt')
caffemodel = os.path.join(D.cfg.DATA_DIR, 'faster_rcnn_models',
                            D.NETS['vgg16'][1])

gpu_id = 0
D.caffe.set_mode_gpu()
D.caffe.set_device(gpu_id)
D.cfg.GPU_ID = gpu_id
D.cfg.TEST.HAS_RPN = True
net = D.caffe.Net(prototxt, caffemodel, D.caffe.TEST)
# Warmup on a dummy image
im = 128 * np.ones((300, 500, 3), dtype=np.uint8)
for i in xrange(2):
    _, _= D.im_detect(net, im)

im = plt.imread('./000456.jpg')
D.im_detect(net, im)
