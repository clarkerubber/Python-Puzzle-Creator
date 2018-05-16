# Python-Puzzle-Creator

## About

This is a python application dedicated to creating chess puzzles locally for your personal games.

## Installation

This script requires the *Python-Chess* library to run, as well as a copy of *Stockfish*


### Install Python Chess

`pip install python-chess`

### Setup

MacOS / Linux : `sh build-stockfish.sh` to obtain the current lichess Stockfish instance.

## Launching Application

`python main.py <filepath to pgn> <#Threads = 4> <Hash (MBytes) = 2048> --quiet`

JSON puzzle output will be in the file `generated-puzzles` in the `Python-Puzzle-Creator` directory

