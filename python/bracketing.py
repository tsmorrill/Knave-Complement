w_1 = "10"

def knave_adj(*args):
    try:
        output = knave_pair(args[0], args[1])
    except IndexError as ex:
        output = knave_single(args[0])
        print(message)
    finally:
        return output

def knave_single(x:str):
    return x


def knave_pair(x:str, y:str):
    return x, y
