
import tensorflow as tf

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_integer(
    'cam_id', 0, 'camera id')
tf.app.flags.DEFINE_string(
    'class_names', 'dove_14_tenth_voc/yolov3.names', 'File with class names')
tf.app.flags.DEFINE_string(
    'data_format', 'NCHW', 'Data format: NCHW (gpu only) / NHWC')
tf.app.flags.DEFINE_string(
    'frozen_model', 'frozen_yolov3-voc-dove.pb', 'Frozen tensorflow protobuf model')
tf.app.flags.DEFINE_bool(
    'tiny', False, 'Use tiny version of YOLOv3')
tf.app.flags.DEFINE_bool(
    'spp', False, 'Use SPP version of YOLOv3')

tf.app.flags.DEFINE_integer(
    'size', 416, 'Image size')

tf.app.flags.DEFINE_float(
    'conf_threshold', 0.5, 'Confidence threshold')
tf.app.flags.DEFINE_float(
    'iou_threshold', 0.4, 'IoU threshold')

tf.app.flags.DEFINE_float(
    'gpu_memory_fraction', 0.5, 'Gpu memory fraction to use')

