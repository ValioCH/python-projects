def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_row = []
    second_row = []
    dash_row = []
    answer_row = []

    for problem in problems:
        first, operator, second = problem.split()

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not first.isdigit() or not second.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(first), len(second)) + 2
        top = first.rjust(width)
        bottom = operator + second.rjust(width - 1)
        dash = "-" * width

        # ✅ Append to rows
        first_row.append(top)
        second_row.append(bottom)
        dash_row.append(dash)

        if show_answers:
            if operator == "+":
                result = str(int(first) + int(second))
            else:
                result = str(int(first) - int(second))
            answer_row.append(result.rjust(width))

    arranged_problems = (
        "    ".join(first_row) + "\n" +
        "    ".join(second_row) + "\n" +
        "    ".join(dash_row)
    )

    if show_answers:
        arranged_problems += "\n" + "    ".join(answer_row)

    return arranged_problems
