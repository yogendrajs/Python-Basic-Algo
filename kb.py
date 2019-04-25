question_list=["1.Which country is Delhi located in?", "2.What is the capitalf of India?", "3.Who is the prime minister of India", "4.Who is the chief minister of UP", "5.Who is GenSec",]
option1=["India", "Chandigarh", "Narendra Modi", "Venkaiyah Naidu", "Jai"]
option2=["USA", "Bhopal", "Rajendra Prasad", "Yogi", "Ravi"]
option3=["France", "Delhi", "Manmohan", "Kejriwal", "Sundar"]
option4=["Korea", "Jaipur", "Jawahar", "Mayank", "Ajay"]
ans_key=["India", "Delhi","Narendra Modi", "Yogi", "Ajay"]
well=["aapka question Rs.1000 ke liye aapki screen per yeh raha", "agla question Rs.5000 ke liye aapki screen pe yeh raha", "agla question Rs.10000 ke liye aapki screen pe yeh raha", "agla question Rs.20000 ke liye aapki screen pe yeh raha", "agla question Rs.50000 ke liye aapki screen pe yeh raha"]
tube=["aap jeet chuke hai Rs.1000", "aap jeet chuke hain Rs. 5000", "aap jeet chuke hain Rs. 10000", "aap jeet chuke hain Rs.20000","aap jeet chuke hain Rs.50000"]
index=0
i = 0
a = ['','','pehla','dusra']
while index<len(question_list):
    if i < 2:
        print well[index]
        print question_list[index]
        print "A. " + option1[index]
        print "B. " + option2[index]
        print "C. " + option3[index]
        print "D. " + option4[index]
        user=raw_input(" ")
        if user==ans_key[index]:
            print "aapka jawab sahi hai"
            print tube[index]
            index=index+1
            i = i + 1

        else:
            print "aapka jawab galat hai"
            print "aap KBC haar chuke hain"
            break
    else:
        print 'aap'+ a[i] + 'padao par kar gye ho'
        i = 0
        continue