import _init_paths
from fast_rcnn.test import test_net
from fast_rcnn.config import cfg, cfg_from_file, cfg_from_list, get_output_dir
from datasets.factory import get_imdb
import caffe
import time, os, sys, pprint, cPickle

cfg_file = './experiments/cfgs/faster_rcnn_alt_opt.yml'
cfg_from_file(cfg_file)
cfg.GPU_ID = 0

max_per_image = 100
vis = False

print('Using config:')
pprint.pprint(cfg)

caffemodel = 'data/faster_rcnn_models/VGG16_faster_rcnn_final.caffemodel'

wait = 1
while not os.path.exists(caffemodel) and wait:
    print('Waiting for {} to exist...'.format(args.caffemodel))
    time.sleep(10)


caffe.set_mode_gpu()
caffe.set_device(cfg.GPU_ID)
prototxt = 'models/pascal_voc/VGG16/faster_rcnn_alt_opt/faster_rcnn_test.pt'

net = caffe.Net(prototxt, caffemodel, caffe.TEST)
net.name = os.path.splitext(os.path.basename(caffemodel))[0]

comp_mode = True # What is this about?

if not cfg.TEST.HAS_RPN:
    imdb.set_proposal_method(cfg.TEST.PROPOSAL_METHOD)

imdb_names = []
el_range = range(0, 61, 30)
az_range = range(90, 271, 45)
for el in el_range:
    for az in az_range:
        imdb_names.append('unrealcv_%d_%d' % (el, az))

# for imdb_name in imdb_names:
#     print imdb_name
#     imdb = get_imdb(imdb_name)
#     imdb.competition_mode(comp_mode)
#     test_net(net, imdb, max_per_image=max_per_image, vis=vis)
#

cls = 'sofa'

table = ''
header = '%9s' % 'el/az' + ''.join(['%9.3f' % az for az in az_range])
table += header + '\n'

for el in el_range:
    row = '%9d' % el
    for az in az_range:
        imdb_name = 'unrealcv_%d_%d' % (el, az)
        imdb = get_imdb(imdb_name)
        imdb.competition_mode(comp_mode)
        output_dir = get_output_dir(imdb, net)
        with open(os.path.join(output_dir, cls + '_pr.pkl')) as f:
            result = cPickle.load(f)
        row += '%9.3f' % result['ap']
    table += row + '\n'

print table
