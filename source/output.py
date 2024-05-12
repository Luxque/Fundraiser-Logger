def printData(data: tuple) -> None:
    title, owner, raised, goal = data
    progress = raised / goal * 100

    quotient = raised // goal
    remainder = raised % goal
    nominator = 0

    for i in range(20):
        if i / 20 <= remainder / goal <= (i+1) / 20:
            nominator = i
            break

    print("\n" + "─" * 110 + "\n")

    print("Project Title:", title)
    print("Project Owner:", owner)
    print("Raised Fund:", str(raised), "JPY")
    print("Goal Fund:", str(goal), "JPY")
    print("Progress:", f"{progress:.3f}%\n")

    for i in range(quotient):
        print("[" + "■" * 20 + "]", end="")
        if (i+1) % 5 == 0 and remainder != 0:
            print("")
    if nominator != 0:
        print("[" + "▶" * nominator + "▷" * (20 - nominator) + "]\n")
    else:
        print("")

    print("\n" + "─" * 110 + "\n")


if __name__ == '__main__':
    print("This is not the main Python script. Please use 'main.py' in this directory.")