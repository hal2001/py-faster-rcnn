

class unrealcv(imdb):
    def __init__(self, gamename, classes):
        imdb.__init__(self, gamename)

        self._data_path = ''
        self._classes = classes

        assert os.path.exists(self._data_path), 'UnrealCV images do not exist: {}'.format(self._data_path)

    def image_path_at(self, i):
        pass

    def image_path_from_index(self, index):
        ''' What is the difference between i and index?
        return absolute path??
        '''
        pass

    def gt_roidb(self):
        """
        Return the database of ground-truth regions of interest.

        This function loads/saves from/to a cache file to speed up future calls.
        """
        # How to set cache_path?
        cache_file = os.path.join(self.cache_path, self.name + '_gt_roidb.pkl')
        if os.path.exists(cache_file):
            with open(cache_file, 'rb') as fid:
                roidb = cPickle.load(fid)
            print '{} gt roidb loaded from {}'.format(self.name, cache_file)
            return roidb

        gt_roidb = [self._load_unrealcv_annotation(index)
                    for index in self.image_index]
        with open(cache_file, 'wb') as fid:
            cPickle.dump(gt_roidb, fid, cPickle.HIGHEST_PROTOCOL)
        print 'wrote gt roidb to {}'.format(cache_file)

        return gt_roidb

    def _load_unrealcv_annotation(index):
        """
        Load image and bounding boxes
        """
        # TODO: need a way to visualize annotation
        pass


if __name__ == '__main__':
    # Directly use the classes of VOC, because the model is trained using these classes
    classes = ('__background__', # always index 0
                     'aeroplane', 'bicycle', 'bird', 'boat',
                     'bottle', 'bus', 'car', 'cat', 'chair',
                     'cow', 'diningtable', 'dog', 'horse',
                     'motorbike', 'person', 'pottedplant',
                     'sheep', 'sofa', 'train', 'tvmonitor')

    unrealcv('RealisticRendering', classes)
