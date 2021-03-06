# -*- coding:utf-8 -*-
# Author: ๐ซ๐๐๐ ๐ค๐๐๐๐
# Email: zhaosheng@nuaa.edu.cn
# Time  : 2022-05-06  20:05:37.000-05:00
# Desc  : API test.

import requests
import argparse
import datetime
import os
parser = argparse.ArgumentParser(description='')
parser.add_argument('--ip', type=str, default="127.0.0.1",help='')
parser.add_argument('--port', type=int, default=8180,help='')
parser.add_argument('--path', type=str, default="register",help='')
parser.add_argument('--wav_path', type=str, default="/VAF-System/test_wavs",help='')
parser.add_argument('--mode', type=str, default="url",help='url or file')

args = parser.parse_args()

url=f"http://{args.ip}:{args.port}/{args.path}/{args.mode}"
headers = {
    'Content-Type': 'multipart/form-data'
}
endtime = datetime.datetime.now()
begintime = datetime.datetime.now()
wavs = sorted([os.path.join(args.wav_path,_file) for _file in os.listdir(args.wav_path) if ".wav" in _file])[:2]

start_time = datetime.datetime.now()
for wav in wavs:
    
    if args.mode == 'file':
        
        request_file = {'wav_file':open(wav, 'rb')}
        values = {"spkid": "15151832004","call_begintime":begintime,"call_endtime":endtime}
        print(values)
        # !ไธ่ฝๆๅฎheader
        # try:
        resp = requests.request("POST",url, files=request_file, data=values)
        print(resp.json())
        # except Exception as e:
        #     print(e)
        #     continue
    else:
        wav_url = f"local:/{wav}"
        values = {"spkid": "15151832004","wav_url":wav_url,"call_begintime":begintime,"call_endtime":endtime}
        print(values)
        # try:
        resp = requests.request("POST",url=url, data=values)
        print(resp.json())
        # except Exception as e:
        #     print(e)
        #     continue

time_used = end = datetime.datetime.now() - start_time
print(time_used)