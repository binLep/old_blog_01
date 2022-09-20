#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import re

sig = ["data-main", "src", "href"]


def core_replace(data, rpl_core):
    rpl = re.findall('('+rpl_core+'="/[^/])', data)
    for k in range(0, len(rpl)):
        if 'old_blog_01' not in data:
            data = re.sub(rpl[k], rpl[k][:-2]+"/old_blog_01"+rpl[k][-2:], data)
            # print(rpl)
    return data


def do_replace(url):
    with open(url, "r+") as fr:
        data = fr.readlines()
    for i in range(0, len(data)):
        for j in range(0, len(sig)):
            data[i] = core_replace(data[i], sig[j])
        print(data[i])
    with open(url, "wb") as fw:
        for i in range(0, len(data)):
            if i == len(data) - 1 and data[i] == '\n':
                break
            fw.write(data[i] + '\n')


def scaner_file(url):
    file = os.listdir(url)
    for f in file:
        real_url = os.path.join(url, f)
        if os.path.isfile(real_url):
            if real_url[-4:] != '.png' and real_url[-4:] != '.jpg':
                print('[*] ' + real_url)
                do_replace(real_url)
        elif os.path.isdir(real_url):
            scaner_file(real_url)
        else:
            continue


scaner_file(sys.argv[1])
