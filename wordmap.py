from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt




text = open("sport_cleaned.txt").read()
wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
# this will remove the axis display along with the image.
plt.axis("off")
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.show() 
