# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: moziran
dic = {"jiangsu":
                {"nanjing": ["gaochun", "jiangning","pukou"],
                 "suzhou": ["changshu", "kunshan", "wujiang"],
                 "changzhou": ["liyang", "jintan", "xinbei"]
                },
       "zhejiang":
                {"hangzhou": ["yuhang", "shangcheng", "xihu"],
                 "jiaxing": ["jiashan", "pinghu", "haining"],
                 "ningbo": ["xiangshan", "yuyao", "cixi"]
                },
       "anhui":
           {"hefei": ["chaohu", "feidong", "feixi"],
            "wuhu": ["fanchang", "nanling", "wuwei"],
            "tongling": ["zongyang", "tongguan", "yi'an"]
           }
       }

print(dic.keys())
while True:
    province = input("请输入您选择的省：")
    if province == "jiangsu":
         print(dic["jiangsu"].keys())
         city = input("请输入您选择的市：")
         if city == "nanjing":
             print(dic["jiangsu"]["nanjing"])
             county = input("请输入您选择的区或县：")
             if county == "gaochun":
                print("gaochun")
             elif county == "jiangning":
                 print("jiangning")
             else:
                 print("pukou")
         elif city == "suzhou":
             print(dic["jiangsu"]["suzhou"])
             county = input("请输入您选择的区或县：")
             if county == "changshu":
                 print("changshu")
             elif county == "kunshan":
                 print("kunshan")
             else:
                 print("wujiang")
         else:
             print(dic["jiangsu"]["changzhou"])
             county = input("请输入您选择的区或县：")
             if county == "liyang":
                print("liyang")
             elif county == "jintan":
                 print("jintan")
             else:
                 print("xinbei")
    elif province == "zhejiang":
         print(dic["zhejiang"].keys())
         city = input("请输入您选择的市：")
         if city == "hangzhou":
             print(dic["zhejiang"]["hangzhou"])
             county = input("请输入您选择的区或县：")
             if county == "yuhang":
                print("yuhang")
             elif county == "shangcheng":
                 print("shangcheng")
             else:
                 print("xihu")
         elif city == "jiaxing":
             print(dic["zhejiang"]["jiaxing"])
             county = input("请输入您选择的区或县：")
             if county == "jiashan":
                print("jiashan")
             elif county == "pinghu":
                 print("pinghu")
             else:
                 print("haining")
         else:
             print(dic["zhejiang"]["ningbo"])
             county = input("请输入您选择的区或县：")
             if county == "xiangshan":
                print("xiangshan")
             elif county == "yuyao":
                 print("yuyao")
             else:
                 print("cixi")
    else:
         print(dic["anhui"].keys())
         city = input("请输入您选择的市：")
         if city == "hefei":
             print(dic["anhui"]["hefei"])
             county = input("请输入您选择的区或县：")
             if county == "chaohu":
                print("chaohu")
             elif county == "feidong":
                 print("feidong")
             else:
                 print("feixi")
         elif city == "wuhu":
             print(dic["anhui"]["wuhu"])
             county = input("请输入您选择的区或县：")
             if county == "fanchang":
                print("fanchang")
             elif county == "nanling":
                 print("nanling")
             else:
                 print("wuwei")
         else:
             print(dic["anhui"]["tongling"])
             county = input("请输入您选择的区或县：")
             if county == "zongyang":
                print("zongyang")
             elif county == "tongguan":
                 print("tongguan")
             else:
                 print("yi'an")

