import 'aoc.dart';

void main() {
  var input = inputAsLines(4, test: false);
  int ret = 0;

  // Part 1
  for (String line in input) {
    var pairs = parsePositiveIntsFromString(line);
    int x0 = pairs[0];
    int x1 = pairs[1];
    int y0 = pairs[2];
    int y1 = pairs[3];
    if ((x0 <= y0 && x1 >= y1) || (y0 <= x0 && y1 >= x1)) {
      ret += 1;
    }
  }
  print(ret);

  ret = 0;

  // Part 2
  for (String line in input) {
    var pairs = parsePositiveIntsFromString(line);
    int x0 = pairs[0];
    int x1 = pairs[1];
    int y0 = pairs[2];
    int y1 = pairs[3];
    var one = [for (var i = x0; i <= x1; i++) i].toSet();
    var two = [for (var i = y0; i <= y1; i++) i].toSet();
    if (one.intersection(two).length != 0) {
      ret += 1;
    }
  }
  print(ret);
}
