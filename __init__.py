import os
from cudatext import *
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def short_name(name):
    if name=='Internet Explorer':
        return 'IE'
    elif name=='Chrome':
        return 'Chr'
    elif name=='Safari':
        return 'Saf'
    elif name=='Firefox':
        return 'Fox'
    elif name=='Android':
        return 'An'
    elif name=='Opera':
        return 'Op'
    return name 

def arr_to_str(arr):
    res=arr[0].rstrip('+')
    for i in arr[1:]:
        res+='/'+i.rstrip('+').rstrip('+</;')
    return res

def get_data_by_property(prop):
    global res
    if prop in res:
        out=''
        for i in res[prop]:
            if len(res[prop][i])>0 and not res[prop][i]==['']:
                out+=short_name(i)+' '+arr_to_str(res[prop][i]).replace('.0','')+';'
            else:
                out+=short_name(i)+' -;'
        if out.endswith('</;'):
            out=out[:-3]
        return out
    return False

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_cuda_css_property_info.ini')

class Command:
    
    def __init__(self):
        global res#=json.load(open('result.json','r'))
        res=json.load(open('result.json','r'))

    def config(self):
        pass
                
    def on_caret(self, ed_self):
        x,y,x1,y1=ed_self.get_carets()[0]
        #print(ed_self.get_carets()[0][2])
        if not (x1==-1):
            if x>x1:
                x,x1=x1,x
            #print(str(x)+' '+str(y)+' '+str(x1)+' '+str(y1))
            text=ed_self.get_text_substr(x,y,x1,y1)
            if len(text)>0:
                res=get_data_by_property(text)
                if res:
                    msg_status(res)# font-size
