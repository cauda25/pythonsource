import random
import time
import sqlite3
from datetime import datetime

# 시도 횟수, 정답 개수
n, cor_ans = 1, 0
# word.txt 읽기 => list 담기
words = []
with open("./basic/word.txt", "r", encoding="utf-8") as f:
    for w in f:
        words.append(w.strip())

# print(words)

start = time.time()
# list 에서 임의 단어 추출(5번)
# 5번에 대한 시간 잰 후 출력
while n < 6:
    # 리스트 내용 섞기
    random.shuffle(words)

    # 임의 추출
    q = random.choice(words)

    # 문제 보여주기
    print(f"Question #{n}")
    print(q, "\n")

    # 타자 입력(input)
    answer = input("단어 : ")

    # 문제 == 입력값(정답 개수 추가)
    if q == answer:
        print("PASS!")
        cor_ans += 1
    else:
        print("Wrong!")

    # n 증가
    n += 1
end = time.time()
et = format(end - start, ".3f")

# cor_ans 3개 이상이면 합격, 불합격
if cor_ans >= 3:
    print("합격")
else:
    print("불합격")

print(f"게임 시간 : {et}초 ,정답 개수 : {cor_ans}개")

# db 저장
# records.db
conn = sqlite3.connect("./basic/records.db", isolation_level=None)
cursor = conn.cursor()

# records 테이블 생성
# id INTGER PRIMARY KEY AUTOINCREMENT(자동증가)
# id, cor_ans, record(초), refdate(날짜)
sql = "CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_ans INTEGER, record TEXT, regdate TEXT)"
cursor.execute(sql)

sql = "INSERT INTO records(cor_ans, record ,regdate) VALUES(?,?,?)"
cursor.execute(sql, (cor_ans, et, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

conn.commit()
conn.close()
