import csv
import sys
import random
from datetime import datetime

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
D  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

start_screen ='''
         Welcome in the CoolMusic! Choose the action:

         1) Add new album
         2) Find albums by artist
         3) Find albums by year
         4) Find musician by album
         5) Find albums by letter(s)
         6) Find albums by genre
         7) Calculate the age of all albums
         8) Choose a random album by genre
         9) Show the amount of albums by an artist *
        10) Find the longest-time album *
         0) Exit
'''

def load_collector():
    with open('music1.csv', 'r') as csvfile:
        all_lines = (line.rstrip() for line in csvfile) # All lines including the blank ones
        valid_lines = (line for line in all_lines if line) # Non-blank lines
        splitted_lines = [line.split(" | ") for line in valid_lines]
        music = [((line[0], line[1]), (int(line[2]), line[3], line[4]))for line in splitted_lines]
        return music

def new_album():
    new_position = []
    artist = new_position.append(input (D+'Type artist: ').title())
    album = new_position.append(input (D+'Type album: ').title())
    year = ''
    while not year.isdigit():
        year = input(D+'Type a year: ')
        if year.isdigit():
            new_position.append(year)
    genre = new_position.append(input (D+'Type a genre: ').title())
    lenght = new_position.append(input (D+'Type lenght of album: '))

    with open('music1.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([' | '.join(new_position)])
        csvfile.close()

def albums_by_artist(music):
    artist = input(D+'Choose artist: ').title()
    for musician in music:
        if artist in musician[0][0]:
            print ((musician[0][0]),'-',(musician[0][1]))

def albums_by_year(music):
    year = input(D+'Choose year: ')
    for date in music:
        if year in str(date[1][0]):
            print ((date[0][0]),'-',(date[0][1]))

def musician_by_album(music):
    album = input(D+'Choose an album: ').title()
    for title in music:
        if album in title[0][1]:
            print (title[0][0])

def albums_by_letter(music):
    letters = input(D+'Type a letter(s): ')
    for title in music:
        if letters in title[0][1]:
            print ((title[0][1]),'-',(title[0][0]))

def albums_by_genre(music):
    genre = input(D+'Choose genre: ').lower()
    for kind in music:
        if genre in kind[1][1]:
            print ((kind[0][0]),'-',(kind[0][1]))

def age_of_albums(music):
    data = datetime.now()
    total_age = 0
    for age in music:
        if age[1][0] < 2018:
            total_age += (data.year) % (age[1][0])
    print (total_age)

def random_album_by_genre(music):
    genre = input(D+'Choose genre: ').lower()
    albums = []
    for kind in music:
        if genre in kind[1][1]:
            albums.append(kind[0])
    random_album = (random.choice(albums))
    print (*random_album)

def amount_of_albums(music):
    artist = input(D+'Choose an artist: ').title()
    counter = 0
    for x in music:
        if artist in x[0][0]:
            counter += 1
    print (counter)

def longest_album(music):
    longest_time = '00:00'
    for lenght in music:
        if len(longest_time) < len(lenght[1][2]) and not lenght[1][2].isalpha():
            longest_time = lenght[1][2]
            longest_album = ((lenght[0][0]),'-',(lenght[0][1]))
        if longest_time < lenght[1][2] and not lenght[1][2].isalpha():
            longest_time = lenght[1][2]
            longest_album = ((lenght[0][0]),'-',(lenght[0][1]))
    print (*longest_album)

def main():
    while 1:
        print (B+start_screen)
        option = input(R+'Choose an option: ')
        music = load_collector()
        if option == '1':
            new_album()
        elif option == '2':
            albums_by_artist(music)
        elif option == '3':
            albums_by_year(music)
        elif option == '4':
            musician_by_album(music)
        elif option == '5':
            albums_by_letter(music)
        elif option == '6':
            albums_by_genre(music)
        elif option == '7':
            age_of_albums(music)
        elif option == '8':
            random_album_by_genre(music)
        elif option == '9':
            amount_of_albums(music)
        elif option == '10':
            longest_album(music)
        elif option == '0':
            print (R+'ByeBye!')
            sys.exit(0)
        else:
            print(W+'Please choose a valid option !')

main()
