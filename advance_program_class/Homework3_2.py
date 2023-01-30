from collections import Counter

article = read_data('data/bonus.txt')
article=article.split(' ')

mix = []
i = 0 
while i < len(article)-1 :
  mix.append(article[i]+' '+article[i+1])
  i+=1

Counter(mix)