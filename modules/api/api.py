import chess
import logging
import re
import time
from modules.bcolors.bcolors import bcolors

# def get_pgn(token):
#     logging.debug(bcolors.WARNING + "Getting new game..." + bcolors.ENDC)
#     success = False
#     while not success:
#         try:
#             response = requests.get('https://en.lichess.org/training/api/game.pgn?token=' + token)
#             success = True
#         except requests.ConnectionError:
#             logging.debug(bcolors.WARNING + "CONNECTION ERROR: Failed to get new game.")
#             logging.debug("Trying again in 30 sec" + bcolors.ENDC)
#             time.sleep(30)
#         except requests.exceptions.SSLError:
#             logging.warning(bcolors.WARNING + "SSL ERROR: Failed to get new game.")
#             logging.debug("Trying again in 30 sec" + bcolors.ENDC)
#             time.sleep(30)


#     try:
#         from StringIO import StringIO
#     except ImportError:
#         from io import StringIO

#     return StringIO(response.text)

def post_puzzle(puzzle):
    logging.info(bcolors.OKBLUE + str(puzzle.to_dict()) + bcolors.ENDC)
    with open('generated-puzzles','a+') as f:
        f.write(str(puzzle.to_dict()))
        f.write("\n\n")
