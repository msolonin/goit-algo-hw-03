# -*- coding: utf-8 -*-
"""
Koch snowflake drawer.
Script that drawing Koch snowflake by turtle
"""

import turtle
import argparse


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(level, size):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 2 / 3**0.5)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, level, size)
        t.right(120)

    window.mainloop()


def parse_argv():
    """ Method for parsing arguments for this script, that drawing Koch snowflake
    """
    parser = argparse.ArgumentParser(description="Script that drawing Koch snowflake")
    parser.add_argument(
        "-s", "--size", type=int, help="Size of snowflake", default=300
    )
    parser.add_argument(
        "-l", "--level", type=int, required=True, help="Recursion level"
    )
    return parser.parse_args()


def main():
    args = parse_argv()
    draw_koch_snowflake(args.level, args.size)


if __name__ == "__main__":
    main()

