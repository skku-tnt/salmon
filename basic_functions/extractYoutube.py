# !pip install pytube3
from pytube import YouTube

video_url = 'https://www.youtube.com/watch?v=2Cjpth9ljMI&list=PLqylIKbCwYVwxiJi-48Lklo3uxqOHNDyY&index=3U'
video = YouTube(video_url)

# print("[영상 제목]", video.title)  # 영상제목
# print("[영상 게시자]", video.author) # 영상 게시자
# print("[조회수]", video.views)
# print("[평균평점]", video.rating) # 평균 평점
# print("[영상길이(초)]", video.length)
# print("[연령제한여부]", video.age_restricted)
# print("[영상 설명]", video.description) # 영상 설명
# print("[썸네일URL]", video.thumbnail_url) # 썸네일 url 주소

# video.streams.all()

# 전송 포맷 중 첫번째 선택
# stream = video.streams.all()[0]
# stream
# <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">

# 음성만 선택시
# video.streams.filter(only_audio = True).all()

# mp4
# video.streams.filter(file_extension = 'mp4').all( )

# 선택
# stream = video.streams.filter(file_extension = 'mp4').all( )[0]
# stream
# <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">

# 영상 다운로드
# stream.download()

# 파일 이름 지정 
## 폴더지정 가능
# stream.download(output_path='test', filename = 'KOBE', filename_prefix= 'R.I.P_')

video.captions.all()

caption = video.captions.get_by_language_code('ko')
if caption == None:
    caption = video.captions.all()[0]

# 자막 xml 포멧 
print(caption.xml_captions)

# 자막 srt 포멧
print(caption.generate_srt_captions())

# 자막 다운받기: download("파일명")
# caption.download(video.title )