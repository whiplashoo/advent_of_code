import 'dart:collection';

import 'aoc.dart';

void main() {
  var input = inputAsLines(5, test: false);

  // Part 1
  int stacksCount = ((input[0].length + 1) / 4).ceil();
  List<Queue<String>> stacks = [];
  for (int i = 0; i < stacksCount; i++) {
    stacks.add(Queue());
  }

  for (String line in input) {
    if (line.isEmpty || line[1] == "1") {
      continue;
    } else if (line[0] == "m") {
      var p = parsePositiveIntsFromString(line);
      int fromStack = p[1] - 1;
      int toStack = p[2] - 1;
      int count = p[0];
      for (int i = 0; i < count; i++) {
        var el = stacks[fromStack].removeLast();
        stacks[toStack].addLast(el);
      }
    } else {
      int stackNum = 0;
      int i = 0;
      while (i < line.length) {
        var el = line.substring(i, i + 3);
        if (el != "   ") {
          stacks[stackNum].addFirst(el);
        }
        i += 4;
        stackNum += 1;
      }
    }
  }

  String ret = "";
  for (Queue stack in stacks) {
    ret += stack.last.replaceAll("[", "").replaceAll("]", "");
  }
  print(ret);
  // Part 2

  stacks.clear();
  for (int i = 0; i < stacksCount; i++) {
    stacks.add(Queue());
  }

  for (String line in input) {
    if (line.isEmpty || line[1] == "1") {
      continue;
    } else if (line[0] == "m") {
      var p = parsePositiveIntsFromString(line);
      int fromStack = p[1] - 1;
      int toStack = p[2] - 1;
      int count = p[0];
      Queue moveQueue = Queue();
      for (int i = 0; i < count; i++) {
        var el = stacks[fromStack].removeLast();
        moveQueue.addLast(el);
      }
      for (int i = 0; i < count; i++) {
        stacks[toStack].addLast(moveQueue.removeLast());
      }
    } else {
      int stackNum = 0;
      int i = 0;
      while (i < line.length) {
        var el = line.substring(i, i + 3);
        if (el != "   ") {
          stacks[stackNum].addFirst(el);
        }
        i += 4;
        stackNum += 1;
      }
    }
  }

  ret = "";
  for (Queue stack in stacks) {
    ret += stack.last.replaceAll("[", "").replaceAll("]", "");
  }
  print(ret);
}
