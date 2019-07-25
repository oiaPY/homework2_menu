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
# click1 = input("请输入你的选择：")
if click1 == "jiangsu":
     print(dic)