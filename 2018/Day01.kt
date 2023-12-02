package src.main.kotlin

import println
import readInput

fun main() {
    fun part1(input: List<String>): Int {
        return input.sumOf {
            it.toInt()
        }
    }

    fun part2(input: List<String>): Int {
        var i = 0
        var freq = 0
        val frequencies = mutableListOf<Int>()
        do {
            freq += input[i].toInt()
            if (freq in frequencies) {
                return freq
            }
            frequencies.add(freq)
            i++
            if (i == input.size) {
                i = 0
            }
        } while (true)
    }

    val input = readInput("Day01")
    part1(input).println()
    part2(input).println()
}