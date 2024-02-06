#love calci
name1=input("Enter your name:-")
name2=input("Enter your partner's name:-")
total=name1+name2
total_small=total.lower()
true=int(total_small.count('t')+total_small.count('r')+total_small.count('u')+total_small.count('e'))
love=int(total_small.count('l')+total_small.count('o')+total_small.count('v')+total_small.count('e'))
percent=str(true)+str(love)
percenta=int(percent)

if (percenta>100 and percenta<200):
    print(f"Your love percentage is {percenta}%,you guys are in a purest love😍😍💯")
elif (percenta<100 and percenta>50):
    print(f"Your love percentage is {percenta}%,You guys are lovelyy together👫♥♥")
elif(percenta<50):
    print(f"Your love percentage is {percenta}%,you guys should try dating.")
else:
    print(f"Your love percentage is {percenta}%,You have eternal love till the end of the earth❤️❤️👴👵🌎")
