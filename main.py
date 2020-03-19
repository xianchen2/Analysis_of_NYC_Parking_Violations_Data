import logging
import os
from sys import argv
import ast
import time
from datetime import datetime
from elasticsearch import Elasticsearch
from math import ceil
from sodapy import Socrata

es = Elasticsearch()

def creat_and_update_index(index_name, doc_type):
    es = Elasticsearch()
    try:
        es.indices.creat(index=index_name)
    except Exception:
        pass    
    es.indices.put_mapping(
        index = index_name,
        doc_type = doc_type,
        body={
            doc_type: { 
            'properties':{
                "Fine_amount": {"type": "float"},
                "Penalty_amount": {"type": "float"},
                "Interest_amount": {"type": "float"},
                "Reduction_amount": {"type": "float"},
                "Payment_amount": {"type": "float"},
                "Amount_due": {"type": "float"}}
            }
        }
    )
    return es

def get_violate_data(filename):
    d=open(str(filename),'r')
    d=d.read()
    d=d.split('\n')
    del d[-1]
    for i in range(len(d)):
        d[i] = ast.literal_eval(d[i])

    return d

if __name__ == '__main__':
    #step 1: create an elastic search index 
    es = creat_and_update_index('violations-index','parking')
    # step 2: get data
    docks = get_violate_data(argv[1])
    #push data into the elastic search
    for dock in docks:
        dock['issue_date'] = datetime.strptime(dock['issue_date'],'%m/%d/%Y') 
        res = es.index(index='violations-index',doc_type='parking',body=dock)
        print(res['result'])




