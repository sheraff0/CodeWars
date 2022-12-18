from collections import Counter


def runoff(voters):
    counter = [*Counter((x[0] for x in voters)).items()]
    counter.sort(key=lambda x: -x[1])
    print(counter)
    top2 = counter[:2]
    if any([
        len(top2) == 2 and top2[0][1] > top2[1][1],
        len(top2) == 1
    ]):
        return top2[0][0]


poll = [['Daisuke Aramaki', 'Gihren Zabi', 'Reinhard von Musel', 'Lex Luthor'], ['Gihren Zabi', 'Daisuke Aramaki', 'Lex Luthor', 'Reinhard von Musel'], ['Lex Luthor', 'Daisuke Aramaki', 'Gihren Zabi', 'Reinhard von Musel'], ['Lex Luthor', 'Daisuke Aramaki', 'Reinhard von Musel', 'Gihren Zabi'], ['Gihren Zabi', 'Lex Luthor', 'Daisuke Aramaki', 'Reinhard von Musel'], ['Reinhard von Musel', 'Daisuke Aramaki', 'Lex Luthor', 'Gihren Zabi'], ['Gihren Zabi', 'Reinhard von Musel', 'Daisuke Aramaki', 'Lex Luthor'], ['Daisuke Aramaki', 'Gihren Zabi', 'Reinhard von Musel', 'Lex Luthor']]
poll2 = [['Johan Liebert', 'Abelt Dessler', 'Lex Luthor', 'Reinhard von Musel'], ['Johan Liebert', 'Lex Luthor', 'Abelt Dessler', 'Reinhard von Musel'], ['Johan Liebert', 'Reinhard von Musel', 'Abelt Dessler', 'Lex Luthor']]

if __name__ == "__main__":
    print(runoff(poll2))
