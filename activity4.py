import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def main():
    #Data consists of only FM-15 data and all '9999' entries have been removed
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
    tempData = pd.DataFrame(sample, columns=['hours', '2005', '2006', '2007',
                                                '2008', '2009', '2010', '2011',
                                                '2012', '2013', '2014', '2015',
                                                '2016', '2017', '2018', '2019', 
                                                '2020', '2021'])
    figure, hoursAxis = plt.subplots()

    #Manually set ticks to line up with months (ticks are in hours)
    # hoursAxis.set_xticks([0, 730, 1460, 2190, 2920, 3650, 4380, 5110, 5840, 6570, 7300, 8030, 8760])
    # hoursAxis.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec', 'Jan'])
    # hoursAxis2 = hoursAxis.twinx()
    
    #SIMPLE LINE PLOT

    # tempData.plot.line(x='hours', y='2005', color='#c0d2ff', ax=hoursAxis)
    # tempData.plot.line(x='hours', y='2006', color='#b6cbff', ax=hoursAxis2)
    # tempData.plot.line(x='hours', y='2007', color='#adc4ff', ax=hoursAxis2)
    # tempData.plot.line(x='hours', y='2008', color='#a0bbff', ax=hoursAxis2)
    # tempData.plot.line(x='hours', y='2009', color='#96b4ff', ax=hoursAxis2)
    # tempData.plot.line(x='hours', y='2010', color='#86a8ff', ax=hoursAxis2)
    # tempData.plot.line(x='hours', y='2011', color='#7a9fff', ax=hoursAxis2)
    # tempData.plot.line(x='hours', y='2012', color='#6e96ff', ax=hoursAxis2)
    # tempData.plot.line(x='hours', y='2013', color='#648fff', ax=hoursAxis2)
    # tempData.plot.line(x='hours', y='2014', color='#5685ff', ax=hoursAxis2)
    # tempData.plot.line(x='hours', y='2015', color='#467aff', ax=hoursAxis2)
    # tempData.plot.line(x='hours', y='2016', color='#3f75ff', ax=hoursAxis2)
    # tempData.plot.line(x='hours', y='2017', color='#316bff', ax=hoursAxis2)
    # tempData.plot.line(x='hours', y='2018', color='#2965ff', ax=hoursAxis2)
    # tempData.plot.line(x='hours', y='2019', color='#205eff', ax=hoursAxis2)
    # tempData.plot.line(x='hours', y='2020', color='#1556ff', ax=hoursAxis2)
    # tempData.plot.line(x='hours', y='2021', color='#0b4eff', ax=hoursAxis2) 


    #Attempt at iterating graphs instead of manually entering
    # yearString = ''
    # for i in range(2006, 2022):
    #     yearString = str(i)
    #     tempData.plot.line(x='hours', y=yearString, color='#b6cbff', ax=hoursAxis2)
    
    #HISTOGRAM with fit line
    #tempBins = [0, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 22.5, 25, 27.5, 30, 32.5, 35, 37.5, 40]
    #plt.hist(tempData['2005'], alpha=1, color='#1000ff', label='2005', bins=tempBins)
    #plt.hist(tempData['2021'], alpha=1, color='#466fdc', label='2021', bins=tempBins)
    #plt.hist(tempData['2007'], alpha=1, color='#6eDDff', label='2007', bins=tempBins)

    #figure.tight_layout()
    
    #Daily averages by year
    avg2005 = tempData['2005'].mean()
    dailyAvg2005 = []
    #Get average daily temperature for all days in 2005
    for day in range(0, 365):
        dailyAvg2005.append(tempData['2005'][day*24:day*24+24].mean())
    
    #yoyAvg is dummy variable to hold current year's daily average values
    yoyAvg = [] 
    daysAboveAvg_b2005 = [0] * 365
    for i in range(2005, 2022):
        yearString = str(i)
        for day in range(0, 365):
            #The calculation is confusing, but it is generally like this: day 1 is 0-23, day 2 is 24-47, day 3 is 48-71
            dayAvg = tempData[yearString][day*24:day*24+24].mean()
            yoyAvg.append(dayAvg)
            if dailyAvg2005[day] > dayAvg:
                daysAboveAvg_b2005[day] += 1
                

        #plt.plot(yoyAvg)
        yoyAvg.clear()
    
    plt.plot(dailyAvg2005)
    plt.plot(daysAboveAvg_b2005)
    plt.legend()
    plt.hot()

    #Mean temperature
    
    
    plt.show()
main()
