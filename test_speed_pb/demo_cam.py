# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf
from PIL import Image
import time
import cv2

import yolo_v3
import yolo_v3_tiny

from utils import load_coco_names, draw_boxes, get_boxes_and_inputs, get_boxes_and_inputs_pb, non_max_suppression, \
                  load_graph, letter_box_image
from config import FLAGS

def main(argv=None):
    ## gpu setting
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=FLAGS.gpu_memory_fraction)
    config = tf.ConfigProto(
        gpu_options=gpu_options,
        log_device_placement=False,
    )

    classes = load_coco_names(FLAGS.class_names)

    ## read camera
    cap = cv2.VideoCapture(FLAGS.cam_id)

    # Get the video writer initialized to save the output video
    # if (not args.image):
    #     vid_writer = cv.VideoWriter(outputFile, cv.VideoWriter_fourcc('M','J','P','G'), 30, (round(cap.get(cv.CAP_PROP_FRAME_WIDTH)),round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))))

    t0 = time.time()
    frozenGraph = load_graph(FLAGS.frozen_model)
    print("[INFO] #### Loaded graph in {:.2f}s".format(time.time()-t0))

    boxes, inputs = get_boxes_and_inputs_pb(frozenGraph)

    with tf.Session(graph=frozenGraph, config=config) as sess:
        while True:
            # get frame from the video
            hasFrame, img = cap.read()
            print("hasFrame  --- {}".format(hasFrame))

            # Stop the program if reached end of video
            if not hasFrame:
                print("Done processing !!!")
                # Release device
                cap.release()
                break

            img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            img_resized = letter_box_image(img, FLAGS.size, FLAGS.size, 128)
            img_resized = img_resized.astype(np.float32)
            print('[INFO] #### img_resized channle : {}'.format(img_resized.shape))


            t0 = time.time()
            detected_boxes = sess.run(
                boxes, feed_dict={inputs: [img_resized]})
            print('[INFO] #### Model session run in {} seconds'.format(time.time() - t0))

            # postprogress
            filtered_boxes = non_max_suppression(detected_boxes,
                                                 confidence_threshold=FLAGS.conf_threshold,
                                                 iou_threshold=FLAGS.iou_threshold)
            print("[INFO] #### Predictions found in {:.2f}s".format(time.time() - t0))

            draw_boxes(filtered_boxes, img, classes, (FLAGS.size, FLAGS.size), True)

            img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
            # img.save(FLAGS.output_img)
            cv2.imshow('winName', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    tf.app.run()
