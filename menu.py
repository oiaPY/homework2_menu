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
                break
             elif county == "jiangning":
                 print("jiangning")
                 break
             elif county == "pukou":
                 print("pukou")
                 break
             elif county == "q":
                break
             elif county == "b":
                 print(dic["jiangsu"].keys())
             else:
                 print("输入无效，请重新输入！")
         elif city == "suzhou":
             print(dic["jiangsu"]["suzhou"])
             county = input("请输入您选择的区或县：")
             if county == "changshu":
                 print("changshu")
                 break
             elif county == "kunshan":
                 print("kunshan")
                 break
             elif county == "wujiang":
                 print("wujiang")
                 break
             elif county == "q":
                break
             elif county == "b":
                 print(dic["jiangsu"].keys())
             else:
                 print("输入无效，请重新输入！")
         elif city == "changzhou":
             print(dic["jiangsu"]["changzhou"])
             county = input("请输入您选择的区或县：")
             if county == "liyang":
                print("liyang")
                break
             elif county == "jintan":
                 print("jintan")
                 break
             elif county == "xinbei":
                 print("xinbei")
                 break
             elif county == "q":
                break
             elif county == "b":
                 print(dic["jiangsu"].keys())
             else:
                 print("输入无效，请重新输入！")
         elif city == "q":
             break
         elif city == "b":
            print(dic.keys())
         else:
             print("输入无效，请重新输入！")
    elif province == "zhejiang":
         print(dic["zhejiang"].keys())
         city = input("请输入您选择的市：")
         if city == "hangzhou":
             print(dic["zhejiang"]["hangzhou"])
             county = input("请输入您选择的区或县：")
             if county == "yuhang":
                print("yuhang")
                break
             elif county == "shangcheng":
                 print("shangcheng")
                 break
             elif county == "xihu":
                 print("xihu")
                 break
             elif county == "q":
                break
             elif county == "b":
                 print(dic["zhejiang"].keys())
             else:
                 print("输入无效，请重新输入！")
         elif city == "jiaxing":
             print(dic["zhejiang"]["jiaxing"])
             county = input("请输入您选择的区或县：")
             if county == "jiashan":
                print("jiashan")
                break
             elif county == "pinghu":
                 print("pinghu")
                 break
             elif county == "haining":
                 print("haining")
                 break
             elif county == "q":
                break
             elif county == "b":
                 print(dic["zhejiang"].keys())
             else:
                 print("输入无效，请重新输入！")
         elif city == "ningbo":
             print(dic["zhejiang"]["ningbo"])
             county = input("请输入您选择的区或县：")
             if county == "xiangshan":
                print("xiangshan")
                break
             elif county == "yuyao":
                 print("yuyao")
                 break
             elif county == "cixi":
                 print("cixi")
                 break
             elif county == "q":
                break
             elif county == "b":
                 print(dic["zhejiang"].keys())
             else:
                 print("输入无效，请重新输入！")
         elif city == "q":
             break
         elif city == "b":
            print(dic.keys())
         else:
             print("输入无效，请重新输入！")
    elif province == "anhui":
         print(dic["anhui"].keys())
         city = input("请输入您选择的市：")
         if city == "hefei":
             print(dic["anhui"]["hefei"])
             county = input("请输入您选择的区或县：")
             if county == "chaohu":
                print("chaohu")
                break
             elif county == "feidong":
                 print("feidong")
                 break
             elif county == "feixi":
                 print("feixi")
                 break
             elif county == "q":
                break
             elif county == "b":
                 print(dic["anhui"].keys())
             else:
                 print("输入无效，请重新输入！")
         elif city == "wuhu":
             print(dic["anhui"]["wuhu"])
             county = input("请输入您选择的区或县：")
             if county == "fanchang":
                print("fanchang")
                break
             elif county == "nanling":
                 print("nanling")
                 break
             elif county == "wuwei":
                 print("wuwei")
                 break
             elif county == "q":
                break
             elif county == "b":
                 print(dic["anhui"].keys())
             else:
                 print("输入无效，请重新输入！")
         elif city == "tongling":
             print(dic["anhui"]["tongling"])
             county = input("请输入您选择的区或县：")
             if county == "zongyang":
                 print("zongyang")
                 break
             elif county == "tongguan":
                 print("tongguan")
                 break
             elif county == "yi'an":
                 print("yi'an")
                 break
             elif county == "q":
                break
             elif county == "b":
                 print(dic["anhui"].keys())
             else:
                 print("输入无效，请重新输入！")
         elif city == "q":
             break
         elif city == "b":
            print(dic.keys())
         else:
             print("输入无效，请重新输入！")
    elif province == "q":
        break
    else:
        print("输入无效，请重新输入！")




