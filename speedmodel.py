import pandas as pd
from helpers import *

class SpeedModel:
    def __init__(self, records):

        self.records = records.melt(id_vars=['Event', 'Distance'],
                                    var_name='Group',
                                    value_name='Timestring')

        times = pd.DataFrame.from_records(data=self.records['Timestring'].apply(time_parser),
                                          columns=['Hours', 'Minutes', 'Seconds'])

        self.records = pd.concat([self.records, times], axis=1)

        self.records['Pace'] = 240 # TODO implement funtion calculate pace secs/km from distance and h m s
    

    def calculate(self, distance, pace):
        best_men = self.records.loc[(self.records['Distance'] == distance) & (
        self.records['Group'] == 'Men')]['Pace'].iat[0]

        return best_men/pace

    def get_proportion_pace(self, proportion):
        tmp = self.records[self.records['Group'] == 'Men'][[
            'Event', 'Distance', 'Pace']].copy(deep=True)
        
        tmp['PredictedPace'] = tmp['Pace'] * proportion

        tmp['PredictedTime'] = tmp['Distance'] * 0.001 * tmp['PredictedPace']


        return tmp

    def export(self):
        return self.records

