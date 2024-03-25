# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os

sets = ['train', 'val', 'test']  # 如果你的Main文件夹没有test.txt，就删掉'test'
# 改成自己的类别。
classes = ['scratches', 'pitted_surface', 'patches', 'rolled-in_scale', 'inclusion', 'crazing']  # class names
abs_path = os.getcwd()  # 获取当前工作路径
print(abs_path)

# 由绝对坐标变成相对坐标
def convert(size, box):
    # 计算倒数，用于归一化
    dw = 1. / (size[0])
    dh = 1. / (size[1])

    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_annotation(image_id):
    # 输入文件的路径,读入的是xml文件
    in_file = open(abs_path + '/VOCdevkit/VOC2007/Annotations/%s.xml' % (image_id), encoding='UTF-8')
    # 输出文件的路径，输出的是yolo的txt格式
    out_file = open(abs_path + '/VOCdevkit/VOC2007/labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    # root是xml文件的根元素，可以用来访问其他属性
    root = tree.getroot()
    # xml中的size部分
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    # 遍历object
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        # difficult = obj.find('Difficult').text
        # 读取xml中的label名
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        # 读取bbox中的边界框
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        b1, b2, b3, b4 = b
        # 标注越界修正
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        # 变成元组的形式
        b = (b1, b2, b3, b4)
        # 转化为yolo的格式
        bb = convert((w, h), b)
        # 以字符串类型写入，" ".join指的是用空格隔开
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


for image_set in sets:
    # 如果没有labels文件夹就创建文件夹
    
    if not os.path.exists(abs_path + '/VOCdevkit/VOC2007/labels/'):
        os.makedirs(abs_path + '/VOCdevkit/VOC2007/labels/')
    # .read().strip().split() 这个组合的作用是从文件中读取内容，去除两端的空白字符，然后将内容按空白字符分割成一个字符串列表。
    image_ids = open(abs_path + '/VOCdevkit/VOC2007/ImageSets/Main/%s.txt' % (image_set)).read().strip().split()
    list_file = open(abs_path + '/VOCdevkit/VOC2007/%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        # 保证不读取到别的文件，如readme等
        list_file.write(abs_path + '/VOCdevkit/VOC2007/JPEGImages/%s.jpg\n' % (image_id))  
        convert_annotation(image_id)
    list_file.close()

