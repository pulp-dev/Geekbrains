sec = int(input())
hrs = sec // 3600
mins = sec % 3600 // 60
sec = sec % 60
print (f"{hrs}:{mins}:{sec}")