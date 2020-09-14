# -*- coding: utf-8 -*-
from collections import Counter
from math import sqrt, acos, sin, cos, radians
import random
import matplotlib.pylab as plt
import numpy as np
def nearest_dot(s):
    mid = int(len(s) / 2)
    left = s[0:mid]
    right = s[mid:]
    mid_x = (left[-1][0] + right[0][0]) / 2.0
    plt.axvline(mid_x,ls='--')
    if len(left) > 2:
        lmin = nearest_dot(left)  # 左侧部分最近点对
        if len(lmin) >= 2:
            plt.plot([lmin[0][0], lmin[1][0]],[lmin[0][1] ,lmin[1][1]], color='r')
            plt.pause(0.2)
            plt.plot([lmin[0][0], lmin[1][0]],[lmin[0][1] ,lmin[1][1]],color='W',alpha=0.99)
    else:
        lmin = left
        if len(lmin) >= 2:
            plt.plot([lmin[0][0], lmin[1][0]],[lmin[0][1] ,lmin[1][1]], color='r')
            plt.pause(0.2)
            plt.plot([lmin[0][0], lmin[1][0]],[lmin[0][1] ,lmin[1][1]],color='W',alpha=0.99)
            
    if len(right) > 2:
        rmin = nearest_dot(right)  # 右侧部分最近点对
        if len(rmin) >= 2:
            plt.plot([rmin[0][0], rmin[1][0]],[rmin[0][1] ,rmin[1][1]],color='W',alpha=0.99)
            plt.pause(0.2)
            plt.plot([rmin[0][0], rmin[1][0]],[rmin[0][1] ,rmin[1][1]],color='W',alpha=0.99)
            
    else:
        rmin = right
        if len(rmin) >= 2:
            plt.plot([rmin[0][0], rmin[1][0]],[rmin[0][1] ,rmin[1][1]], color='r')
            plt.pause(0.2)
            plt.plot([rmin[0][0], rmin[1][0]],[rmin[0][1] ,rmin[1][1]],color='W',alpha=0.99)
            
    if len(lmin) > 1:
        dis_l = get_distance(lmin)
    else:
        dis_l = float("inf")
    if len(rmin) > 1:
        dis_r = get_distance(rmin)
    else:
        dis_r = float("inf")
    d = min(dis_l, dis_r)  # 最近点对距离
    mid_min = []
    for i in left:
        if mid_x - i[0] <= d:  # 如果左侧部分与中间线的距离<=d
            for j in right:
                if abs(i[0] - j[0]) <= d and abs(i[1] - j[1]) <= d:  # 如果右侧部分点在i点的(d,2d)之间
                    if get_distance((i, j)) <= d: mid_min.append([i, j])  # ij两点的间距若小于d则加入队列
    if mid_min:
        dic = []
        for i in mid_min:
            dic.append({get_distance(i): i})
            plt.plot([i[0][0], i[1][0]],[i[0][1] ,i[1][1]], color='r')
            plt.pause(0.2)
            plt.plot([i[0][0], i[1][0]],[i[0][1] ,i[1][1]], color='W',alpha=0.99)
        dic.sort(key=lambda x: x.keys())
        return list(dic[0].values())[0]
    elif dis_l > dis_r:
        return rmin
    else:
        return lmin


# 求点对的距离
def get_distance(m):
    dx = m[0][1] - m[1][1]  
    dy = m[0][0] - m[1][0]  
    return sqrt(dx**2 + dy **2)


def divide_conquer(s):
    s.sort()
    print(s)
    nearest_dots = nearest_dot(s)
    return nearest_dots

def set_Point(N):
    return [(random.randint(0, 10000)/100,random.randint(0, 10000)/100) for i in range(N)]

def draw(p):
    plt.ion()
    for each in p:
        plt.title("Graph")
        plt.grid(True)
        plt.xlabel("X")
        plt.ylabel("Y")
        my_x_ticks = np.arange(0 ,100, 5)
        my_y_ticks = np.arange(0, 100, 5)
        plt.xticks(my_x_ticks)
        plt.yticks(my_y_ticks)
        plt.scatter(each[0] ,each[1], s=20, c='b', marker="o")
        plt.pause(0.01)
if __name__ == "__main__":
    N = int(input("please input N:"))
    p = set_Point(N)
    draw(p)
    l = divide_conquer(p)
    print("最近点对为：", l)
    print("距离为：%.2f" % sqrt((l[0][0] - l[1][0]) ** 2 + (l[0][1] - l[1][1]) ** 2))
    plt.scatter(l[0][0] ,l[0][1], s=50, c='G', marker="o")
    plt.scatter(l[1][0] ,l[1][1], s=50, c='G', marker="o")
    plt.pause(1)
    plt.plot([l[0][0], l[1][0]],[l[0][1] ,l[1][1]],color='r')
