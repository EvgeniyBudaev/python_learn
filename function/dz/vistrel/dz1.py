def whos_first(p1, p2):
    # ваше решение
    diff = p1.find('B') - p2.find('B')
    if diff < 0:
      return 'p1'
    elif diff > 0:
      return 'p2'
    else:
      return 'tie'  
   
print(whos_first(
  "   Bang!   ",
  "      Bang!   "
))    