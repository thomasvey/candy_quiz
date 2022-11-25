# Candy Quiz
This Game is made for an Raspery-Pi
## Description

Its a conzentration game for a smal class with one Teacher. 



All Plyers, Techer and Kids, hold a Switch in there Hands. 

The Techer reads a Text lound. When there is a wrong word, he will press is Botton in a hidden way. 

The Kids read the same Text, when the Techer reads a Wrong word, the Kids also press they Botton. 

In the end the Rsult is Plottet to the Screen. For each right pressed Button the kid can gat a smal candy. 

## How to run
1. clone this respository
```bash
git clone https://github.com/thomasvey/candy_quiz.git
```
2. install requirements
```bash
pip install -e requirement.txt
```

3. Change the Names and the Game length in the candy_game.py

4. run the Game
```bash
python candy_game.py
```

## Tips
To debounce the Switch, add a 0.1uF capacitor across youre Switch