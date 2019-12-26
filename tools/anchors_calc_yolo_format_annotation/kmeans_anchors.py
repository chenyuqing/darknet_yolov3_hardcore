# -*- coding=utf-8 -*-
import glob
import os
import sys
import xml.etree.ElementTree as ET
import numpy as np
from kmeans import kmeans, avg_iou

# label path
labels_txt = "./labels/"
# 聚类的数目
CLUSTERS = 6
# 模型中图像的输入尺寸，默认是一样的, from cfg file
SIZE = 608

# 加载YOLO格式的标注数据
def load_dataset(labels_txt):
    if not os.path.exists(labels_txt):
        print('no labels folders, program abort')
        sys.exit(0)

    label_file = os.listdir(labels_txt)
    print('label count: {}'.format(len(label_file)))
    dataset = []

    for label in label_file:
        with open(os.path.join(labels_txt, label), 'r') as f:
            txt_content = f.readlines()

        for line in txt_content:
            line_split = line.split(' ')
            roi_with = float(line_split[len(line_split)-2])
            roi_height = float(line_split[len(line_split)-1])
            if roi_with == 0 or roi_height == 0:
                continue
            dataset.append([roi_with, roi_height])
            # print([roi_with, roi_height])

    return np.array(dataset)

data = load_dataset(labels_txt)
out = kmeans(data, k=CLUSTERS)
kmeans_anchors = ""
print(out)
print("Accuracy: {:.2f}%".format(avg_iou(data, out) * 100))

for x, y in zip(out[:, 0], out[:, 1]):
    kmeans_anchors += str(int(x*SIZE))+","+str(int(y*SIZE)) + ","


print(kmeans_anchors[:-1])
print('-------------------------------------')
print("Boxes:\n {}-{}".format(out[:, 0] * SIZE, out[:, 1] * SIZE))

ratios = np.around(out[:, 0] / out[:, 1], decimals=2).tolist()
print("Ratios:\n {}".format(sorted(ratios)))

