#import matplotlib.pyplot as plt

#plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
#plt.axis((0, 6, 0, 20))
#plt.show()

checking_one = 0

misc = 375
annunal = 45000
monthly = (annunal / 12)
biweekly = ((monthly / 2)- misc)

checking_one = (biweekly)
print(checking_one)

amt = 456
final = ( ((checking_one + amt) - checking_one) / checking_one  * 100 )
"""
decrase a->  ((amt / checking)*100  )
incrase algo = -->  (( (checking + amt) - checking ) / checking * 100  )

"""
print( final )


diff = ( ((amt / checking_one)* 100) )
decrease =  ( ((checking_one - amt) / checking_one * 100) )
print("the diff/you took is {}% and the decrease is {}%".format(int(diff),100 - int(decrease)))
