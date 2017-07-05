# 클래스 class

##### Article variables
title1 = "개발"
author1 = "마르코"
content1 = "개발은 쉬워요"
view_count1 = 0

title2 = "코칭"
author2 = "마르코"
content2 = "코칭은 쉬워요"
view_count2 = 0

title3 = "창업"
author3 = "마르코"
content3 = "창업은 쉬워요"
view_count3 = 0

##### Article class
# class Article:
#     title = "개발"
#     author = "마르코"
#     content = "개발은 쉬워요"
#     view_count = 0

# article1 = Article()
# print(article1.title)
# article2 = Article()
# article2.title = "코칭"
# print(article1.title)
# print(article2.title)

##### Article class with __init__
class Article:
    author = "마르코"
    view_count = 0

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def read(self):
        self.view_count = self.view_count + 1

article1 = Article("개발", "개발은 쉬워요")
article2 = Article("코칭", "코칭은 쉬워요")
article3 = Article("창업", "창업은 쉬워요")

article2.read()
article3.read()
print(article1.title, article1.content, article1.view_count)
print(article2.title, article2.content, article2.view_count)
print(article3.title, article3.content, article3.view_count)

article1.read()
print(article1.view_count)
article1.read()
print(article1.view_count)
article1.view_count = article1.view_count + 1
print(article1.view_count)


##### Article class inheritance 상속
class BrunchArticle(Article):
    source = "브런치"

    def read(self):
        self.view_count = self.view_count + 5


brunch_article = BrunchArticle("다시개발", "다시개발은 재밌어요~")
print(brunch_article.view_count)
print(brunch_article.title , brunch_article.content)
print(brunch_article.view_count)
print(brunch_article.source)
print(brunch_article.view_count)
brunch_article.read()
print(brunch_article.view_count)
brunch_article.read()
print(brunch_article.view_count)
