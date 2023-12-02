import java.io.File

fun main() {
    fun part1(input: List<String>): Int {
        var claims = mutableListOf<Claim>()
        for (line in input) {
            var l = line.replace(Regex("#| |x|: |@|,"), "_")
            l.split("_").println()
        }
        return 0
    }

    fun part2(input: List<String>): Int {
        TODO()
    }

    val input = readInput("Day03t")
    part1(input).println()
    part2(input).println()
}

data class Claim(
        val id: Int,
        val x: Int,
        val y: Int,
        val w: Int,
        val h: Int,
)

/** Reads lines from the given input txt file. */
fun readInput(name: String) = File("./", "$name.txt").readLines()

/** The cleaner shorthand for printing output. */
fun Any?.println() = println(this)
