import 'aoc.dart';

void main() {
  var input = inputAsLines(2);
  int score = 0;

  var myPlay = {"X": 1, "Y": 2, "Z": 3};
  var wins = ["AY", "BZ", "CX"];
  var draws = ["AX", "BY", "CZ"];
  var losses = ["AZ", "BX", "CY"];

  // Part 1
  for (String line in input) {
    String me = line[2];
    String play = line.replaceAll(" ", "");
    if (wins.contains(play)) {
      score += 6;
    } else if (draws.contains(play)) {
      score += 3;
    }
    score += myPlay[me]!;
  }
  print(score);

  // Part 2
  score = 0;
  var strategy = {"X": losses, "Y": draws, "Z": wins};
  var res = {"X": 0, "Y": 3, "Z": 6};
  for (String line in input) {
    String opp = line[0];
    String expected = line[2];
    for (String play in strategy[expected]!) {
      if (play[0] == opp) {
        score += myPlay[play[1]]!;
      }
    }
    score += res[expected]!;
  }
  print(score);
}
