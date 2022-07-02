import argparse
import sys

from functions.agent import Agent
from functions.game_ai import SnakeGameAI
from functions.additional_functions import plot

parser = argparse.ArgumentParser()
parser.add_argument("--width", help="set the width of the game window (default=640)")
parser.add_argument("--height", help="set the height of the game window (default=480)")
parser.add_argument("--num-obstacles", help="set the number of obstacles within the game (default=5)")
parser.add_argument("--speed", help="set the speed of the snake (default=100)")
args = parser.parse_args()

if args.width:
    try :
        width=int(args.width)
    except :
        print('Argument Type Error: width should be an integer.')
        sys.exit()
else:
    width=640

if args.height:
    try :
        height=int(args.height)
    except :
        print('Argument Type Error: height should be an integer.')
        sys.exit()
else:
    height=480

if args.num_obstacles or args.num_obstacles==0:
    try :
        num_obstacles=int(args.num_obstacles)
    except :
        print('Argument Type Error: num_obstacles should be an integer.')
        sys.exit()
else:
    num_obstacles=5

if args.speed:
    try :
        speed=int(args.speed)
    except :
        print('Argument Type Error: speed should be an integer.')
        sys.exit()
else:
    speed=100

if __name__ == '__main__':
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI(num_obstacles=num_obstacles, width=width, height=height, speed=speed)
    while True:
        # get current state of the game 
        old_state = game.get_state()

        # predict next move
        next_move = agent.get_action(old_state)

        # play the predicted next move
        game_over, reward, score = game.play(next_move, agent.n_games)

        # get new state of the game
        new_state = game.get_state()

        # train short memory
        agent.train_short_memory(old_state, next_move, reward, new_state, game_over)

        # remember
        agent.remember(old_state, next_move, reward, new_state, game_over)

        if game_over:
            # reset game
            game.reset()
            agent.n_games +=1

            # train long memory
            agent.train_long_memory()

            # update record
            if score > record:
                record = score

            print('Game', agent.n_games, 'Score', score, 'Record:', record)

            # plot scores
            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)
            plot(plot_scores, plot_mean_scores)
