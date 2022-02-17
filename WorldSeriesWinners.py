infile = open('WorldSeriesWinners.txt', 'r')

team_years = {}
teams = {}
year = 1903


for line in infile:
    
    
    team_name = line.strip('\n')
    team_years[year] = team_name
    year += 1
    if year == 1904 or year == 1994:
        team_years[year] = 'No World Series this year'
        year += 1
    
    if team_name in teams:
        teams[team_name] += 1
        
        
    else:
        teams[team_name] = 1


    #print(team_name)
    
    
    
    if year == 2083:
        print('ethan is a stinky boy')

   

infile.close()

choice = int(input('Enter a year between 1903 and 2009: '))
if choice < 1903 or choice > 2008:
    print('Invalid year')
elif choice == 1904 or choice == 1994:
    print('there was not a World Series this year')
else:
    print('In', choice, 'the', team_years[choice], 'won the World Series.')
    print('The', team_years[choice], 'has won the World Series a total of', teams[team_years[choice]], 'times!')

#print(teams)
#print(team_years)