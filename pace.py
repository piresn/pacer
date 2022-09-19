from helpers import *
import pandas as pd

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
    


class Pace:
    """
    Creates paces, store as seconds per km and print as min:sec per km.
    """
    def __init__(self):
        self.pace=None

    def pace_from_kmh(self, kmh):
        self.pace=kmh_to_seckm(kmh)

    def pace_from_distance(self, meters, seconds, hours=0, minutes=0):
        time = seconds+60*minutes+3600*hours
        km = meters/1000
        self.distanceEvent = meters
        self.pace = time/km

    def calculate_percentage_best(self, records): #TODO this method + SpeedModel should be removed from Pace class
        s = SpeedModel(records)
        self.percentage_best = s.calculate(self.distanceEvent, self.pace)

    def print(self, decimals=0, unit='minkm'):

        if unit=='minkm':
            return seckm_to_minkm(self.pace, decimals=decimals)
        elif unit=='kmh':
            out = 3600/self.pace
            if decimals > 0:
                return round(out, decimals)
            else:
                return round(out)
        elif unit=='secskm':
            return self.pace
