import cv2
import pandas as pd
import os
import numpy as np
import sys
import PyQt5
import matplotlib.pyplot as plt

#定义类实现opencv匹配ic

class REC():
    def __init__(self, image_path = None, module_path = None):
        self.image_path = image_path
        self.module_path = module_path
        self.name_path = ''
        self.get_image_list()
        self.get_module_list()

        #包含三个参数 字符  位置  概率
        self.pre_result = {}
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
        tmp_result = []
        for i, v1 in enumerate(result):
            for j, v2 in enumerate(result[i][:]):
                if v2 >= threshold:
                    tmp_result.append([c, j, i, w, h, v2])
        return tmp_result
    
    #执行框融合
    def op_result(self):
        pass

    #
    def real_resulr(self):
        pass

    #执行匹配
    def match(self):
        # 读入图片
        img_rgb = cv2.imread(self.image_list[0])
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        self.get_name_pos(img_rgb)
        # 循环匹配模板
        print('match test')
        print(self.module_path)
        for imgi in os.listdir(self.module_path)[0:1]:
            tmp_result = []
            print(imgi)
            template = cv2.imread(os.path.join(self.module_path, imgi), 0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.85
            loc = np.where(res >= threshold)
            self.chance_result(res, 0.85)
            for pt in zip(*loc[::-1]):
                #将结果保存
                print(pt)
                tmp_result.append([imgi[:-4], pt[0], pt[1], w, h])

                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
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
