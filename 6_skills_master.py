def count_skills(tree, required):
    res = set()
    for skill in required:
        while skill not in res:
            res.add(skill)
            skill = tree[skill]
    return len(res)


if __name__ == "__main__":
    print(count_skills([ 0, 0, 0, 1, 3, 3, 2 ], { 4, 5 }))
