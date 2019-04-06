person = {
    "name" : "ten cua mot nguoi nao day",
    "nyc" : "nguoi yeu cu",
    "dev": "lap trinh vien",
    "aye": "anh yeu em",
    "teckid": "trung tam day hoc lap trinh"
}

for word in person:
    print(word, end=' ')

print()
input_word = input("code? ")
mean = person[input_word] 

print(mean)
    
