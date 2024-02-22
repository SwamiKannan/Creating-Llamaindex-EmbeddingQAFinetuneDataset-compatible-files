import json
from json_utils import create_corpus, create_json

with open('..//problems.json','r',encoding='utf-8') as f:
    dataset = json.load(f)

preferred_subjects = ['units-and-measurement', 'science-and-engineering-practices', 'physics']

dict_qa={}
keys = list(dataset.keys())
count_subj = 0
count = 0
for key in keys:
    vals = dataset[key]
    if vals['topic'] in preferred_subjects:
        question = vals['hint']+vals['question'] +''.join(vals['choices'])
        answer = vals['lecture'] + vals['solution'] if vals['solution']=="" else vals['lecture']
        dict_qa[count_subj]={'Question':question, 'Reference':answer}
        count_subj+=1
    count+=1

print(f'{len(list(dict_qa.keys()))} question-answer sets created')

with open('qa_json.json','w', encoding='utf-8') as fo:
    json.dump(dict_qa,fo)

content = create_corpus(dict_qa)
create_json(content)