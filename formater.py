import csv
HEADER = ("Flamengo", 'Fluminense', 'Palmeiras')
DATA= {
    'Libertadores' : [3,1,3],
    'CDB' : [4,1,2],
    'Brasileiro': [7,2,9]
}

with open('movies.csv','w', newline='') as csvfile:
    movies= csv.writer(csvfile)
    movies.writerow(HEADER)
    for competition, results in DATA.items():
        row = [competition] + results
        movies.writerow(row)