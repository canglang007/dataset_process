# dataset_process
本仓库内存放针对数据集的处理的一些代码，包括数据集划分，格式转换等

## 常见数据集格式解析

### 目标检测

- YOLO 格式

  所有的图片都在 images 文件夹里，标签在 labels 文件夹里，标签为 txt 格式，每一行包含五个数字，第一个数字为类别标签，第二到五个数字为框的信息，分别为 x，y，h，w，大小被归一化到小于 1

- voc 格式

  ① JPEGImages 文件夹：数据集图片

  ② Annotations 文件夹：标注，与图片对应的 xml 文件

  ③ ImageSets/Main 文件夹：将数据集分为训练集和验证集，因此产生的 train.txt 和 val.txt

- coco 格式

  images 文件夹里面是数据集的图片

  annotations 存放 train.json,val.json 文件等
