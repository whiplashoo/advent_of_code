import 'dart:io';

String inputAsString(int day, {test = false}) {
  if (test) return File('2022/day${day}t.txt').readAsStringSync();
  return File('2022/day${day}.txt').readAsStringSync();
}

List<String> inputAsLines(int day, {test = false}) {
  return inputAsString(day, test: test).split('\n');
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

List<int> parsePositiveIntsFromString(String line) {
  // Use a regex to get all integers in a string.
  return RegExp(r'\d+')
      .allMatches(line)
      .map((m) => int.parse(m.group(0)!))
      .toList();
}
