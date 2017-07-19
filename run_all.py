# -*- coding: utf-8 -*-

import city_chains
import city_crawler
import District

if __name__ == '__main__':
    #可以设置爬取的链接数
    city_crawler.getTypes(20)
    print('crawler complete!')
    #提取爬取数据的城市名，unicode保存
    District.district()
    #0表示为爬取的数据作为词库，其它表示用额外的数据作为词库，验证谐音城市接龙
    p=input("请选择接龙词库（0：表示用爬取的数据作为词库 or else num：用额外的数据作为词库，验证谐音城市接龙）：")
    if p=='0':
        city_chains.city_start(0)
    else:
        city_chains.city_start(p)