import turtle

# 화면 설정
window = turtle.Screen()
window.bgcolor("white")

# 거북이 설정
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

# 삼각형 그리기
for _ in range(3):
    t.forward(100)  # 100 픽셀 앞으로 이동
    t.left(120)     # 120도 왼쪽으로 회전

# 화면 유지
window.mainloop()
