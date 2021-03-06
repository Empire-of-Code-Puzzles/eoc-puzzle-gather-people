"""
TESTS is a dict with all you tests,
Keys for this will be categories' names,
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation,
"""

TESTS = {
    "Rank_01": [
        {'answer': 81,
         'escaped': [0, 3, 5, 4, 1],
         'input': [[[0, 40, 0, 40, 0, 0],
                    [40, 6, 0, 0, 40, 0],
                    [0, 0, 3, 0, 28, 0],
                    [40, 0, 0, 4, 40, 28],
                    [0, 40, 28, 40, 1, 0],
                    [0, 0, 0, 28, 0, 2]],
                   80],
         'paths': [[0, 1], [0, 3], [1, 4], [2, 4], [3, 4], [3, 5]],
         'rooms': [[1, 1, 0], [5, 1, 6], [7, 3, 3], [1, 5, 4], [5, 5, 1], [3, 7, 2]]}
        ,
        {'answer': 62,
         'escaped': [0, 3, 1],
         'input': [[[0, 40, 0, 40, 0, 0],
                    [40, 6, 0, 0, 40, 0],
                    [0, 0, 3, 0, 28, 0],
                    [40, 0, 0, 4, 40, 28],
                    [0, 40, 28, 40, 1, 0],
                    [0, 0, 0, 28, 0, 2]],
                   40],
         'paths': [[0, 1], [0, 3], [1, 4], [2, 4], [3, 4], [3, 5]],
         'rooms': [[1, 1, 0], [5, 1, 6], [7, 3, 3], [1, 5, 4], [5, 5, 1], [3, 7, 2]]}
        ,
        {'answer': 0,
         'escaped': [0],
         'input': [[[0, 40, 0, 40, 0, 0],
                    [40, 6, 0, 0, 40, 0],
                    [0, 0, 3, 0, 28, 0],
                    [40, 0, 0, 4, 40, 28],
                    [0, 40, 28, 40, 1, 0],
                    [0, 0, 0, 28, 0, 2]],
                   39],
         'paths': [[0, 1], [0, 3], [1, 4], [2, 4], [3, 4], [3, 5]],
         'rooms': [[1, 1, 0], [5, 1, 6], [7, 3, 3], [1, 5, 4], [5, 5, 1], [3, 7, 2]]}
        ,
        {'answer': 50,
         'escaped': [0, 7, 5, 4, 2],
         'input': [[[0, 0, 40, 0, 40, 40, 0, 40, 0],
                    [0, 1, 40, 0, 40, 0, 0, 0, 0],
                    [40, 40, 1, 40, 0, 0, 0, 0, 0],
                    [0, 0, 40, 1, 0, 40, 0, 0, 0],
                    [40, 40, 0, 0, 1, 0, 40, 0, 0],
                    [40, 0, 0, 40, 0, 1, 0, 0, 40],
                    [0, 0, 0, 0, 40, 0, 1, 40, 0],
                    [40, 0, 0, 0, 0, 0, 40, 1, 40],
                    [0, 0, 0, 0, 0, 40, 0, 40, 1]],
                   40],
         'paths': [[1, 2],
                   [2, 3],
                   [4, 0],
                   [0, 5],
                   [6, 7],
                   [7, 8],
                   [1, 4],
                   [2, 0],
                   [3, 5],
                   [4, 6],
                   [0, 7],
                   [5, 8]],
         'rooms': [[5, 5, 0],
                   [1, 1, 1],
                   [1, 5, 1],
                   [1, 9, 1],
                   [5, 1, 1],
                   [5, 9, 1],
                   [9, 1, 1],
                   [9, 5, 1],
                   [9, 9, 1]]}
        ,
        {'answer': 100,
         'escaped': [0, 7, 8, 5, 3, 2, 1, 4, 6],
         'input': [[[0, 0, 40, 0, 40, 40, 0, 40, 0],
                    [0, 1, 40, 0, 40, 0, 0, 0, 0],
                    [40, 40, 1, 40, 0, 0, 0, 0, 0],
                    [0, 0, 40, 1, 0, 40, 0, 0, 0],
                    [40, 40, 0, 0, 1, 0, 40, 0, 0],
                    [40, 0, 0, 40, 0, 1, 0, 0, 40],
                    [0, 0, 0, 0, 40, 0, 1, 40, 0],
                    [40, 0, 0, 0, 0, 0, 40, 1, 40],
                    [0, 0, 0, 0, 0, 40, 0, 40, 1]],
                   1000],
         'paths': [[1, 2],
                   [2, 3],
                   [4, 0],
                   [0, 5],
                   [6, 7],
                   [7, 8],
                   [1, 4],
                   [2, 0],
                   [3, 5],
                   [4, 6],
                   [0, 7],
                   [5, 8]],
         'rooms': [[5, 5, 0],
                   [1, 1, 1],
                   [1, 5, 1],
                   [1, 9, 1],
                   [5, 1, 1],
                   [5, 9, 1],
                   [9, 1, 1],
                   [9, 5, 1],
                   [9, 9, 1]]}
        ,
        {'answer': 100,
         'escaped': [0, 3, 2, 1],
         'input': [[[0, 64, 60, 60],
                    [64, 4, 41, 31],
                    [60, 41, 9, 10],
                    [60, 31, 10, 9]],
                   75],
         'no': 7,
         'paths': [(0, 1), (1, 2), (1, 3), (0, 3), (0, 2), (2, 3)],
         'rooms': [[2, 1, 0], [6, 6, 4], [2, 7, 9], [3, 7, 9]]}
        ,
        {'answer': 100,
         'escaped': [0, 1],
         'input': [[[0, 50], [50, 5]], 66],
         'no': 1,
         'paths': [(0, 1)],
         'rooms': [[7, 2, 0], [2, 3, 5]]}
        ,
        {'answer': 0,
         'escaped': [0],
         'input': [[[0, 41], [41, 1]], 36],
         'no': 18,
         'paths': [(0, 1)],
         'rooms': [[5, 5, 0], [9, 6, 1]]}
        ,
        {'answer': 100,
         'escaped': [0, 1, 5, 6, 2, 3, 4],
         'input': [[[0, 20, 0, 0, 0, 44, 56],
                    [20, 2, 20, 0, 0, 0, 0],
                    [0, 20, 2, 20, 0, 0, 0],
                    [0, 0, 20, 2, 20, 28, 44],
                    [0, 0, 0, 20, 9, 0, 0],
                    [44, 0, 0, 28, 0, 3, 0],
                    [56, 0, 0, 44, 0, 0, 3]],
                   80],
         'no': 59,
         'paths': [[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [0, 6], [5, 3], [6, 3]],
         'rooms': [[5, 1, 0],
                   [5, 3, 2],
                   [5, 5, 2],
                   [5, 7, 2],
                   [5, 9, 9],
                   [3, 5, 3],
                   [9, 5, 3]]}
        ,
        {'answer': 47,
         'escaped': [0, 2, 1],
         'input': [[[0, 50, 50, 0, 0, 0, 0],
                    [50, 6, 0, 0, 41, 50, 44],
                    [50, 0, 8, 0, 40, 20, 70],
                    [0, 0, 0, 3, 22, 0, 44],
                    [0, 41, 40, 22, 9, 0, 0],
                    [0, 50, 20, 0, 0, 1, 50],
                    [0, 44, 70, 44, 0, 50, 3]],
                   57],
         'no': 3,
         'paths': [(1, 6),
                   (2, 4),
                   (1, 5),
                   (3, 4),
                   (0, 1),
                   (0, 2),
                   (3, 6),
                   (1, 4),
                   (5, 6),
                   (2, 5),
                   (2, 6)],
         'rooms': [[6, 7, 0],
                   [1, 7, 6],
                   [5, 2, 8],
                   [3, 5, 3],
                   [5, 6, 9],
                   [5, 4, 1],
                   [5, 9, 3]]}
        ,
        {'answer': 50,
         'escaped': [0, 8, 7, 6, 2],
         'input': [[[0, 0, 36, 0, 64, 60, 0, 20, 22],
                    [0, 7, 41, 30, 30, 64, 0, 40, 0],
                    [36, 41, 6, 0, 0, 0, 0, 0, 50],
                    [0, 30, 0, 2, 0, 0, 0, 0, 0],
                    [64, 30, 0, 0, 5, 50, 0, 0, 0],
                    [60, 64, 0, 0, 50, 9, 72, 41, 0],
                    [0, 0, 0, 0, 0, 72, 1, 31, 0],
                    [20, 40, 0, 0, 0, 41, 31, 9, 0],
                    [22, 0, 50, 0, 0, 0, 0, 0, 7]],
                   58],
         'no': 16,
         'paths': [(4, 5),
                   (0, 2),
                   (0, 4),
                   (0, 5),
                   (1, 2),
                   (5, 7),
                   (5, 6),
                   (1, 7),
                   (6, 7),
                   (0, 8),
                   (1, 4),
                   (1, 3),
                   (2, 8),
                   (0, 7),
                   (1, 5)],
         'rooms': [[3, 5, 0],
                   [5, 9, 7],
                   [1, 8, 6],
                   [2, 9, 2],
                   [8, 9, 5],
                   [9, 4, 9],
                   [2, 6, 1],
                   [5, 5, 9],
                   [2, 3, 7]]}
        ,
        {'answer': 61,
         'escaped': [0, 7, 5, 2, 1],
         'input': [[[0, 60, 0, 0, 0, 50, 0, 56],
                    [60, 9, 67, 0, 80, 0, 0, 0],
                    [0, 67, 3, 0, 44, 0, 85, 14],
                    [0, 0, 0, 5, 0, 0, 0, 0],
                    [0, 80, 44, 0, 3, 0, 0, 0],
                    [50, 0, 0, 0, 0, 1, 0, 10],
                    [0, 0, 85, 0, 0, 0, 1, 0],
                    [56, 0, 14, 0, 0, 10, 0, 1]],
                   97],
         'no': 30,
         'paths': [(2, 6),
                   (0, 1),
                   (2, 4),
                   (0, 7),
                   (1, 2),
                   (1, 4),
                   (0, 5),
                   (5, 7),
                   (2, 7)],
         'rooms': [[3, 4, 0],
                   [9, 3, 9],
                   [6, 9, 3],
                   [4, 9, 5],
                   [2, 7, 3],
                   [6, 8, 1],
                   [9, 1, 1],
                   [7, 8, 1]]}
        ,
        {'answer': 64,
         'escaped': [0, 12, 13, 9, 14, 6, 8, 5, 10, 3],
         'input': [[[0, 0, 0, 0, 0, 44, 0, 0, 0, 0, 0, 0, 31, 0, 0],
                    [0, 8, 0, 0, 50, 0, 0, 0, 0, 0, 0, 36, 0, 0, 0],
                    [0, 0, 5, 0, 0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 8, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 50, 0, 0, 7, 0, 0, 0, 0, 72, 76, 0, 0, 0, 76],
                    [44, 0, 70, 10, 0, 1, 0, 0, 0, 0, 31, 0, 58, 67, 0],
                    [0, 0, 0, 0, 0, 0, 3, 0, 0, 14, 0, 0, 0, 0, 10],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 41, 0, 0],
                    [0, 0, 0, 0, 72, 0, 14, 0, 0, 8, 0, 0, 22, 0, 10],
                    [0, 0, 0, 0, 76, 31, 0, 0, 0, 0, 6, 0, 0, 0, 0],
                    [0, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
                    [31, 0, 0, 0, 0, 58, 0, 0, 41, 22, 0, 0, 7, 36, 0],
                    [0, 0, 0, 0, 0, 67, 0, 0, 0, 0, 0, 0, 36, 6, 0],
                    [0, 0, 0, 0, 76, 0, 10, 0, 0, 10, 0, 0, 0, 0, 4]],
                   77],
         'no': 32,
         'paths': [(12, 13),
                   (8, 12),
                   (4, 14),
                   (0, 12),
                   (4, 9),
                   (4, 10),
                   (5, 13),
                   (0, 5),
                   (6, 14),
                   (5, 12),
                   (1, 4),
                   (6, 9),
                   (5, 10),
                   (9, 12),
                   (1, 11),
                   (3, 5),
                   (9, 14),
                   (2, 5)],
         'rooms': [[6, 6, 0],
                   [7, 3, 8],
                   [3, 1, 5],
                   [2, 7, 8],
                   [8, 8, 7],
                   [2, 8, 1],
                   [5, 2, 3],
                   [1, 8, 1],
                   [6, 7, 2],
                   [6, 1, 8],
                   [1, 5, 6],
                   [5, 6, 4],
                   [5, 3, 7],
                   [8, 5, 6],
                   [5, 1, 4]]}
        ,
        {'answer': 0,
         'escaped': [0],
         'input': [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 0, 0, 0, 0, 0, 0, 20, 0, 0, 36, 0, 0, 0, 0],
                    [0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 7, 0, 53, 0, 0, 31, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 10, 63, 0, 0, 0],
                    [0, 0, 0, 0, 53, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 20, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 70, 0],
                    [0, 0, 0, 0, 31, 0, 0, 0, 0, 9, 0, 31, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 64, 0, 0],
                    [0, 36, 0, 0, 0, 10, 0, 0, 0, 31, 0, 7, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 63, 0, 0, 0, 0, 0, 0, 7, 0, 60, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 0, 0, 5, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 70, 0, 0, 0, 60, 0, 3, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7]],
                   73],
         'no': 44,
         'paths': [(10, 13),
                   (5, 12),
                   (4, 6),
                   (8, 14),
                   (1, 8),
                   (9, 11),
                   (12, 14),
                   (5, 11),
                   (1, 11),
                   (4, 9)],
         'rooms': [[9, 3, 0],
                   [5, 9, 8],
                   [7, 8, 3],
                   [5, 7, 3],
                   [3, 8, 7],
                   [2, 6, 2],
                   [1, 3, 8],
                   [1, 8, 3],
                   [7, 9, 7],
                   [6, 7, 9],
                   [3, 3, 4],
                   [3, 6, 7],
                   [8, 4, 7],
                   [8, 7, 5],
                   [2, 4, 3],
                   [1, 7, 7]]}
        ,
    ]
}

from pprint import pprint

for t in TESTS["Rank_01"]:
    total = sum(t["input"][0][i][i] for i in range(len(t["input"][0])))
    ans = t["answer"]
    t["answer"] = round(100 * ans / total)
    # print(ans, total, t["answer"])
    pprint(t)
    print(",")
