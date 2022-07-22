import pyttsx3

# 이미지 인공지능으로부터 받은 텍스트를 sentence에 저장 - 현재는 임시 텍스트
sentence = 'The quick brown fox jumped over the lazy dog.'

# TTS 엔진 시작
engine = pyttsx3.init()

# TTS 엔진 초기 선언
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # Voice id : Alex
engine.setProperty('rate', 200)

# mp3 파일로 저장
engine.save_to_file(sentence, 'test.mp3')

# 오디오로 출력
engine.say(sentence)
engine.runAndWait()