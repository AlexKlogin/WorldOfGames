import Utils

def add_score(difficulty):
    try:
        with open('Scores.txt', "r") as file:
            current_score = int(file.read())
            try:
                with open('Scores.txt', 'w') as file:
                    file.write(str(current_score + (difficulty * 3) + 5))
            except:
                print('Could not write to  Scores.txt')
    except:
        print('Could not open Scores.txt. Creating new one.')
        try:
            with open('Scores.txt', 'w') as file:
                file.write(str((difficulty * 3) + 5))
        except:
                print('Could not write to  Scores.txt')







