# MultiAgents
Question 1 (4 points): Reflex Agent
    Cài đặt hàm evaluationFunction:
    - Tránh ma: xét nếu ở gần ma và ma không trong thời gian hoảng sợ thì tránh 
   (return - vô cùng vì ở hàm getAction bên trên khi chọn bestScore thì không chọn những vị trí này)
    - Ăn thức ăn gần nhất: tìm khoảng cách đến thức ăn gần nhất 
   (giá trị điểm sẽ lớn nhất để khi chọn bestScore trong hàm getAction sẽ chọn những vị trí đó)


Question 2 (5 points): Minimax
    Tính toán khi ma cũng di chuyển tối ưu
    Cài đặt thuật toán Minimax bằng cách thêm các hàm getValue, maxValue, minValue và cài đặt hàm getAction
    hàm getValue:
	trả về điểm (giá trị để đánh giá) khi không còn hành động nào tiếp theo hoặc đã đến độ sâu được cho
        nếu là pacman (index = 0) thì trả về hàm maxValue
	nếu là ma (index>0) thì trả về hàm minValue
    hàm maxValue
	tìm giá trị lớn nhất khi thực hiện các hành động tiếp theo và hành động để đạt được giá trị đó
    hàm minValue
        tìm giá trị nhỏ nhất khi thực hiện các hành động tiếp theo và hành động để đạt được giá trị đó  	
    hàm getAction sẽ trả về hành động tối ưu

Question 3 (5 points): Alpha-Beta Pruning
    Tính toán khi ma cũng di chuyển tối ưu
    Cài đặt giống minimax nhưng thêm 2 giá trị alpha (lưu giá trị tốt nhất của  max), beta(lưu giá trị tốt nhất của min)

Question 4 (5 points): Expectimax
    Tính toán khi ma di chuyển ngẫu nhiên
    Các hàm getValue, maxValue vẫn giống bài 2. Hàm minValue thay bằng expectedValue
    Hàm này trả về giá trị trung bình khi thực hiện các hành động tiếp theo
