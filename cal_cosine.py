import kashgari
from kashgari.embeddings import BERTEmbedding
import logging
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import jieba
import sys

chinese_bert_file='./data/chinese_L-12_H-768_A-12'

def cal_cosine():
    bert = BERTEmbedding(chinese_bert_file,
                            task=kashgari.CLASSIFICATION,
                            sequence_length=10)

    # call for single embed
    seg_list1 = jieba.cut("我来到北京清华大学", cut_all=False)
    seg_list2 = jieba.cut("天然矿泉水是指从地下深处自然涌出的或钻井采集的", cut_all=False)
    seg_list1 = list(seg_list1)
    seg_list2 = list(seg_list2)
    embed_tensor1 = bert.embed_one(seg_list1)
    embed_tensor2 = bert.embed_one(seg_list2)

    # embed_tensor1 = bert.embed_one(['今','天','天','气','不','错'])
    # embed_tensor2 = bert.embed_one(['我','住','在','南','京'])

    print(embed_tensor1.shape)
    print(embed_tensor2.shape)

    embedding1 = np.zeros(shape=(1,3072))
    embedding2 = np.zeros(shape=(1,3072))
    
    for i in range(embed_tensor1.shape[0]):
        # print(embed_tensor1[i][:])
        embedding1 += embed_tensor1[i][:]
        embedding2 += embed_tensor2[i][:]

    print(embedding1)
    print(embedding2)
    cos_value = cosine_similarity(embedding1, embedding2)
    print('cos_value =', str(cos_value[0][0]))
