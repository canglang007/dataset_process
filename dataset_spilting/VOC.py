
import os
import random
import argparse

# 这里的默认路径是windows下的绝对路径，自己需要注意自己的os和路径
parser = argparse.ArgumentParser()
# xml文件的地址，根据自己的数据进行修改 xml一般存放在Annotations下
parser.add_argument('--xml_path', default='D:\VOCdevkit\VOC2007\Annotations', type=str, help='input xml label path')
# 数据集的划分，地址选择自己数据下的ImageSets/Main
parser.add_argument('--txt_path', default='D:\VOCdevkit\VOC2007\ImageSets\Main', type=str, help='output txt label path')
opt = parser.parse_args()

# 这里将比例划分为了8:1:1
train_percent = 0.8  # 训练集所占比例
val_percent = 0.1    # 验证集所占比例
test_persent = 0.1   # 测试集所占比例

xmlfilepath = opt.xml_path
txtsavepath = opt.txt_path
total_xml = os.listdir(xmlfilepath)

if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)

num = len(total_xml)  
list = list(range(num))

t_train = int(num * train_percent)  
t_val = int(num * val_percent)

train = random.sample(list, t_train)
num1 = len(train)
for i in range(num1):
    list.remove(train[i])


val_test = [i for i in list if not i in train]
val = random.sample(val_test, t_val)
num2 = len(val)
for i in range(num2):
    list.remove(val[i])


file_train = open(txtsavepath + '/train.txt', 'w')
file_val = open(txtsavepath + '/val.txt', 'w')
file_test = open(txtsavepath + '/test.txt', 'w')
file_trainval = open(txtsavepath + '/trainval.txt', 'w')

for i in train:
    name = total_xml[i][:-4] + '\n'
    file_train.write(name)
    file_trainval.write(name)

for i in val:
    name = total_xml[i][:-4] + '\n'
    file_val.write(name)
    file_trainval.write(name)    

for i in list:
    name = total_xml[i][:-4] + '\n'
    file_test.write(name)
    
    
file_train.close()
file_val.close()
file_trainval.close()
file_test.close()

# 参考链接<https://blog.csdn.net/retainenergy/article/details/124613553>

