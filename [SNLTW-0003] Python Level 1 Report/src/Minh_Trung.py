tieuhoc = [["Ngày giải phóng miền Nam Việt Nam là ngày nào? ", 20,30,29, "B"], ["Triều Nguyễn có bao nhiêu vua?", 11,10,12, "C"]]
trunghoc= [[" Con chó sống nhiều nhất được mấy năm?", 10,9,1, "A"], ["Trạng Lường là ai?", "Lương Thế Vinh","Nguyễn Bá Tĩnh"," Nguyễn Bỉnh Khiêm", "A"], ["Chiến trannh thế giới lần thứ hai bắt đầu và kết thúc vào năm nào? ", "1938-1944", "1939-1945","1940-1946", "B"]]
phothong= [["Có bao nhiêu nguyên tố hóa học trên trái đất?(tính đến năm 2020)", 98 ,230,118, "C"]]

achivevment = [" Tiểu học", "Trung học", "Phổ Thông"]



grade = 0
while(True):
    print("Có ba level là: 1, 2, 3 (1 là dễ nhất,3 là khó nhất)")
    print("hãy nhập level bạn chọn: ")
    level=int(input())


    if level==1:
        cauhoi=tieuhoc
    elif level ==2:
        cauhoi = trunghoc
    elif level == 3:
        cauhoi = phothong
    else:
        print("Câu hỏi không tồn tại!")
        print("Mời bạn nhập lại cấp độ bạn chọn: ")
        continue
    for i in range(len(cauhoi)):
        print("Câu hỏi: ", cauhoi[i][0])
        print("A. ", cauhoi[i][1])
        print("B. ", cauhoi[i][2])      
        print("C. ", cauhoi[i][3])
        a = input("Mời bạn chọn câu trả lời bạn cho là đúng:) ")
        if a.upper() ==cauhoi[i][4]:
            print("Bravo")
            grade = grade + 1
            print("Điểm của bạn là", grade)
        else:
            print("Chúc bạn may mắn lần sau!")
            break
    
    print("Bạn đã đạt được thành tựu: ", achivevment[level-1])
          
                  
    
     
