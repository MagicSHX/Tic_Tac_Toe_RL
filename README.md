# Tic_Tac_Toe_RL
> Create a Tic Tac Toe game agent with Reinforcement Learning model

## Table of contents
* [General info](#general-info)
* [Demo](#demo)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
My insterest is in Reinforcement learning and multi-agent system, using project like this to practice and gain experience.

## Demo
![Example Demo](img/AI.gif)

## Technologies
* Python 3 - pytorch
* Python 3 - tkinter

## Setup
* Download project into local folder
* To play game against pre-trained AI, please open "Game UI.ipynb" and execute, you will see a window pops-up as per demo
* To try to train the Reinforcement Learning model from scratch/ last saved model, please open "RL_model.ipynb". There are few parameters inside can be setup before execution:

parameter setup:

button = 1: RL model + predict via latest model <br />
button = 0: Only predict via latest model <br />
existing setup: `button = 1` <br />
<br />
train_model_from_crash = 1: train model from scratch <br />
train_model_from_crash = 0: reload saved model last time and continue with training. <br />
existing setup: `train_model_from_crash = 0` <br />
<br />
How many Reinforcement learning loop will be trained: `main_loop_count = 20` <br />
Epoch size under each Reinforcement learning loop: `epoch_size = 3000` <br />
How many epochs to print out 1 loss: `steps_for_printing_out_loss = 1000` <br />
Model learning rate: `learning_rate = 0.2` <br />
DQ learning rate: `DQ_ratio = 0.75` <br />

## Features
List of features ready:
* Reinforcement Learning model, to let AI plays against last version of AI, to gain training data. Then enahnced training data will be used to continue training latest AI model.
* A simple game UI has been developed, to provide an interface for human player plays with AI model.
* Machine learning model used for this model is light level(pt model is only 24 kb), as game is not too complex, it has to be enhanced for a more complex game 

To-do list:
* Will develop a "Connect Four" game with Reinforcement learning model. Compared with this game here, game rule itself will be more fair to both players.
* Add some noise(random steps) into training output, so that AI can auto-generate more scenarios, without relying too much on initial training scenario.

## Status
Project is: _in progress_

## Inspiration
My insterest is in Reinforcement learning and multi-agent system, using project like this to practice and gain experience.

## Contact
Created by 'shaohongxu0509@gmail.com' - feel free to contact me!