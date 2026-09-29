print(''' window  middle  aisle      aisle   middle  window
   A       B       C          D       E       F''')

seats =          ['A1','B1','C1','D1','E1','F1',
              'A2','B2','C2','D2','E2','F2',
              'A3','B3','C3','D3','E3','F3',
              'A4','B4','C4','D4','E4','F4',
              'A5','B5','C5','D5','E5','F5',
              'A6','B6','C6','D6','E6','F6',
              'A7','B7','C7','D7','E7','F7',
              'A8','B8','C8','D8','E8','F8']

l = ['A1', 'B5','C8','F8','D6']
r=2
c=1
print(1,end='  ')
for i in seats:
    if c<6:
        if i in l:
            print('■',end='       ')
        else:
            print('□',end='       ')
        c+=1
    else:
        if i in l:
            print('■')
        
        else:
            print('□')
        if i != "F8":
            print(r,end='  ')
            r+=1
        c=1
        
    if c==4:
        print('   ',end='')
        
        