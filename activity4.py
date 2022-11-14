import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def main():
    data = pd.read_csv("ontarioAirport.csv")
    #make sure data time does not match, so no duplicates
    tempSeries = data['TMP']
    tempData = []
    z = " d"
    #convert codified data to celsius
    for entry in tempSeries:
        tempData.append(float(entry[2:5]) / 10)

    

    data['TMP'] = tempData
    sampleList = data['TMP'][0:156611].tolist()
    one_1000 = []
    for number in range(0, 156611):
        one_1000.append(number)

    y_2005 = sampleList[0:8760]
    y_2006 = sampleList[8761:17521]
    y_2007 = sampleList[17521:26281]
    y_2008 = sampleList[26282:35042]
    y_2009 = sampleList[35043:43803]
    y_2010 = sampleList[43804:52564]
    y_2011 = sampleList[52565:61325]
    y_2012 = sampleList[61326:70086]
    y_2013 = sampleList[70087:78847]
    y_2014 = sampleList[78848:87608]
    y_2015 = sampleList[87609:96369]
    y_2016 = sampleList[96370:105130]
    y_2017 = sampleList[105131:113891]
    y_2018 = sampleList[113892:122652]
    y_2019 = sampleList[122653:131413]
    y_2020 = sampleList[131414:140174]
    y_2021 = sampleList[140175:148935]
    y_2022 = sampleList[148927:156502]

    listOfYears = []
    
    hourRange = []
    #Make complementary hour list for data array
    for hour in range(0, 8760):
        hourRange.append(hour)
    # listOfYears.append(hourRange, y_2005, y_2006, y_2007,
    #                                y_2008, y_2009, y_2010,
    #                                y_2011, y_2012, y_2013,
    #                                y_2014, y_2015, y_2016,
    #                                y_2017, y_2018, y_2019,
    #                                y_2020, y_2021)
    
    sample = np.array([hourRange, y_2005, y_2006, y_2007, y_2008, y_2009,
                                  y_2010, y_2011, y_2012, y_2013, y_2014,
                                  y_2015, y_2016, y_2017, y_2018, y_2019,
                                  y_2020, y_2021]).transpose()
   # print(sample)
    sampleTemp = pd.DataFrame(sample, columns=['hours', '2005', '2006', '2007',
                                                '2008', '2009', '2010', '2011',
                                                '2012', '2013', '2014', '2015',
                                                '2016', '2017', '2018', '2019', 
                                                '2020', '2021'])
    a1 = sampleTemp.plot.line(x='hours', y='2005', c='DarkBlue')
    a2 = sampleTemp.plot.line(x='hours', y='2006', color='Green')
    plt.show()
main()
