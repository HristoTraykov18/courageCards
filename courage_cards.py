
import argparse
import csv

import pandas as pd


class CourageCards:
    def __init__(self, df):
        self.df = df

    def _get_green_cards_mean(self):
        pass

    def _get_level_duration(self):
        pass

    def _get_total_points(self):
        pass

    def create_output_csv(self):
        pass


def contains_valid_data(df):
    events = ('start', 'shuffle_cards', 'green_card',
              'red_card', 'banked', 'end')

    if 'event' not in df.columns or 'created' not in df.columns:
        print('[ERROR] Could not find \'event\' or \'created\' columns!')
        return False

    df_events = df[df.columns[0]]

    # Validate start and end events
    if df_events.iloc[0] != events[0] or df_events.iloc[-1] != events[-1]:
        print('[ERROR] Invalid \'start\' or \'end\' events!')
        return False

    df_events.drop(labels=[df_events.index[0],
                   df_events.index[-1]], inplace=True)
    events = events[1:-1]

    for event in df_events:
        if event not in events:
            print('[ERROR] \'start\' or \'end\' events used more than once!')
            return False

    df_created = df[df.columns[0]]

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

    if (not contains_valid_data(df)):
        exit(code=2)

    # print(df['event'].index[0])
    # courage_cards = CourageCards(df)
    # courage_cards.create_output_csv()
