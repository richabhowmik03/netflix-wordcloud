from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import wordcloud

stopwords = set(STOPWORDS)

gg_image = r"C:\Users\richa\Downloads\code\try\b.png"
mask = np.array(Image.open(gg_image))

data_file = pd.read_csv('netflix_titles.csv')

wordcloud = WordCloud(
    stopwords = stopwords,
    mask = mask,
    background_color= "white",
    collocations= False,
    colormap= "Set2").generate(''.join(data_file['title']))
plt.figure(figsize=(40,30))
plt.imshow(wordcloud,interpolation='bilinear')

plt.axis('off')
plt.show()
plt.tight_layout(pad=0)

wordcloud.to_file('cloudb.png')
