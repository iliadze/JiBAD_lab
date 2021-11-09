# Zadanie domowe 1 (09.11)
# Ilia Dotsenko

Trie = []
def build(samples):
    #initialize the root node
    Trie.append({'key':'',
                 'child_nodes':[],
                 'fail_link': 0,
                 'output':[]})

    #creating the trie based on the given samples
    for sample in samples:
        add_sample(sample)

    #find fail links within the created trie
    find_fail_links()

def add_sample(sample):
    step = 0
    k = 0

    #matching the sample with already created child nodes
    child = next_step(step, sample[k])
    while child != None:
        step = child
        k+=1
        if k < len(sample):
            child = next_step(step, sample[k])
        else:
            break
    #creating new child nodes until the sample is over
    for i in range(k, len(sample)):
        node = {'key':sample[i],'child_nodes':[],'fail_link':0,'output':[]}
        Trie.append(node)
        Trie[step]['child_nodes'].append(len(Trie) - 1)
        step = len(Trie) - 1
    #saving the value of the given sample to the last node (accept state)
    Trie[step]['output'].append(sample)

def next_step(step, key):
    #return the child node index mathcing the provided key, otherwise return None
    for node in Trie[step]['child_nodes']:
        if Trie[node]['key'] == key:
            return node
    return None

def find_fail_links():
    #finding fail links for all the nodes
    nodes = []

    for node in Trie[0]['child_nodes']:
        nodes.append(node)
        #all root's child nodes have a fail link to the root
        Trie[node]['fail_link'] = 0
    while nodes:
        now_at = nodes.pop(0)
        for child in Trie[now_at]['child_nodes']:
            nodes.append(child)
            step = Trie[now_at]['fail_link']
            while next_step(step, Trie[child]['key']) == None and step != 0:
                  step = Trie[step]['fail_link']
            Trie[child]['fail_link'] = next_step(step, Trie[child]['key'])
            #set the fail link to the root
            if Trie[child]['fail_link'] is None:
                  Trie[child]['fail_link'] = 0
            Trie[child]['output'] = Trie[child]['output'] + \
                                       Trie[Trie[child]['fail_link']]['output']

def search(words):
    step = 0
    words_found = []

    for i in range(len(words)):
        while next_step(step, words[i]) is None and step != 0:
            step = Trie[step]['fail_link']
        step = next_step(step, words[i])
        if step is None:
            step = 0
        else:
            for x in Trie[step]['output']:
                words_found.append({'index':i-len(x) + 1,'word':x})
    return print(words_found)

#insert your samples
build(['aa', 'abb', 'abc', 'cab'])

#insert text to be checked
search('aabcabb')

