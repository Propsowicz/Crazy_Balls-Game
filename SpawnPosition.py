import random



def spawn_pos_X(player_X, windowX):
    X1 = player_X - 100
    X2 = player_X + 100
    if X1 >= 60 and X2 <= (windowX - 60):
        spawn_X = random.choices((random.randint(60, X1), random.randint(X2, windowX - 60)))[0]
    elif X1 < 60:
        spawn_X = 0 + 60
    else:
        spawn_X = windowX - 60

    return spawn_X


def spawn_pos_Y(player_Y, windowY):
    Y1 = player_Y - 100
    Y2 = player_Y + 100
    if Y1 >= 60 and Y2 <= (windowY - 60):
        spawn_Y = random.choices((random.randint(60, Y1), random.randint(Y2, windowY - 60)))[0]
    elif Y1 < 60:
        spawn_Y = 0 + 60
    else:
        spawn_Y = windowY - 60

    return spawn_Y
