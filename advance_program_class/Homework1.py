w, h = 10, 5
x, y = 2, 3

while True:
    
    print('當前座標： (', x, ',', y, ')')
    i, j = 0, 0
    while i < h :
      j=0
      while j < w :
        if i==h-y and j+1==x :
          print('*',end='') 
        else :
          print('-',end='') 
        j+=1
        
      print('');
      i+=1
    
    control = input('按 W/A/S/D 來移動星星(q 結束)！ ')
    control = control.lower()
    
    if control == 'w' and y<h:
        y+=1
    elif control == 's' and y>1:
        y-=1
    elif control == 'a' and x>1:
        x-=1
    elif control == 'd' and x<w:
        x+=1
    elif control == 'q':
        break