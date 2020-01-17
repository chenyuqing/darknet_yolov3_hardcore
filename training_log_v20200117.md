备注：数据备份在移动硬盘的路径： /media/ares2/ext_disk/0000_dove_dataset_bak
```
-0000_dove_dataset_bak
|-train
|-val
|-test
```
## 数据的改动(8th training)

### 统计样本分布的脚本：compute-labels-name.py
- 使用方法
```
1. 新建一个tmp临时文件夹，然后依次从train,val,test中复制需要的图片文件进去，然后执行以下命令以获得train,val,test中所有图片的路径
find `pwd`/ -name "*jpg" > train8.txt
find `pwd`/ -name "*jpg" > val8.txt
find `pwd`/ -name "*jpg" > test8.txt

2. 把compute-labels-name.py跟train8.txt,val8.txt,test8.txt放一起
vi compute-labels-name.py，修改如下：
train_filename =  "train8.txt"
val_filename = "val8.txt"
test_filename = "test8.txt"
执行脚本，python compute-labels-name.py
输出如下：
train8 :
all picture is  3100 (图片数量)
label0 = 981 (bbx 数量)
label1 = 1015
label2 = 1003
label3 = 462
label4 = 419
label5 = 880
label6 = 1137
label7 = 872
label8 = 496
label9 = 826
label10 = 858
label11 = 872
label12 = 476
label13 = 438
label14 = 0

val8 :
all picture is  2100
label0 = 320
label1 = 329
label2 = 362
label3 = 463
label4 = 426
label5 = 352
label6 = 369
label7 = 396
label8 = 468
label9 = 376
label10 = 275
label11 = 337
label12 = 492
label13 = 453
label14 = 0

test8 :
all picture is  2063
label0 = 311
label1 = 320
label2 = 326
label3 = 469
label4 = 391
label5 = 342
label6 = 339
label7 = 371
label8 = 388
label9 = 357
label10 = 321
label11 = 346
label12 = 378
label13 = 396
label14 = 0

```
### 训练数据
- training data: train/dove14_fifth_before_after-img100 + train/dove14-fifth-train-data-img100 + train/dove14-fifth-train-data-img200 + train/label3_4_8_12_13_train_img500
- 训练数据bbx分布图

### 验证数据
- val data: val/dove14_fifth_before_after_img200 + val/dove14_fifth_before_after_img500 + val/label3_4_8_12_13_val_img500

### 测试数据
- test data: test/dove14_fifth_before_after_img300 + test/dove14_fifth_before_after_img400 + test/dove14_fifth_before_after_label3481213_img500

## 训练过程
- 训练前准备.data, .cfg, .names, .weights 
```

```

## 训练结果

## 总结

