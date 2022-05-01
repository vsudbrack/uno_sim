# uno_sim
Simulating a match of Uno to discuss different strategies


## Strategies

  Play by color: first try to find a card with the same color.

  Play by number: first try to find a card with the same number.

## Results by now
Run 100'000 games, and the % of win:
  - 01.021%: game ties (run out of cards in the main deck)
  - 54.555%: player prioritizing cards of the same color wins
  - 44.424%: player prioritizing cards of the same number wins
 
### Preliminar interpretation:
By playing a card with a color equal to the color of the card on the table, you increase your chances of winning by 10% against a player who prioritizes playing a card with the same number of the card on the table. One possible explanation is that to cover all possible numbers one needs (at least) 10 cards in one's hand, while one can cover all colors with as few as 4 cards. So by switching numbers in the table rather than changing its colors, one's opponent will find it harder to have a matching number. 


## Future prospects:
### In code:
  - In strategy by color, always try to play a different number.
  - In strategy by number, always try to play a different color. 
  - Play equal cards together. 
  - Add special cards (?)
  - When the main deck ends, suffles the table cards and add to the main deck. No ties possible. 
  
 ### In analysis:
  - Analyze each strategy against a player with no strategy (plays random card whenever possible). 
