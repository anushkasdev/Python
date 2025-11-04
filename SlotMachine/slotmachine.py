MAX_LINES = 4
MAX_BET = 50
MIN_BET = 1

rows = 3
cols = 3
def getAmount(): 
  while True : 
    amount = input("Please enter the amount for deposit : $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Please enter a valid number.")
    else:
      print("Please enter a valid amount only.")
  return amount

def getLines(): 
  while True : 
    lines = input("Please enter the number of lines : ")
    if lines.isdigit():
      lines = int(lines)
      if 1 <=lines<= MAX_LINES:
        break
      else:
        print(f"Please enter the lines between 1 and ${MAX_LINES}.")
    else:
      print("Please enter a valid line from 1 to " + int(MAX_LINES)+ ".")
  return lines
# for betting to different amounts
def getBet(): 
  while True : 
    bet = input("Please enter the amount for Betting : $")
    if bet.isdigit():
      bet = int(bet)
      if MIN_BET<=bet<=MAX_BET:
        break
      else:
        print(f"Please enter a valid bet in the range from {MIN_BET} and {MAX_BET}.")
    else:
      print("Please enter a valid amount only.")
  return bet

def main():
  amount = getAmount()
  lines = getLines()
  bet = getBet()
  total_bet = bet*lines
  amount_left = amount - total_bet
  print(f"You are betting ${bet} on {lines} lines, with a total bet amount of ${total_bet}")
  print(f"Total amount left is : ${amount_left}")
main()
