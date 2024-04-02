Here is three different solutions to a task where the program gets a syntax-wise consistent input for distributing inheritance.
The main challenge is figuring out the distribution rules and avoiding unnecessary computation.

The first solution "perinnönjako1" is in my opinion the best solution to the problem.
It utilizes floating-point numbers (f64) which allows for exceeding precision. A foreseaable problem with this is the inherit inaccuracy of floating-point numbers in computers. However in practice the inaccuracy would mean over distributing only fractions of cents.

The second and third solutions divide and round the amount down at each point in the distribution. This results in under distributing the money, but with the safety that we can never over distribute the money.

In the directories are a few example inputs in s.txt files. Try these out and see what the program prints in the standard output. You can also try to modify these as long as the modified input follows the allowed syntax.
