import cv2
import pandas as pd
import os
import numpy as np
import sys
import PyQt5
import matplotlib.pyplot as plt

#定义类实现opencv匹配ic

class REC():
    def __init__(self, image_path = None, module_path = None, threshold = 0.8):
        self.image_path = image_path
        self.module_path = module_path
        self.name_path = ''
        self.get_image_list()
        self.get_module_list()
        self.threshold = threshold
        #包含三个参数 字符  位置  概率
        self.pre_result = []

    #获取识别图片位置
    def get_image_list(self):
        self.image_list = [os.path.join(p, fi) for p, n, f in os.walk(self.image_path) for fi in f]
        return self.image_list

    def get_module_list(self):
        self.module_list = [os.path.join(p, fi) for p, n, f in os.walk(self.module_path) for fi in f]
        return self.module_list

    def get_name_pos(self, img):
        pass

    #选择设定阈值的预测
    def chance_result(self, c, result, w, h, threshold):
        for i, v1 in enumerate(result):
            for j, v2 in enumerate(result[i][:]):
                if v2 >= threshold:
                    self.pre_result.append([c, j, i, w, h, v2])

    #执行框融合
    def op_result(self):
        l = [1 for i in range(len(self.pre_result))]
        #根据x值进行重新排序
        self.pre_result.sort(key = lambda s:s[1])
        print(self.pre_result)
        print(len(self.pre_result))
        tmp = self.pre_result[:][:]
        for index in range(len(tmp)-1):
            if -4<tmp[index][1]-tmp[index+1][1]<4:
                if tmp[index][1] > tmp[index+1][1]:
                    l[index] = 1
                else:
                    l[index] = 0

        for i in range(len(l)):
            if l[i] == 1:
                print(self.pre_result[i][0])






    #
    def real_result(self):
        pass

    #执行匹配
    def match(self):
        # 读入图片
        img_rgb = cv2.imread(self.image_list[0])
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        self.get_name_pos(img_rgb)

        #循环匹配每一个模板
        for imgi in os.listdir(self.module_path)[0:]:
            template = cv2.imread(os.path.join(self.module_path, imgi), 0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            #选取制定阈值结果
            self.chance_result(imgi[:-4], res, w, h, 0.9)

            # for pt in zip(*loc[::-1]):
            #     #将结果保存
            #     print(pt)
            #     tmp_result.append([imgi[:-4], pt[0], pt[1], w, h])
            #
            #     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        self.op_result()
        cv2.namedWindow('img')
        cv2.imshow('img', img_rgb)
        cv2.waitKey(0)
        print('match success!')

    #将洁厕结果转换为csv文件用于分析
    def csv_result(self):
        pass

if __name__ == "__main__":
    #创建一个类
    img_path = '../image'
    md_path = '../module'
    T1 = REC(img_path, md_path)
    T1.match()
