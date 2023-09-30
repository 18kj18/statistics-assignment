linenum = 0
with open("./data.csv", "r") as file:
    for line in file:
        total = 0
        linenum += 1
        freq = {}
        
        s = line.replace("\n", "").split(",")
        try:
            #Mean - Average & Frequency
            for num in s:
                total += int(num)
                freq[num] = freq.get(num,0) + 1
            avg = total/len(s)
            
            #Median - Middle
            med = s[int(len(s))//2]
            
            #Mode - Most frequent
            max_count = 0

            for num, count in freq.items():
                if count > max_count:
                    max_count = count
                    mode = num

            #Output
            print('\nLine', linenum) 
            print(f"The mean is {avg}")
            print(f"The median is {med}")
            print(f"The frequency is {freq}")
            print(f"The mode is {mode}")
            
        except:
            continue