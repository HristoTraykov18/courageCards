
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
        print('[ERROR] Could not find \'event\' and/or \'created\' columns!')
        return False

    df_events = df['event']

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

    df_created = df['created']

    try:
        pd.to_datetime(df_created, format='%Y-%m-%d %H:%M:%S.%f-07:00')
    except:
        print(f"[ERROR] Invalid datatime format provided!")
        return False

    df_len = len(df_created)

    for i in range(0, df_len - 1):
        if df_created.iloc[i] >= df_created.iloc[i+1]:
            print(
                '[ERROR] Event {} is created earlier than event {}, while it should be the other way around!'.format(
                    df_created.keys()[i+1], df_created.keys()[i]))
            return False

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

    courage_cards = CourageCards(df)
    courage_cards.create_output_csv()
