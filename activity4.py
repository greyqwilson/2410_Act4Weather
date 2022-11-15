import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as scistat
import scipy.optimize

#Courtesy of unsym @stackoverflow
def fit_sin(tt, yy):
    '''Fit sin to the input time sequence, and return fitting parameters "amp", "omega", "phase", "offset", "freq", "period" and "fitfunc"'''
    tt = np.array(tt)
    yy = np.array(yy)
    ff = np.fft.fftfreq(len(tt), (tt[1]-tt[0]))   # assume uniform spacing
    Fyy = abs(np.fft.fft(yy))
    guess_freq = abs(ff[np.argmax(Fyy[1:])+1])   # excluding the zero frequency "peak", which is related to offset
    guess_amp = np.std(yy) * 2.**0.5
    guess_offset = np.mean(yy)
    guess = np.array([guess_amp, 2.*np.pi*guess_freq, 0., guess_offset])

    def sinfunc(t, A, w, p, c):  return A * np.sin(w*t + p) + c
    popt, pcov = scipy.optimize.curve_fit(sinfunc, tt, yy, p0=guess)
    A, w, p, c = popt
    f = w/(2.*np.pi)
    fitfunc = lambda t: A * np.sin(w*np.array(t) + p) + c
    return {"amp": A, "omega": w, "phase": p, "offset": c, "freq": f, "period": 1./f, "fitfunc": fitfunc, "maxcov": np.max(pcov), "rawres": (guess,popt,pcov)}


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
    
    #Daily averages by year
    avg2005 = tempData['2005'].mean()
    dailyAvg2005 = []
    #Get average daily temperature for all days in 2005
    for day in range(0, 365):
        dailyAvg2005.append(tempData['2005'][day*24:day*24+24].mean())
    
    #yoyAvg is dummy variable to hold current year's daily average values
    yoyAvg = [] 
    daysAboveAvg_b2005 = [0] * 365
    
    #Get daily averages for each year from 2005 thru 2022
    for i in range(2005, 2022):
        yearString = str(i)
        for day in range(0, 365):
            #The calculation is confusing, but it is generally like this: day 1 is 0-23, day 2 is 24-47, day 3 is 48-71
            dayAvg = tempData[yearString][day*24:day*24+24].mean()
            yoyAvg.append(dayAvg)
            if dailyAvg2005[day] < dayAvg:
                daysAboveAvg_b2005[day] += 1
        #plt.plot(yoyAvg, label=yearString)
        yoyAvg.clear()
    
    #Get statistical data for day 319
    avgDailyNov15 = []
    print(tempData['2005'][319*24])
    for year in range(2005, 2022):
        yearString = str(year)
        avgDailyNov15.append(tempData[yearString][319*24])

    #Get statistical data for each hour of day 319
    Nov15 = []
    hourlyNov15 = []
    hourlyMean = []
    for year in range(2005, 2022):
        yearString = str(year)
        Nov15.append(np.array(tempData[yearString][319*24:319*24+24])) #each year's Nov 15th
    
    for hour in range(0, 24):
        hourArr = []
        for day in Nov15:
            hourArr.append(day[hour])
        hourlyNov15.append(hourArr)
        hourlyMean.append(np.array(hourlyNov15[hour]).mean())

    twoFourHours = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    plt.boxplot(hourlyNov15)
    fitSinDict = fit_sin(twoFourHours, hourlyMean)
    plt.plot(twoFourHours, fitSinDict['fitfunc'](twoFourHours))
    plt.plot(twoFourHours, hourlyMean)
    plt.title("Nov 15 Hourly Temperatures 2005-2021")
    plt.legend()
    plt.show()
main()
