import json
# from sentence_transformers import SentenceTransformer, losses, InputExample
# from torch.utils.data import DataLoader
# from datasets import load_dataset
import random
import uuid

NUMBER_OF_CORPUS_ANSWERS = 10

with open("D:\\Falcon_projects\\problems.json",'r') as f:
    qas = json.load(f)

data = [qa[1] for qa in list(qas.items())]
print(len(data))
print(data[0])
final_qas ={}
topics = ['units-and-measurement','science-and-engineering-practices','physics']
i=0
for d in data:
    if d['topic'] in topics:
        question = d['question']
        reference = d['lecture']+ d['solution']
        final_qas.update({i:{'Question':question, 'Reference': reference}})
        i+=1


def create_corpus(qa_items):
    corpus_check={}
    content = []
    index = list(qa_items.keys())[0]
    for i in index:
        uiud_q = uuid.uuid1()
        question = qa_items[i]['Question']
        answer  = qa_items[i]['Reference']
        corpora_id = random.choice(index.pop(i),NUMBER_OF_CORPUS_ANSWERS)
        corpora_list = [qa_items[id]['Reference'] for id in corpora_id] + [answer]
        corpus = ''.join(random.shuffle(corpora_list))
        if corpus in corpus_check.keys():
            corpus_check[corpus]=uiud_r
            uiud_r = corpus_check[corpus]
        else:
            uiud_r = uuid.uuid1()
        content.append((uiud_q, question, uiud_r, corpus))
    del corpus_check
    return content

def create_json(content_list):
    queries ={}
    response_docs = {}
    corpus = {}
    for content in content_list:
        queries[content[0]]=content[1]
        corpus[content[2]] = content[3]
        response_docs[content[0]]=[content[2]]
    with open('output.json','w') as f:
        json.dump(queries)
        json.dump(corpus)
        json.dump(response_docs)





# model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')

# for row in data:
#     i = 