# courageCards

## A small CLI tool that takes a sample of data and proccesses it to output a result in a CSV file
### A new psychometric level is released, in which:
1. A deck of red and green cards is shuffled.
2. A candidate draws the top card.
3. If it is green they get one point.
4. They can then choose to draw another card or bank their points.
5. If they bank their points, they keep their points and the deck is shuffled.
6. If they draw another green card, they get another point.
7. If they draw a red card, they lose all their unbanked points and the deck is shuffled.
8. They will do this a maximum of 45 times.

### In the set of data from the new level (test_level_data.json), the `event` column refers to the action taken by the candidate, and can contain the following strings:
`start` - The level start time
`shuffle_cards` - The deck is shuffled.
`green_card` - The candidate selected a green card and gets one point
`red_card` - The candidate selected a red card and lost their unbanked points
`banked` - The candidate opted to bank their points, preventing their loss in the instance of a red card being selected.
`end` - The level end time

### The result contains:
* The total time spent on the level
* The mean number of green cards selected across all rounds of play
* The total points the candidate has received

Full description in task_description.pdf
Test data in test_level_data.json
