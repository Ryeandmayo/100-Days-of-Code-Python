import math
def paint_calc(height, width, cover):
  cans = (height * width) / cover
  round_up_cans = math.ceil(cans)
  print(f"You'll need {round_up_cans} cans of paint.")




h = int(input("Height of wall: ")) # Height of wall (m)
m = int(input("Width of wall: ")) # Width of wall (m)
coverage = int(input("How many square meters can one can of paint cover: "))
paint_calc(height=test_h, width=test_w, cover=coverage)