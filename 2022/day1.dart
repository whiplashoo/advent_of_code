import 'dart:math';

import 'aoc.dart';

void main() {
  var input = inputAsLines(1);
  List<int> cals = [];

  // Part 1
  int bucket = 0;
  for (String i in input) {
    if (i.isEmpty) {
      cals.add(bucket);
      bucket = 0;
    } else {
      bucket += int.parse(i);
    }
  }
  print(cals.reduce(max));

  // Part 2
  cals.sort((b, a) => a.compareTo(b));
  print(cals.sublist(0, 3).reduce((a, b) => a + b));
}
