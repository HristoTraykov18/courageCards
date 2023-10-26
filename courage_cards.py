
import argparse
import csv

import numpy as np
import pandas as pd


class CourageCards:
    def __init__(self, df):
        self.df = df

    # Get the mean number of green cards (all rounds)
    def _get_green_cards_mean(self):
        df_events = self.df['event'][2:]
        green_cards_in_round = 0
        green_cards = []

        for event in df_events:
            if event == 'green_card':
                green_cards_in_round += 1
            elif event == 'shuffle_cards':
                green_cards.append(green_cards_in_round)

        return np.mean(green_cards, dtype=np.int64)

    # Get the total time spent on the level
    def _get_level_duration(self):
        return self.df['created'].iloc[-1] - self.df['created'].iloc[0]

    # Get the total points received
    def _get_total_points(self):
        pts_stacked = 0
        pts_total = 0
        df_events = self.df['event']

        for event in df_events:
            if event == 'green_card':
                pts_stacked += 1
            elif event == 'red_card':
                pts_stacked = 0
            elif event == 'banked':
                pts_total += pts_stacked
                pts_stacked = 0

        return pts_total

    def create_output_csv(self):
        with open('output.csv', 'w+') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([self._get_level_duration(),
                                self._get_green_cards_mean(),
                                self._get_total_points()])


def contains_valid_data(df):
    events = ('start', 'shuffle_cards', 'green_card',
              'red_card', 'banked', 'end')

    # Validate start and end events
    if 'event' not in df.columns or 'created' not in df.columns:
        print('[ERROR] Could not find \'event\' and/or \'created\' columns!')
        exit(code=2)

    df_events = df['event']

    if df_events.iloc[0] != events[0] or df_events.iloc[-1] != events[-1]:
        print('[ERROR] Invalid \'start\' or \'end\' events!')
        exit(code=3)

    df_events.drop(labels=[df_events.index[0],
                   df_events.index[-1]], inplace=True)
    events = events[1:-1]

    for event in df_events:
        if event not in events:
            print('[ERROR] \'start\' or \'end\' events used more than once!')
            exit(code=4)

    # Validate datetime format
    if df['created'].dtypes != np.datetime64:
        try:
            df['created'] = pd.to_datetime(
                df['created'], format='%Y-%m-%d %H:%M:%S.%f-07:00')
        except:
            print(f"[ERROR] Invalid datatime format provided!")
            exit(code=5)

    # Validate ascending order of events creation
    df_len = len(df['created'])

    for i in range(0, df_len - 1):
        if df['created'].iloc[i] >= df['created'].iloc[i+1]:
            print(
                '[ERROR] Event {} is created earlier than event {}, while it should be the other way around!'.format(
                    df['created'].keys()[i+1], df['created'].keys()[i]))
            exit(code=6)

    return True


parser = argparse.ArgumentParser(
    description='A simple CLI tool for analysing CourageCards level data')

parser.add_argument('-td', help='Test level data in JSON format', metavar='[file.json]',
                    dest='test_data', required=True)


if __name__ == '__main__':
    args = parser.parse_args()

    try:
        df = pd.read_json(args.test_data)
    except ValueError:
        print('[ERROR] Invalid test data provided. Please use a JSON file!')
        exit(code=1)

    if (contains_valid_data(df)):
        courage_cards = CourageCards(df)
        courage_cards.create_output_csv()
