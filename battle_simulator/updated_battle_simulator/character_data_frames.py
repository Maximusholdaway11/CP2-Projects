#Max Holdaway Updated Battle Simulator: Character Data Frame function(s)
import pandas
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import matplotlib.pyplot as plt
import numpy as np

#A function to load all the characters into one dataframe
def load_characters_into_data_frame(characters):
    if characters != []:
        character_data_frame = pandas.DataFrame(characters)
        character_data_frame.set_index('name')
        return character_data_frame
    else:
        return ""

#The function to show the charater min max mean and medians as well as a prompt if they want to see a graph of them.
def characters_min_max_median_mean(character_data_frame):
    min_frame = character_data_frame[['health', 'strength', 'defense', 'speed']].min()
    max_frame = character_data_frame[['health', 'strength', 'defense', 'speed']].max()
    mean_frame = character_data_frame[['health', 'strength', 'defense', 'speed']].mean()
    median_frame = character_data_frame[['health', 'strength', 'defense', 'speed']].median()
    user_input = inquirer.select(
            message="Choose which option you want to see for the characters stats:",
            choices=['min', 'max', 'mean', 'median'],
        ).execute()
    if user_input == "min":
        print("Here are lowest values of each stat.")
        print(min_frame)
        user_confirmation = inquirer.confirm(message="Do you want to see a graph of this data?").execute()
        if user_confirmation:
            plt.style.use('_mpl-gallery')

            x = ["Health", "Strength", "Defense", "Speed"]
            y = [min_frame['health'], min_frame['strength'], min_frame['defense'], min_frame['speed']]
            graph_pos = [0.1, 0.1, 5, 5]
            fig, ax = plt.subplots()
            ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
            ax.set(ylim=(0, 100), yticks=np.arange(1, 101), ylabel="Stats", position=graph_pos)

            plt.show()
    elif user_input == "max":
        print("Here are maximum values of each stat.")
        print(max_frame)
        user_confirmation = inquirer.confirm(message="Do you want to see a graph of this data?").execute()
        if user_confirmation:
            plt.style.use('_mpl-gallery')

            x = ["Health", "Strength", "Defense", "Speed", "xp"]
            y = [max_frame['health'], max_frame['strength'], max_frame['defense'], max_frame['speed']]
            graph_pos = [0.1, 0.1, 5, 5]
            fig, ax = plt.subplots()
            ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
            ax.set(ylim=(0, 100), yticks=np.arange(1, 101), ylabel="Stats", position=graph_pos)

            plt.show()
    elif user_input == "mean":
        print("Here are the means of each stat.")
        print(mean_frame)
        user_confirmation = inquirer.confirm(message="Do you want to see a graph of this data?").execute()
        if user_confirmation:
            plt.style.use('_mpl-gallery')

            x = ["Health", "Strength", "Defense", "Speed", "xp"]
            y = [mean_frame['health'], mean_frame['strength'], mean_frame['defense'], mean_frame['speed']]
            graph_pos = [0.1, 0.1, 5, 5]
            fig, ax = plt.subplots()
            ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
            ax.set(ylim=(0, 100), yticks=np.arange(1, 101), ylabel="Stats", position=graph_pos)

            plt.show()
    elif user_input == "median":
        print("Here are medians of each stat.")
        print(median_frame)
        user_confirmation = inquirer.confirm(message="Do you want to see a graph of this data?").execute()
        if user_confirmation:
            plt.style.use('_mpl-gallery')

            x = ["Health", "Strength", "Defense", "Speed", "xp"]
            y = [mean_frame['health'], mean_frame['strength'], mean_frame['defense'], mean_frame['speed']]
            graph_pos = [0.1, 0.1, 5, 5]
            fig, ax = plt.subplots()
            ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
            ax.set(ylim=(0, 100), yticks=np.arange(1, 101), ylabel="Stats", position=graph_pos)

            plt.show()
    