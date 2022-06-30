import argparse

from functions.agent import Agent
from functions.game_ai import SnakeGameAI
from functions.additional_functions import plot

parser = argparse.ArgumentParser()
parser.add_argument("--width", help="set game window's width (default=640)", type=int)
parser.add_argument("--height", help="set game window's height (default=480)", type=int)
parser.add_argument("--num-obstacles", help="set the number of obstacles within the game (default=5)", type=int)

args = parser.parse_args()

if args.width:
    width=args.width
else:
    width=640

if args.height:
    height=args.height
else:
    height=480

if args.num_obstacles or args.num_obstacles==0:
    num_obstacles=args.num_obstacles
else:
    num_obstacles=5

if __name__ == '__main__':
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI(width=width, height=height, num_obstacles=num_obstacles)
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