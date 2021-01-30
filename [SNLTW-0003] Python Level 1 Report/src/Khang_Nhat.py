print('Chọn các hệ sau đây:')
print('1.Tấn công\n2.Phòng thủ\n3.Bền bỉ\n4.Cân bằng')
vp = int(input('Bạn chọn hệ nào: '))
if(vp == 1):
    print('Bạn đã chọn hệ tấn công!\n')
    atk = 25
    hp = 125
    stm = 5
elif(vp == 2):
    print('Bạn đã chọn hệ phòng thủ!\n')
    atk = 15
    hp = 140
    stm = 5
elif(vp == 3):
    print('Bạn đã chọn hệ bền bỉ\n')
    atk = 20
    hp = 120
    stm = 7
else:
    print('Bạn đã chọn hệ cân bằng\n')
    atk = 22
    hp = 130
    stm = 6
en = 0
enatk = 18
enhp = 175
enstm = 6
enen = 0
print('Bạn hãy chọn các phụ kiện sau đây:')
print('1.Thêm sắc bén(+5 tấn công)\n2.Đế nhọn hơn(+1 sức bền bỉ)\n3.Đĩa nặng hơn(+20 hp)\n4.Nạp năng lượng(+1 năng lượng)')
pk = int(input('Chọn 1 trong các phụ kiện sau đây: '))
if(pk == 1):
    print('Bạn đã chọn thêm sắc bén!\n')
    atk += 5
elif(pk == 2):
    print('Bạn đã chọn đến nhọn hơn!\n')
    stm += 1
elif(pk == 3):
    print('Bạn đã chọn đĩa nặng hơn!\n')
    hp += 20
else:
    print('Bạn đã chọn nạp năng lượng!\n')
    en += 1
print('Trận đấu bắt đầu!')
while True:
    print('Chỉ số của bạn:\nHP:', hp, 'Sức chịu đựng:', stm, 'Năng lượng:', en)
    print('Chỉ số của đối phương:\nHP:', enhp, 'Sức chịu đựng', enstm, 'Năng lượng:', enen)
    print('Hướng dẫn trận đấu:\nChọn 1: Tấn công (gây sát thương và trừ máu đối phương)\nChọn 2: Phòng thủ (Giảm sát thương từ đối phương)\nChọn 3: Spin(tăng 1 hp)\nChọn 4: Nạp sức mạnh (+1 năng lượng, có 3 năng lượng sẽ được dùng skill)')
    import random 
    enhd = random.randint(1, 4)
    hd = int(input('Chọn hành động của bạn: '))
    if(hd == 1):
        print('Bạn đã chọn tấn công, đối phương bị trừ {} hp!'.format(atk))
        enhp -= atk
    if(hd == 2):
        print('Bạn đã chọn phòng thủ, sát thương của đối phương bị trừ 10')
        if (enhd == 1):
            hp += 10
    if(hd == 3):
        print('Bạn đã chọn Spin, lực bền bỉ của được cộng 1')
        stm += 1
    if(hd == 4):
        print('Bạn đã chọn nạp năng lượng, bạn được cộng 1 năng lượng')
        en += 1
    if(en == 3):
        en -= 3
        if (vp == 1):
            print('Kích hoạt skill tấn công! Đối phương bị trừ 50 hp!')
            enhp -= 50
        if(vp == 2):
            print('Kích hoạt skill phòng thủ! Bạn được tăng 50 hp!')
            hp += 50
        if(vp == 3):
            print('Kích hoạt skill bền bỉ! Bạn được tăng 2 lực bền bỉ và gây 35 sát thương cho đối phương!')
            stm += 2
            enhp -= 35
        if(vp == 4):
            print('Kích hoạt skill cân bằng! Sát thương của đối phương sẽ không ảnh hưởng và gây 40 sát thương!')
            enhp -= 40
    if(enhd == 1):
        print('Đối phương đã tấn công bạn, bạn bị mất {} hp'.format(enatk))
        if(en == 3 and vp == 4):
            hp += enatk
    if(enhd == 2):
        print('Đối phương đã phòng thủ, sát thương gây ra của bạn sẽ bị trừ đi 10')
        if(hd == 1):
            enhp += 10
    if(enhd == 3):
        print('Đối phương đã Spin, lực bền bỉ của phương tăng 1')
        enstm += 1
    if(enhd == 4):
        print('Đối phương đã nạp năng lượng, năng lượng đối phương tăng 1')
        enen += 1
    if(enen == 3):
        print('Kích hoạt skill đối phương, Bàn tay Hắc Ám!, Bạn bị trừ 35 máu và 2 lực bền bỉ! ')
        hp -= 35
        stm -= 2
    stm -= 1
    enstm -= 1
    if(enhp <= 0):
        print('Bạn đã chiến thắng với một pha nốc ao!')
        break
    if(enstm == 0):
        print('Bạn đã chiến thắng với một pha hết lực quay!')
        break
    if(hp <= 0):
        print('Đối phương đã chiến thắng với một pha nốc ao!\n Game over :(')
        break
    if(stm <= 0):
        print('Đối phương đã chiến thắng với một pha hết lực quay!\n Game over :(')
        break
    if(enhp <= 0 and hp <= 0):
        print('Trận kết thúc với hai pha nốc ao, không ai chiến thắng!')
        break
    if(enstm <= 0 and stm <=0):
        print('Trận đấu kết thúc với hai pha hết lực quay!')
        break
