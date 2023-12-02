def day2_1(file):
    score = 0
    for line in file:
        opponent, you = line.strip().split(' ')
        match you:
            case 'X': score += 1
            case 'Y': score += 2
            case 'Z': score += 3
        match evaluate_game(opponent, you):
            case 'loss': print('L')
            case 'draw': score += 3
            case 'win': score += 6
    print(score)


def evaluate_game(opponent, you):
    match opponent, you:
        case 'A', 'X': return 'draw'
        case 'A', 'Y': return 'win'
        case 'A', 'Z': return 'loss'

        case 'B', 'X': return 'loss'
        case 'B', 'Y': return 'draw'
        case 'B', 'Z': return 'win'

        case 'C', 'X': return 'win'
        case 'C', 'Y': return 'loss'
        case 'C', 'Z': return 'draw'


def day2_2(file):
    score = 0
    for line in file:
        opponent, result = line.strip().split(' ')
        match result:
            case 'X': print('L')
            case 'Y': score += 3
            case 'Z': score += 6
        match choose_move(opponent, result):
            case 'rock': score += 1
            case 'paper': score += 2
            case 'scissors': score += 3
    print(score)


def choose_move(opponent, result):
    match opponent, result:
        case 'A', 'X': return 'scissors'
        case 'A', 'Y': return 'rock'
        case 'A', 'Z': return 'paper'

        case 'B', 'X': return 'rock'
        case 'B', 'Y': return 'paper'
        case 'B', 'Z': return 'scissors'

        case 'C', 'X': return 'paper'
        case 'C', 'Y': return 'scissors'
        case 'C', 'Z': return 'rock'


def main():
    file = open("day2.txt", "r")
    day2_2(file)


if __name__ == "__main__":
    main()
