from collections import Counter

article = read_data('data/article1.txt')  "這是老師要求的測驗方式"
article=article.split(' ')
Counter(article)