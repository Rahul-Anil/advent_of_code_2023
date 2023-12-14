import os


def read_input(path: str) -> list:
    with open(path) as f:
        return f.read()


def p1(inp: str) -> int:
    p1 = 0
    cubes = {"red": 12, "green": 13, "blue": 14}
    for line in inp.strip().splitlines():
        error_flag = False
        game_no, rounds = line.split(":")
        game_no = int(game_no.split()[1])
        rounds = rounds.split(";")
        for r in rounds:
            for cube in r.strip().split(","):
                cube_count, cube_color = cube.split()
                cube_count = int(cube_count)
                if cubes[cube_color] < cube_count:
                    error_flag = True
                    break
        if not error_flag:
            p1 += game_no
    print(f"p1: {p1}")


def p2(inp: str) -> int:
    p2 = 0
    for line in inp.strip().splitlines():
        power = 1
        game_no, rounds = line.split(":")
        game_no = int(game_no.split()[1])
        rounds = rounds.split(";")
        min_cube_possible = {"red": 0, "green": 0, "blue": 0}
        for r in rounds:
            for cube in r.strip().split(","):
                cube_count, cube_color = cube.split()
                cube_count = int(cube_count)
                min_cube_possible[cube_color] = max(
                    cube_count, min_cube_possible[cube_color]
                )
        for color, value in min_cube_possible.items():
            power *= value
        p2 += power
    print(f"p2: {p2}")


def sample():
    inp = read_input("sample.txt")
    p1(inp)
    p2(inp)


def sol():
    inp = read_input("d2.txt")
    p1(inp)
    p2(inp)


if __name__ == "__main__":
    sample()
    sol()
