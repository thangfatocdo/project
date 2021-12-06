import random
def enter_data():
    while True:
        n = input("nhập vào số bạn đoán: ")
        if n.isnumeric():
                n= int(n)
                if n > 0:
                    return n
        else:
            print("Số bạn nhập không đúng! ")
def intro():
    playername= input("Vui lòng nhập tên của bạn: ")
    print("Xin chào",playername,", hiện giờ tôi đang nghĩ đến một số từ 1 đến 10, nếu bạn đoán đúng bạn sẽ thắng, bạn có 4 lần đoán")
def guessesnumber():
    answer= random.randint(1,10) #bien answer la mot so nguyen ngau nhien tu 1 den 20
    guessestaken= 0
    for guessestaken in range(4): #ham range trong loop for luon dung truoc so cuoi cung, vi vay nho cong them 1 neu muon no dung ngay so da chon    
        a = enter_data()
        PlayerGuesses = a     
        if PlayerGuesses> answer:
            print("Số bạn đoán cao hơn số tôi nghĩ. xin hãy đoán lại!")
        if PlayerGuesses< answer:
            print("Số bạn đoán thấp hơn số tôi nghĩ. xin hăy đoán lại!")
        if PlayerGuesses ==  answer:
            break #ngung vong lap vi nguoi choi da doan dung
    if PlayerGuesses ==  answer:
            guessestaken= str(guessestaken+1) #doi bien gusessestaken thanh kieu string de co ket hop voi kieu string dong ben duoi
                                          #boi vi bien guesttaken bat dau tu so 0 nen khi ta hien thi no se bi hut mat mot so
                                          #vd nhu player doan trung ngay trong lan dau tien, neu ta khong cong guessestaken them 1 thi kq hien thi se la 0 thay vi 1
            print("chúc mừng, bạn đă đoán đúng")
            print("bạn đă đoán",guessestaken,"lần")
    if PlayerGuesses != answer:
       print('haha mày thua rồi, là số ',answer,' nhé')
choilai= 'co'
while choilai == 'co' or choilai == 'có':
    intro()
    guessesnumber()
    print('bạn có muốn chơi lại không?')
    choilai = input()
    
    

    
    


