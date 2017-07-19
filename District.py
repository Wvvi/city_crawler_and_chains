# -*- coding: utf-8 -*-

import csv

path="C:/Users/Wvv/Desktop/city_crawler_chains"
def district():
    with open(path+'/district.txt','w') as d:
        writer = csv.writer(d)
        with open(path+'/city_where.txt','r',encoding='utf-8') as f:
            lines=f.readlines()
            for i in lines[1:]:
                temp=i.split('·')[0]
                writer.writerow([temp])

if __name__=='__main__':
    district()
        
        
        
        