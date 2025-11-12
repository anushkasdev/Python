MAX_LINES = 4
MAX_BET = 50
MIN_BET = 1
import random

rows = 3
cols = 3

symbol_count = {
  "A": 2,
  "B": 4, 
  "C": 6,
  "D": 8
}

symbol_value = {
  "A": 5,
  "B": 4, 
  "C": 3,
  "D": 2
}

def checkwinnings(columns, lines, bets, values):
  winnnings = 0
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol != symbol_to_check:
        break
    else:
      winnnings+= values[symbol] * bets
    return winnnings


def get_slot_machine_spins(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)
  
  columns = []
  for col in range(cols):
    column = []
    current_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(all_symbols)
      current_symbols.remove(value)
      column.append(value)
    columns.append(column)
  return columns


def print_slot_machine(columns):
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i != len(columns) - 1:
        print(column[row], end = "|")
      else:
        print(column[row], end = "")
    print()
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
  slots = get_slot_machine_spins(rows, cols, symbol_count)
  print_slot_machine(slots)
main()
