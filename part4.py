cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']


kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]

midterm_score = [kor_score, math_score, eng_score]

print(id(kor_score))  # kor_score 리스트 객체의 메모리 주소 출력
print(id(kor_score[0]))  # kor_score 리스트의 첫 번째 요소의 메모리 주소 출력
