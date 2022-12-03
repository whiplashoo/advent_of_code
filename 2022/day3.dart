import 'aoc.dart';

int getPriority(String letter) {
  List<String> alphabet = [];
  for (int i = 97; i <= 122; i++) {
    alphabet.add(String.fromCharCode(i));
  }
  for (int i = 65; i <= 90; i++) {
    alphabet.add(String.fromCharCode(i));
  }
  return alphabet.indexOf(letter) + 1;
}

void main() {
  var input = inputAsLines(3, test: false);
  int score = 0;

  // Part 1
  for (String line in input) {
    final first = line.substring(0, (line.length / 2).ceil());
    final second = line.substring((line.length / 2).ceil(), line.length);
    for (var i = 0; i < first.length; i++) {
      final letter = first[i];
      if (second.contains(letter)) {
        score += getPriority(letter);
        break;
      }
    }
  }
  print(score);

  // Part 2
  score = 0;
  for (var i = 0; i < input.length; i += 3) {
    for (var j = 0; j < input[i].length; j++) {
      final letter = input[i][j];
      if (input[i + 1].contains(letter) && input[i + 2].contains(letter)) {
        score += getPriority(letter);
        break;
      }
    }
  }
  print(score);
}
