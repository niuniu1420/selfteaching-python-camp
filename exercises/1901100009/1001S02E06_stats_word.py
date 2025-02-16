en_text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

'''

cn_text = '''
在青春的路口，曾经有那么一条小路若隐若现，召唤着我。
母亲拦住我：“那条路走不得。”我不信。
“我就是从那条路走过来的，你还有什么不信？”
“既然你能从那条路上走过来，我为什么不能？”
“我不想让你走弯路。”
“但是我喜欢，而且我不怕。”
母亲心疼地看我好久，然后叹口气：“好吧，你这个倔强的孩子，那条路很难走，一路小心。”
'''


#1.

def states_text_en(text):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element):
            words.append(element)
    counter={}
    word_set = set(words)

    for word in word_set:
        counter[word] = words.count(word)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)



def states_text_cn(text):
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character]=cn_characters.count(character)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)   

if __name__=="__main__":
    en_result = states_text_en(en_text)
    cn_result = states_text_cn(cn_text)
    print ('统计参数中英文单词出现的频次==> \n',en_result)
    print ('统计参数中中文字出现的频次==> \n',cn_result)


