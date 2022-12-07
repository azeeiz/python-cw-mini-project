# write your code here


# court_type = input('What is your court?')
def padel_court_cost(court_type):
    if court_type == "indoor":
        return print (30)
    if court_type == "outdoor":
        return print (20)
# padel_court_cost(court_type)

# racket_brand = input('What racket brand would you like?')
def racket_cost(racket_brand):
    if racket_brand == "Bullpadel":
        return print (100)
    if racket_brand == "Nox":
        return print (140)
    if racket_brand == "Sixus":
        return print (200)
# racket_cost(racket_brand)

# ball_boxes = input('How many boxes do you want?')
def padel_ball_cost(ball_boxes):
    if ball_boxes == "box":
        return print (2)
    if ball_boxes == "two boxes":
        return print (3.5)
    if ball_boxes == "three boxes":
        return print (5)
# padel_ball_cost(ball_boxes)

def padel_game_cost():
    time = input("WHat time?")
    court_type = input("The court type")
    racket_brand = input('racket brand')
    ball_boxes = input('number of ball boxes')
    return print(f'Hours: {time}\n court_type: {court_type}\n racket_brand: {racket_brand}\n ball_boxes: {ball_boxes}')
padel_game_cost()