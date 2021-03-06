# Author: π«πππ π€ππππ
# Email: zhaosheng@nuaa.edu.cn
# Time  : 2022-05-06  19:53:59.000-05:00
# Desc  : utils about database
import pickle
from utils.phone import getPhoneInfo
from datetime import datetime, timedelta
def add_to_database(database,embedding,spkid,wav_file_path,raw_file_path,database_filepath,max_score,mean_score,min_score):
    """add new speaker or new wav to black databse

    Args:
        database (dict): old database
        embedding (torch.tensor): new embedding
        spkid (string): speak id
        wav_file_path (string): wav file path
    """

    # Database Format:{
    #     "embedding_1":ηΌη ειοΌ
    #     "wav":ι’ε€ηζδ»Άθ·―εΎοΌ
    #     "raw":εε§ζδ»Άθ·―εΎοΌ
    #     "zip_code":ε½ε±ε°zip_codeοΌ
    #     "phone_type":θΏθ₯ε
    #     "time":ζ³¨εζΆι΄
    #     "max_score":θͺζζ£ιͺζι«ε
    #     "mean_socre":θͺζζ£ιͺεΉ³εε
    #     "min_socre":θͺζζ£ιͺζδ½ε
    # }

    if spkid in database.keys():
        return False
    else:
        database[spkid] = {}
        
    phone_info = getPhoneInfo(spkid)
    if phone_info:
        database[spkid]["zip_code"] = phone_info['zip_code']
        database[spkid]["phone_type"] = phone_info['phone_type']
    else:
        database[spkid]["zip_code"] = "None"
        database[spkid]["phone_type"] = "None"
    database[spkid]["embedding_1"] = embedding.numpy()
    database[spkid]["wav"] = wav_file_path
    database[spkid]["raw"] = raw_file_path

    database[spkid]["max_score"] = max_score
    database[spkid]["mean_score"] = mean_score
    database[spkid]["min_score"] = min_score

    database[spkid]["time"] = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    with open(database_filepath, 'wb') as f:
        pickle.dump(database, f)
    return True