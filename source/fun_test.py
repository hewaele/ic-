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
                    self.pre_result.append([int(c), j, i, j+w, i+h, v2])

    #执行框融合
    def py_nms(self, dets, thresh):
        # x1、y1、x2、y2、以及score赋值
        x1 = dets[:, 1]
        y1 = dets[:, 2]
        x2 = dets[:, 3]
        y2 = dets[:, 4]
        scores = dets[:, 5]
        # 每一个候选框的面积
        areas = (x2 - x1 + 1) * (y2 - y1 + 1)
        # order是按照score降序排序的
        order = scores.argsort()[::-1]
        keep = []
        while order.size > 0:
            i = order[0]
            keep.append(i)
            # 计算当前概率最大矩形框与其他矩形框的相交框的坐标，会用到numpy的broadcast机制，得到的是向量
            xx1 = np.maximum(x1[i], x1[order[1:]])
            yy1 = np.maximum(y1[i], y1[order[1:]])
            xx2 = np.minimum(x2[i], x2[order[1:]])
            yy2 = np.minimum(y2[i], y2[order[1:]])

            # 计算相交框的面积,注意矩形框不相交时w或h算出来会是负数，用0代替
            w = np.maximum(0.0, xx2 - xx1 + 1)
            h = np.maximum(0.0, yy2 - yy1 + 1)
            inter = w * h
            # 计算重叠度IOU：重叠面积/（面积1+面积2-重叠面积）
            ovr = inter / (areas[i] + areas[order[1:]] - inter)

            # 找到重叠度不高于阈值的矩形框索引
            inds = np.where(ovr <= thresh)[0]
            # 将order序列更新，由于前面得到的矩形框索引要比矩形框在原order序列中的索引小1，所以要把这个1加回来
            order = order[inds + 1]
        return keep

    def show_image(self, img):
        for i in self.pre_result:
            cv2.rectangle(img, (i[1], i[2]), (i[3], i[4]), (0, 0, 255), 2)
        cv2.namedWindow('image')
        cv2.imshow('image', img)
        cv2.waitKey(0)
    #
    def real_result(self, result, index):
        tmp_result = []
        for i in index:
            tmp_result.append(result[i])

        tmp_result.sort(key=lambda s:s[1])
        a = np.array(tmp_result)[:,0]
        print(str(a))

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
            self.chance_result(imgi[:-4], res, w, h, 0.85)

        result_index = self.py_nms(np.array(self.pre_result), 0.35)
        print(result_index)
        self.real_result(self.pre_result, result_index)
        self.show_image(img_rgb)

        # cv2.namedWindow('img')
        # cv2.imshow('img', img_rgb)
        # cv2.waitKey(0)
        print('match success!')

    #将检测结果转换为csv文件用于分析
    def csv_result(self):
        pass

if __name__ == "__main__":
    #创建一个类
    img_path = '../image'
    md_path = '../module'
    T1 = REC(img_path, md_path)
    T1.match()
