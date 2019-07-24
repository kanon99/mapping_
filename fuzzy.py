#!/usr/bin/env pythong
# _*_ coding:utf-8 _*_

from fuzzywuzzy import fuzz
import pandas as pd

# a=fuzz.ratio("浙江大菱-宁波", "浙江大菱海洋食品有限公司")
# print(a)

def fuz():

    # 设置空num列
    awd_dict = {'name':[] , 'num': [],'fuzzi':[]}
    # data为爱稳定的表格
    data = list(awd_dict["name"])
    data_len = len(data)
    new_num = list(awd_dict["num"])
    fuzzz = list(awd_dict["fuzzi"])

    # data1为ERP的表格
    #创建epr字典表
    erp_dict = {'name':[],'mu':[]}
    data1 = list(erp_dict["name"])
    data_len1 = len(data1)
    #获得ERP的num列：
    nm = list(erp_dict["mu"])

    for j in range(data_len):
        # if j == 0 :
        data_n = data[j]
        for i in range(data_len1):
            data1_n = data1[i]
            cacu = fuzz.ratio(data1_n, data_n)
            if cacu > 0:
                #update fuzzz
                jj = int(fuzzz[j])
                if cacu >= jj:
                    fuzzz[j] = cacu
                    #取到erp第i行的mu 值：
                    new_nm_erp = nm[i]
                    #设置awd的第j行的 num 值 为num[i]
                    new_num[j] = new_nm_erp
            else:
                pass
    print(new_num)



if __name__ == "__main__":
    fuz()
