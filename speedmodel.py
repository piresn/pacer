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

        TotalSeconds = self.records['Seconds'] + self.records['Minutes']*60 + self.records['Hours']*3600

        self.records['SecKm'] = TotalSeconds / (self.records['Distance']/1000)



    def calculate_user_score(self, distance, pace):
        best_men = self.records.loc[(self.records['Distance'] == distance) & (
        self.records['Group'] == 'Men')]['SecKm'].iat[0]

        if pace > 0:
            self.user_score = best_men/pace
        else:
            self.user_score = 1

        return self.user_score


    def print_user_score(self, decimals=2):
        return round(self.user_score*100, 2)


    def predict_paces(self):
        tmp = self.records[self.records['Group'] == 'Men'][[
            'Event', 'Distance', 'SecKm']].copy(deep=True)
        
        tmp['PredictedPace'] = tmp['SecKm'] / self.user_score

        tmp['PredictedTime'] = tmp['Distance'] * 0.001 * tmp['PredictedPace']

        tmp['Predicted Pace (min/km)'] = tmp['PredictedPace'].apply(seckm_to_minkm, decimals=1)

        tmp['Predicted Time (h:m:s)'] = tmp['PredictedTime'].apply(ParseTotalSeconds)

        return tmp

    def export(self):
        return self.records


