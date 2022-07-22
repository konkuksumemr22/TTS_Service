import pyttsx3
import sys
# 이미지 인공지능으로부터 받은 텍스트를 sentence에 저장 - 현재: 임시 텍스트
sentence = 'The quick brown fox jumped over the lazy dog. hi there'

# TTS 엔진 시작
engine = pyttsx3.init()

# TTS 엔진 초기 선언
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)
engine.setProperty('rate', 165)

# 오디오로 출력
engine.say(sentence)

# mp3 파일로 저장
engine.save_to_file(sentence, 'result.mp3')

# TTS 엔진 실행
engine.runAndWait()

# 프로그램 종료
sys.exit()
