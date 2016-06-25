import sys
sys.path.append('./tools/')
import demo
from demo import *

cfg.TEST.HAS_RPN = True  # Use RPN for proposals
prototxt = os.path.join(cfg.MODELS_DIR, NETS['vgg16'][0],
                        'faster_rcnn_alt_opt', 'faster_rcnn_test.pt')
caffemodel = os.path.join(cfg.DATA_DIR, 'faster_rcnn_models',
                            NETS['vgg16'][1])

if not os.path.isfile(caffemodel):
    raise IOError(('{:s} not found.\nDid you run ./data/script/'
                    'fetch_faster_rcnn_models.sh?').format(caffemodel))

caffe.set_mode_cpu()
net = caffe.Net(prototxt, caffemodel, caffe.TEST)

print '\n\nLoaded network {:s}'.format(caffemodel)

# Warmup on a dummy image
im = 128 * np.ones((300, 500, 3), dtype=np.uint8)
for i in xrange(2):
    _, _= im_detect(net, im)

if __name__ == '__main__':
    while 1:
        filename = raw_input('Filename: ')
        if not os.path.isfile(filename):
            print 'File not exist'
            continue
        # filename = './data/demo/000456.jpg'
        demo(net, filename)
        plt.show()
