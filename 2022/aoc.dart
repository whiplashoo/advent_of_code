import 'dart:io';

String inputAsString(int day) {
  return File('2022/day${day}.txt').readAsStringSync();
}

List<String> inputAsLines(int day) {
  return inputAsString(day).split('\n');
}

List<int> inputAsInts(int day) {
  return inputAsLines(day).map((line) => int.parse(line.trim())).toList();
}

void printMatrix(List<List<dynamic>> matrix) {
  for (var row in matrix) {
    print(row.join(' '));
  }
}

List<int> parseIntsFromString(String line) {
  // Use a regex to get all integers in a string.
  return RegExp(r'-?\d+')
      .allMatches(line)
      .map((m) => int.parse(m.group(0)!))
      .toList();
}
