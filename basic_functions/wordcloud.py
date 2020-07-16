from wordcloud import WordCloud
import matplotlib.pyplot as plt

#txt 파일 가져와서 text로 저장하기
f = open("/Users/huhyoujung/Desktop/코딥/lecture_note10.txt", 'r')
list = []
for line in f.readlines():
    try:
        list.append( re.findall('#\D+:(.*)',line)[0] )
    except:
        list.append( line )
text = ' '.join(list).replace('\n',' ')

#word cloud 생성
wordcloud = WordCloud(font_path='font/NanumGothic.ttf', background_color='white').generate(text)

#word cloud 옵션 설정
plt.figure(figsize=(22,22)) #이미지 사이즈 지정
plt.imshow(wordcloud)
plt.axis('off') #x y 축 숫자 없애기
plt.show() 
plt.savefig()

#불용어가 있을 경우 제거해주기
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 
 
stopwords = set(STOPWORDS) 
stopwords.add('불용어') 
 
wordcloud = WordCloud(font_path='font/NanumGothic.ttf',stopwords=stopwords,background_color='white').generate(text)