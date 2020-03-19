
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
    es = creat_and_update_index('violation-index','parking')
    # step 2: get data
    docks = get_violate_data(argv[1])
    #push data into the elastic search
    for dock in docks:
        dock['issue_date'] = datetime.strptime(dock['issue_date'],'%m/%d/%Y') 
        try:
            dock['fine_amount']=float(dock['fine_amount'])
        except Exception:
            pass    
        
        try:
            dock['reduction_amount']=float(dock['reduction_amount'])
        except Exception:
            pass            

        try:
            dock['penalty_amount']=float(dock['penalty_amount'])
        except Exception:
            pass            
        
        try:
            dock['interest_amount']=float(dock['interest_amount'])
        except Exception:
            pass            

        try:
            dock['amount_due']=float(dock['amount_due'])
        except Exception:
            pass               

        res = es.index(index='violation-index',doc_type='parking',body=dock)
        print(res['result'])


