import re

pattern=r'[A-Z]+rticle'
text='''
Initially available only in English, Wikipedia exists in over 340 languages and is the world's ninth most visited website. The English Wikipedia, with over 7 million articles, remains the largest of the editions, which together comprise more than 65 million articles and attract more than 1.5 billion unique device visits and 13 million edits per month (about 5 edits per second on average) as of April 2024.[W 1] As of September 2025, over 25% of Wikipedia's traffic comes from the United States, while Japan accounts for nearly 7%, and the United Kingdom, Germany and Russia each represent around 5%.[5]

Wikipedia has been praised for enabling the democratization of knowledge, its extensive coverage, unique structure, and culture. Wikipedia has been censored by some national governments, ranging from specific pages to the entire site.[6][7] Wikipedia's volunteer editors have written extensively on a wide variety of topics, but the encyclopedia has also been criticized for systemic bias, such as a gender bias against women and a geographical bias against the Global South.[8][9] While the reliability of Wikipedia was frequently criticized in the 2000s, it has improved over time, receiving greater praise from the late 2010s onward.[3][10][11] Articles on breaking news are often accessed as sources for up-to-date information about those events.[12][13]
'''
# match=re.search(pattern,text)
# print(match)
matches=re.finditer(pattern,text)
for match in matches:
    print(match)