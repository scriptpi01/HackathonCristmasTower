nob = int(input())
height = input().split()
wh = input().split()
if len(height) == len(wh):

  total = []
  total.extend(height)
  for i in range(len(total)):
    total[i] = int(total[i])
  # for i in range(nob):
  #   for j in range(int(height[i])):
  #     print('*'*(int(wh[i])))

  # for i in range(max(total)):
  #   for j in range(nob):
  #     if int(wh[j]) > int(wh[j-1]) > int(wh[j-2]):
  #       print('*'*int(wh[0]), ' '*9, '*'*int(wh[1]), ' '*9, '*'*int(wh[2]))
  if max(total) > 5:
    start = max(total)
  else:
    start = 5
  for i in range(start, 0, -1):
    for j in range(nob):
      if i == 1:
        if i > int(height[j]):  
          # print(' '*int(wh[j]), ' '*3, 'l', ' '*3, end=' ')
          if nob == height.index(height[j])+1 :
            print(' '*int(wh[j]) , end=' ')
          else:
            print(' '*int(wh[j]), ' '*3, 'l', ' '*3, end=' ')
        elif i <= int(height[j]):
          # print('*'*int(wh[j]), ' '*3, 'l', ' '*3, end=' ')
          if nob == height.index(height[j])+1 :
            print('*'*int(wh[j]) , end=' ')
          else:
            print('*'*int(wh[j]), ' '*3, 'l', ' '*3, end=' ')

      elif i ==2:
        if i > int(height[j]):
          # print(' '*int(wh[j]), ' '*0, '-oxoxo-', ' '*0 ,end=' ')
          if nob == height.index(height[j])+1 :
            print(' '*int(wh[j]) , end=' ')
          else:
            print(' '*int(wh[j]), ' '*0, '-oxoxo-', ' '*0 ,end=' ')
        elif i <= int(height[j]):
          # print('*'*int(wh[j]), ' '*0, '-oxoxo-', ' '*0 ,end=' ')
          if nob == height.index(height[j])+1 :
            print('*'*int(wh[j]) , end=' ')
          else:
            print('*'*int(wh[j]), ' '*0, '-oxoxo-', ' '*0 ,end=' ')
      elif i ==3:
        if i > int(height[j]):
          # print(' '*int(wh[j]), ' '*1, '-oxo-', ' '*1 ,end=' ')
          if nob == height.index(height[j])+1 :
            print(' '*int(wh[j]) , end=' ')
          else:
            print(' '*int(wh[j]), ' '*1, '-oxo-', ' '*1 ,end=' ')
        elif i <= int(height[j]):
          # print('*'*int(wh[j]), ' '*1, '-oxo-', ' '*1 ,end=' ')
          if nob == height.index(height[j])+1 :
            print('*'*int(wh[j]) , end=' ')
          else:
            print('*'*int(wh[j]), ' '*1, '-oxo-', ' '*1 ,end=' ')
      elif i == 4:
        if i > int(height[j]):
          # print(' '*int(wh[j]), ' '*2, '-o-', ' '*2 ,end=' ')
          if nob == height.index(height[j])+1 :
            print(' '*int(wh[j]) , end=' ')
          else:
            print(' '*int(wh[j]), ' '*2, '-o-', ' '*2 ,end=' ')
        elif i <= int(height[j]):
          # print('*'*int(wh[j]), ' '*2, '-o-', ' '*2 ,end=' ')
          if nob == height.index(height[j])+1 :
            print('*'*int(wh[j]) , end=' ')
          else:
            print('*'*int(wh[j]), ' '*2, '-o-', ' '*2 ,end=' ')
      elif i ==5:
        if i > int(height[j]):
          # print(' '*int(wh[j]), ' '*3, '-', ' '*3 ,end=' ')
          if nob == height.index(height[j])+1 :
            print(' '*int(wh[j]) , end=' ')
          else:
            print(' '*int(wh[j]), ' '*3, '-', ' '*3 ,end=' ')
        elif i <= int(height[j]):
          # print('*'*int(wh[j]), ' '*3, '-', ' '*3 ,end=' ')
          if nob == height.index(height[j])+1 :
            print('*'*int(wh[j]) , end=' ')
          else:
            print('*'*int(wh[j]), ' '*3, '-', ' '*3 ,end=' ')
      else:
        if i > int(height[j]):
          print(' '*int(wh[j]), ' '*3, '-', ' '*3 ,end=' ')
        elif i <= int(height[j]):
          print('*'*int(wh[j]), ' '*3, '-', ' '*3 ,end=' ')
    print('')


  # if i > int(height[j]):
  #         print(' '*int(wh[j]),' '*10 ,end='')
  #       elif i <= int(height[j]):
  #         print('*'*int(wh[j]),' '*10, end='')



  # print('*'*int(wh[0]), ' '*9, '*'*0, ' '*9, '*'*0)
  # print('*'*int(wh[0]), ' '*9, '*'*int(wh[1]), ' '*9, '*'*0)
  # print('*'*int(wh[0]), ' '*9, '*'*int(wh[1]), ' '*9, '*'*int(wh[2]))
  # print('*'*int(wh[0]), ' '*9, '*'*int(wh[1]), ' '*9, '*'*int(wh[2]))
  # print('*'*int(wh[0]), ' '*9, '*'*int(wh[1]), ' '*9, '*'*int(wh[2]))
  # print('*'*int(wh[0]), ' '*9, '*'*int(wh[1]), ' '*9, '*'*int(wh[2]))
  # print('*'*int(wh[0]), ' '*9, '*'*int(wh[1]), ' '*9, '*'*int(wh[2]))
  # print('*'*int(wh[0]), ' '*9, '*'*int(wh[1]), ' '*9, '*'*int(wh[2]))
  # print('*'*int(wh[0]), ' '*9, '*'*int(wh[1]), ' '*9, '*'*int(wh[2]))

  #base
  base = 0
  for i in range(nob):
    base += int(wh[i])
  base = base+(11*(len(wh)-1))
  print("")
  print('*'*base)

  #number
  number = 0
  print("")
  for i in range(nob):
    number += (int(height[i])*int(wh[i]))+int(wh[i])
  number = number+((len(height)-1)*11)
  print(number)


else:
  print('0')
