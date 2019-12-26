## Calculate the anchors of Yolo-format annotations
+ usage
```
/# set paramters in kmeans_anchors.py
# label path
labels_txt = "./labels/"
# 聚类的数目，6或者9
CLUSTERS = 6
# 模型中图像的输入尺寸，默认是一样的, from cfg file
SIZE = 608


/# then run the script
python kmeans_anchors.py

/# It will give you the result like this
label count: 1946
[[0.05572917 0.1962963 ]
 [0.103125   0.15277778]
 [0.13072917 0.0875    ]
 [0.07864583 0.29166667]
 [0.040625   0.18055556]
 [0.0484375  0.10416667]]
Accuracy: 75.28%
33,119,62,92,79,53,47,177,24,109,29,63
-------------------------------------
Boxes:
 [33.88333333 62.7        79.48333333 47.81666667 24.7        29.45      ]-[119.34814815  92.88888889  53.2        177.33333333 109.77777778
  63.33333333]
Ratios:
 [0.22, 0.27, 0.28, 0.46, 0.68, 1.49]


```
