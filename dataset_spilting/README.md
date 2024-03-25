# 数据集划分

## 一.voc 数据集

voc 数据集的格式一般如下：

```

├── Annotations            # 里面存放 .xml 文件，图片的标签，比如坐标位置信息等。
├── ImageSets
│   ├── Segmentation # 用于分割的数据
│   └── Main     # 用于存放生存的txt文件，如trainval.txt,train.txt，val.txt,test.txt
└── JPEGImages    # 存放的是图片文件，分割后的图片
```

参考链接：<https://blog.csdn.net/u012505617/article/details/104576840>

&#x20; <https://blog.csdn.net/retainenergy/article/details/124613553>
