teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

#1
prumerna_teplota = [sum(den)/4 for den in teploty]

#2
ranni_teploty = [den[0] for den in teploty]

#3
nocni_teploty = [den[-1] for den in teploty]

#4
poledne_noc = [[den[1], den[-1]] for den in teploty]

