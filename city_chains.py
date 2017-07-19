# -*- coding: utf-8 -*-

import random


path="C:/Users/Wvv/Desktop/city_crawler_chains" #需要改自己本地文件存放的位置
def city_exists(x,flag):
    if flag==0:
        adr='district.txt' #爬取并处理后的数据文件
    else:
        adr='csm_new.txt'  #验证谐音城市接龙的文件
    #判断输入的城市是否在城市库中
    with open(path+'/'+adr,'r') as f:
    #with open(path+'/district.txt','r') as f:
        for i in set(f.readlines()):
            if x==i.strip():
                return True
        return False

#汉字转拼音
def chinese_to_pinyin(x):
    y = ''
    dic = {}
    with open(path+"/unicode_pinyin.txt") as f:
        for i in f.readlines():
            dic[i.split()[0]] = i.split()[1]
    for i in x:
        i = str(i.encode('unicode_escape'))[-5:-1].upper()
        try:
            y += dic[i] + ' '
        except:
            y += 'XXXX ' #非法字符用XXXX代替
    return y
	
def city_select(x,flag):
    if x=='':
        return 'sorry,i need to have a rest!'
    #参数x为城市名，返回该城市名的接龙匹配城市
    if flag==0:
        adr='district.txt'
    else:
        adr='csm_new.txt'
    t=[]
    with open(path+'/'+adr,'r') as f:
    #with open(path+'/district.txt','r') as f:
        pinyin = chinese_to_pinyin(x[-1])
        base = f.readlines()[:-1]
        random.shuffle(base)
        for i in base:
            if chinese_to_pinyin(i[0])[:-2] == pinyin[:-2]:
                t.append(i)
    if t!=[]:
        return "接龙城市：%s" %random.choice(t)
    else:
        return "很遗憾，词库缺少此城市的接龙城市名！"

		
def city_start(flag):
    #flag为0时用爬取的数据文件作为词库，flag为其它时，用可以验证谐音城市接龙的文件作为词库
    while True:
        p = input("请输入一个城市名:")
        cycle_num1=0
        cycle_num2=0
        while p.strip() == '':
            p=input("对不起，我不明白，请重新输入：")
            cycle_num1+=1
            if cycle_num1>5:
                break
        while city_exists(p,flag) == False:
            p=input("该城市名不存在，请重新输入：")
            cycle_num2+=1
            if cycle_num2>5:
                break
        t = city_select(p,flag)
        print (t)
        m=input("是否继续（y/n）：")
        if m=='y':
            n=input("请选择接龙词库（0 or else num）：")
            if n=='0':
                city_start(0)
            else:
                city_start(n)
        else:
            print("已退出！")
        break

if __name__ == '__main__':
    #flag,m参数可根据需要修改
    city_start(0)