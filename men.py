from mendeley import Mendeley
from mendeley.session import MendeleySession
import requests
import yaml
import os
import re
# ref: https://stackoverflow.com/questions/47777288/authentication-issue-in-mendeley-python-sdk


# path = '/home/keita/work/paper/Centrality_in_valued_graphs_A_measure_of_betweenness_based_on_network_flow.pdf'
# session.documents.create_from_file(path)

# c=session.catalog.by_identifier(doi='10.1371/journal.pmed.0020124', view='stats')
# print(c.re)

def add_pdf_file(session, path,group):
    session.documents.create_from_file(path)
    return 0

def add_all_pdf(session,dirc,group,):
    "dirc ディレクトリ内の pdf ファイルを全て group のドキュメントに追加"
    return 0

def search_doc(session,group,name):
    "group 内にある name ドキュメントを探索"
    return 0

def list_doc(group):
    " group 内にあるドキュメントの一覧を表示"
    for doc in group.documents.iter():
        print(doc.title)
    return 0

def search_config(f_name):
    "config ファイルの中から情報を取得"
    "以下で登録http://dev.mendeley.com/"
    config = {}
    if os.path.isfile(f_name): 
        with open(f_name) as f:
            f_lines = f.readlines()
            for line in f_lines:
                content = line.split(':')
                config[content[0]] = re.findall(r'{(.*?)}',content[1])[0]
    else:
        print("Please make config file(conifg.yml)")
    return config



def main():
    
        
    config = search_config('config.txt')
    redirect_url = "http://localhost:8000/testing"

    # mendeley = Mendeley(client_id,client_secret,redirect_uri=redirect_url)
    mendeley = Mendeley(config['clientId'],config['clientSecret'],redirect_uri=redirect_url)

    auth = mendeley.start_implicit_grant_flow()
    login_url = auth.get_login_url()

    res = requests.post(login_url,allow_redirects = False, data = {
        'username': config['user'],
        'password': config['pass']
    })

    # res = requests.post(login_url,allow_redirects = False, data = {
    #     'username': user,
    #     'password': password
    # })
    auth_response = res.headers['Location']
    
    session = auth.authenticate(auth_response)

    for gr in session.groups.iter():
        print(gr.name)
        if gr.name == config['group']:
            group_id = gr.id
            
    group = session.groups.get(group_id)

    list_doc(group)
    

if __name__ == "__main__":
    main()
