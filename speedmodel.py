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
        self.userpace = pace

        best_men = self.records.loc[(self.records['Distance'] == distance) & (
        self.records['Group'] == 'Men')]['SecKm'].iat[0]

        user_secskm = self.userpace.print(unit='secskm')
        if user_secskm > 0:
            self.user_score = best_men/user_secskm
        else:
            self.user_score = 1

        return self.user_score


    def print_user_score(self, decimals=2):
        return round(self.user_score*100, decimals)


    def predict_paces(self, algorithm='Nuno'):

        tmp = self.records[self.records['Group'] == 'Men'][[
                'Event', 'Distance', 'SecKm']].copy(deep=True)
        
        if algorithm == 'Nuno':
    
            tmp['PredictedPace'] = tmp['SecKm'] / self.user_score
            tmp['PredictedTime'] = tmp['Distance'] * 0.001 * tmp['PredictedPace']

        elif algorithm.startswith('Riegel'):
            # https://bmcsportsscimedrehabil.biomedcentral.com/articles/10.1186/s13102-016-0052-y
            if algorithm == 'Riegel standard':
                R = 1.05
            elif algorithm == 'Riegel elite':
                R = 1.08

            tmp['PredictedTime'] = self.userpace.time * (tmp['Distance']/self.userpace.distanceEvent)**R
            tmp['PredictedPace'] = 1000 * tmp['PredictedTime'] / tmp['Distance']



        tmp['Predicted Pace (min/km)'] = tmp['PredictedPace'].apply(seckm_to_minkm, decimals=1)
        tmp['Predicted Time (h:m:s)'] = tmp['PredictedTime'].apply(ParseTotalSeconds)

        return tmp

    def export(self):
        return self.records


