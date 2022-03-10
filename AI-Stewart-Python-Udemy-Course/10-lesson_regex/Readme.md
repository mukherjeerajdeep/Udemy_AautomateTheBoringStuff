This Chapter is for the regex tutorial

```doctest
Groups are created in regex strings with parentheses.
The first set of parentheses is group 1, the second is 2, and so on.
Calling group() or group(0) returns the full matching string, group(1) returns group 1's matching string, and so on.
Use \( and \) to match literal parentheses in the regex string.
The | pipe can match one of many possible groups.
```

```doctest
The ? says the group matches zero or one times.
The * says the group matches zero or more times.
The + says the group matches one or more times.
The curly braces can match a specific number of times.
The curly braces with two numbers matches a minimum and maximum number of times.
Leaving out the first or second number in the curly braces says there is no minimum or maximum.
"Greedy matching" matches the longest string possible, "nongreedy matching" (or "lazy matching") matches the shortest string possible.
Putting a question mark after the curly braces makes it do a nongreedy/lazy match.
```
