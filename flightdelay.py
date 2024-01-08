import pickle
import streamlit as st

# loading the trained model
#pickle_in = open('xgbclassifier.pkl', 'rb')
#classifier = pickle.load(pickle_in)
with open('xgbclassifier.pkl', 'rb') as file:
    # Load the pickled model
    classifier = pickle.load(file)
    
st.cache_data.clear()

# defining the function which will make the prediction using the data which the user inputs
def prediction(Airline, OriginCityName, Diverted, DistanceGroup, Quarter,
                       Month, DayofMonth, DayOfWeek, TaxiOut, DepTime,DepTimeBlk):

    # Pre-processing user input
    if Airline == "Air Wisconsin Airlines Corp":
        Airline = 0
    elif Airline == "Alaska Airlines Inc.":
        Airline = 1
    elif Airline == "Allegiant Air":
        Airline = 2
    elif Airline == "American Airlines Inc.":
        Airline = 3
    elif Airline == "Capital Cargo International":
        Airline = 4
    elif Airline == "Comair Inc.":
        Airline = 5
    elif Airline == "Commutair Aka Champlain Enterprises, Inc.":
        Airline = 6
    elif Airline == "Delta Air Lines Inc.":
        Airline = 7
    elif Airline == "Empire Airlines Inc.":
        Airline = 8
    elif Airline == "Endeavor Air Inc.":
        Airline = 9
    elif Airline == "Envoy Air":
        Airline = 10
    elif Airline == "Frontier Airlines Inc.":
        Airline = 11
    elif Airline == "GoJet Airlines, LLC d/b/a United Express":
        Airline = 12
    elif Airline == "Hawaiian Airlines Inc.":
        Airline = 13
    elif Airline == "Horizon Air":
        Airline = 14
    elif Airline == "JetBlue Airways":
        Airline = 15
    elif Airline == "Mesa Airlines Inc.":
        Airline = 16
    elif Airline == "Republic Airlines":
        Airline = 17
    elif Airline == "SkyWest Airlines Inc.":
        Airline = 18
    elif Airline == "Southwest Airlines Co.":
        Airline = 19
    elif Airline == "Spirit Air Lines":
        Airline = 20
    else:
        Airline = 21

    if DayOfWeek == "Monday":
        DayOfWeek = 1
    elif DayOfWeek == "Tuesday":
        DayOfWeek = 2
    elif DayOfWeek == "Wednesday":
        DayOfWeek = 3
    if DayOfWeek == "Thursday":
        DayOfWeek = 4
    elif DayOfWeek == "Friday":
        DayOfWeek = 5
    elif DayOfWeek == "Saturday":
        DayOfWeek = 6
    else:
        DayOfWeek = 7

    if Diverted == "True":
        Diverted = True
    else:
        Diverted = False

##Quater "1(Jan-Mar)","2(Apr-Jun)","3(Jul-Sep)","4(Oct-Dec)"
    if Quarter == "1(Jan-Mar)":
        Quarter = 1
    elif Quarter == "2(Apr-Jun)":
        Quarter = 2
    elif Quarter == "3(Jul-Sep)":
        Quarter = 3
    else:
        Quarter = 4

    if Month == "January":
        Month = 1
    elif Month == "February":
        Month = 2
    elif Month == "March":
        Month = 3
    elif Month == "April":
        Month = 4
    elif Month == "May":
        Month = 5
    elif Month == "June":
        Month = 6
    elif Month == "July":
        Month = 7
    elif Month == "August":
        Month = 8
    elif Month == "September":
        Month = 9
    elif Month == "October":
        Month = 10
    elif Month == "November":
        Month = 11
    else:
        Month = 12



    if DepTimeBlk == "0001-0559":
        DepTimeBlk = 0
    elif DepTimeBlk == "0600-0659":
        DepTimeBlk = 1
    elif DepTimeBlk == "0700-0759":
        DepTimeBlk = 2
    elif DepTimeBlk == "0800-0859":
        DepTimeBlk = 3
    elif DepTimeBlk == "0900-0959":
        DepTimeBlk = 4
    elif DepTimeBlk == "1000-1059":
        DepTimeBlk = 5
    elif DepTimeBlk == "1100-1159":
        DepTimeBlk = 6
    elif DepTimeBlk == "1200-1259":
        DepTimeBlk = 7
    elif DepTimeBlk == "1300-1359":
        DepTimeBlk = 8
    elif DepTimeBlk == "1400-1459":
        DepTimeBlk = 9
    elif DepTimeBlk == "1500-1559":
        DepTimeBlk = 10
    elif DepTimeBlk == "1600-1659":
        DepTimeBlk = 11
    elif DepTimeBlk == "1700-1759":
        DepTimeBlk = 12
    elif DepTimeBlk == "1800-1859":
        DepTimeBlk = 13
    elif DepTimeBlk == "1900-1959":
        DepTimeBlk = 14
    elif DepTimeBlk == "2000-2059":
        DepTimeBlk = 15
    elif DepTimeBlk == "2100-2159":
        DepTimeBlk = 16
    elif DepTimeBlk == "2200-2259":
        DepTimeBlk = 17
    else:
        DistanceGroup = 18

    if DistanceGroup == "1(0-250 Miles)":
        DistanceGroup = 1
    elif DistanceGroup == "2(251-500 Miles)":
        DistanceGroup = 2
    elif DistanceGroup == "3(501-750 Miles)":
        DistanceGroup = 3
    elif DistanceGroup == "4(751-1000 Miles)":
        DistanceGroup = 4
    elif DistanceGroup == "5(1001-1250 Miles)":
        DistanceGroup = 5
    elif DistanceGroup == "6(1251-1500 Miles)":
        DistanceGroup = 6
    elif DistanceGroup == "7(1501-1750 Miles)":
        DistanceGroup = 7
    elif DistanceGroup == "8(1751-2000 Miles)":
        DistanceGroup = 8
    elif DistanceGroup == "9(2001-2250 Miles)":
        DistanceGroup = 9
    elif DistanceGroup == "10(2501-2750 Miles)":
        DistanceGroup = 10
    else:
        DistanceGroup = 11

    if Month == "January":
        Month = 1
    elif Month == "February":
        Month = 2
    elif Month == "March":
        Month = 3
    elif Month == "April":
        Month = 4
    elif Month == "May":
        Month = 5
    elif Month == "June":
        Month = 6
    elif Month == "July":
        Month = 7
    elif Month == "August":
        Month = 8
    elif Month == "September":
        Month = 9
    elif Month == "October":
        Month = 10
    elif Month == "November":
        Month = 11
    else:
        Month = 12

    if OriginCityName == "Aberdeen, SD":
        OriginCityName = 0
    elif OriginCityName == "Abilene, TX":
        OriginCityName = 1
    elif OriginCityName == "Adak Island, AK":
        OriginCityName = 2
    elif OriginCityName == "Aguadilla, PR":
        OriginCityName = 3
    elif OriginCityName == "Akron, OH":
        OriginCityName = 4
    elif OriginCityName == "Alamosa, CO ":
        OriginCityName = 5
    elif OriginCityName == "Albany, GA":
        OriginCityName = 6
    elif OriginCityName == "Albany, NY":
        OriginCityName = 7
    elif OriginCityName == "Albuquerque, NM":
        OriginCityName = 8
    elif OriginCityName == "Alexandria, LA":
        OriginCityName = 9
    elif OriginCityName == "Allentown/Bethlehem/Easton, PA":
        OriginCityName = 10
    elif OriginCityName == "Alpena, MI":
        OriginCityName = 11
    elif OriginCityName == "Amarillo, TX":
        OriginCityName = 12
    elif OriginCityName == "Anchorage, AK":
        OriginCityName = 13
    elif OriginCityName == "Appleton, WI":
        OriginCityName = 14
    elif OriginCityName == "Arcata/Eureka, CA":
        OriginCityName = 15
    elif OriginCityName == "Asheville, NC":
        OriginCityName = 16
    elif OriginCityName == "Ashland, WV":
        OriginCityName = 17
    elif OriginCityName == "Aspen, CO":
        OriginCityName = 18
    elif OriginCityName == "Atlanta, GA":
        OriginCityName = 19
    elif OriginCityName == "Atlantic City, NJ":
        OriginCityName = 20
    elif OriginCityName == "Augusta, GA":
        OriginCityName = 21
    elif OriginCityName == "Austin, TX":
        OriginCityName = 22
    elif OriginCityName == "Bakersfield, CA":
        OriginCityName = 23
    elif OriginCityName == "Baltimore, MD":
        OriginCityName = 24
    elif OriginCityName == "Bangor, ME":
        OriginCityName = 25
    elif OriginCityName == "Barrow, AK":
        OriginCityName = 26
    elif OriginCityName == "Baton Rouge, LA":
        OriginCityName = 27
    elif OriginCityName == "Beaumont/Port Arthur, TX":
        OriginCityName = 28
    elif OriginCityName == "Belleville, IL":
        OriginCityName = 29
    elif OriginCityName == "Bellingham, WA":
        OriginCityName = 30
    elif OriginCityName == "Bemidji, MN":
        OriginCityName = 31
    elif OriginCityName == "Bend/Redmond, OR":
        OriginCityName = 32
    elif OriginCityName == "Bethel, AK":
        OriginCityName = 33
    elif OriginCityName == "Billings, MT":
        OriginCityName = 34
    elif OriginCityName == "Binghamton, NY":
        OriginCityName = 35
    elif OriginCityName == "Birmingham, AL":
        OriginCityName = 36
    elif OriginCityName == "Bishop, CA":
        OriginCityName = 37
    elif OriginCityName == "Bismarck/Mandan, ND":
        OriginCityName = 38
    elif OriginCityName == "Bloomington/Normal, IL":
        OriginCityName = 39
    elif OriginCityName == "Boise, ID":
        OriginCityName = 40
    elif OriginCityName == "Boston, MA":
        OriginCityName = 41
    elif OriginCityName == "Bozeman, MT":
        OriginCityName = 42
    elif OriginCityName == "Brainerd, MN":
        OriginCityName = 43
    elif OriginCityName == "Branson, MO":
        OriginCityName = 44
    elif OriginCityName == "Bristol/Johnson City/Kingsport, TN":
        OriginCityName = 45
    elif OriginCityName == "Brownsville, TX":
        OriginCityName = 46
    elif OriginCityName == "Brunswick, GA":
        OriginCityName = 47
    elif OriginCityName == "Buffalo, NY":
        OriginCityName = 48
    elif OriginCityName == "Burbank, CA":
        OriginCityName = 49
    elif OriginCityName == "Burlington, VT":
        OriginCityName = 50
    elif OriginCityName == "Butte, MT":
        OriginCityName = 51
    elif OriginCityName == "Cape Girardeau, MO":
        OriginCityName = 52
    elif OriginCityName == "Casper, WY":
        OriginCityName = 53
    elif OriginCityName == "Cedar City, UT":
        OriginCityName = 54
    elif OriginCityName == "Cedar Rapids/Iowa City, IA":
        OriginCityName = 55
    elif OriginCityName == "Champaign/Urbana, IL":
        OriginCityName = 56
    elif OriginCityName == "Charleston, SC":
        OriginCityName = 57
    elif OriginCityName == "Charleston/Dunbar, WV":
        OriginCityName = 58
    elif OriginCityName == "Charlotte Amalie, VI":
        OriginCityName = 59
    elif OriginCityName == "Charlotte, NC":
        OriginCityName = 60
    elif OriginCityName == "Charlottesville, VA":
        OriginCityName = 61
    elif OriginCityName == "Chattanooga, TN":
        OriginCityName = 62
    elif OriginCityName == "Cheyenne, WY":
        OriginCityName = 63
    elif OriginCityName == "Chicago, IL":
        OriginCityName = 64
    elif OriginCityName == "Christiansted, VI":
        OriginCityName = 65
    elif OriginCityName == "Cincinnati, OH":
        OriginCityName = 66
    elif OriginCityName == "Clarksburg/Fairmont, WV":
        OriginCityName = 67
    elif OriginCityName == "Cleveland, OH":
        OriginCityName = 68
    elif OriginCityName == "Cody, WY":
        OriginCityName = 69
    elif OriginCityName == "Cold Bay, AK":
        OriginCityName = 70
    elif OriginCityName == "College Station/Bryan, TX":
        OriginCityName = 71
    elif OriginCityName == "Colorado Springs, CO":
        OriginCityName = 72
    elif OriginCityName == "Columbia, MO":
        OriginCityName = 73
    elif OriginCityName == "Columbia, SC":
        OriginCityName = 74
    elif OriginCityName == "Columbus, GA":
        OriginCityName = 75
    elif OriginCityName == "Columbus, MS":
        OriginCityName = 76
    elif OriginCityName == "Columbus, OH":
        OriginCityName = 77
    elif OriginCityName == "Concord, NC":
        OriginCityName = 78
    elif OriginCityName == "Cordova, AK":
        OriginCityName = 79
    elif OriginCityName == "Corpus Christi, TX":
        OriginCityName = 80
    elif OriginCityName == "Dallas, TX":
        OriginCityName = 81
    elif OriginCityName == "Dallas/Fort Worth, TX":
        OriginCityName = 82
    elif OriginCityName == "Dayton, OH":
        OriginCityName = 83
    elif OriginCityName == "Daytona Beach, FL":
        OriginCityName = 84
    elif OriginCityName == "Deadhorse, AK":
        OriginCityName = 85
    elif OriginCityName == "Decatur, IL":
        OriginCityName = 86
    elif OriginCityName == "Del Rio, TX":
        OriginCityName = 87
    elif OriginCityName == "Denver, CO":
        OriginCityName = 88
    elif OriginCityName == "Des Moines, IA":
        OriginCityName = 89
    elif OriginCityName == "Detroit, MI":
        OriginCityName = 90
    elif OriginCityName == "Devils Lake, ND":
        OriginCityName = 91
    elif OriginCityName == "Dickinson, ND":
        OriginCityName = 92
    elif OriginCityName == "Dillingham, AK":
        OriginCityName = 93
    elif OriginCityName == "Dodge City, KS":
        OriginCityName = 94
    elif OriginCityName == "Dothan, AL":
        OriginCityName = 95
    elif OriginCityName == "Dubuque, IA":
        OriginCityName = 96
    elif OriginCityName == "Duluth, MN":
        OriginCityName = 97
    elif OriginCityName == "Durango, CO":
        OriginCityName = 98
    elif OriginCityName == "Eagle, CO":
        OriginCityName = 99
    elif OriginCityName == "Eau Claire, WI":
        OriginCityName = 100
    elif OriginCityName == "El Paso, TX.":
        OriginCityName = 101
    elif OriginCityName == "Elko, NV":
        OriginCityName = 102
    elif OriginCityName == "Elmira/Corning, NY":
        OriginCityName = 103
    elif OriginCityName == "Erie, PA":
        OriginCityName = 104
    elif OriginCityName == "Escanaba, MI":
        OriginCityName = 105
    elif OriginCityName == "Eugene, OR":
        OriginCityName = 106
    elif OriginCityName == "Evansville, IN":
        OriginCityName = 107
    elif OriginCityName == "Everett, WA":
        OriginCityName = 108
    elif OriginCityName == "Fairbanks, AK":
        OriginCityName = 109
    elif OriginCityName == "Fargo, ND":
        OriginCityName = 110
    elif OriginCityName == "Fayetteville, AR":
        OriginCityName = 111
    elif OriginCityName == "Fayetteville, NC":
        OriginCityName = 112
    elif OriginCityName == "Flagstaff, AZ":
        OriginCityName = 113
    elif OriginCityName == "Flint, MI":
        OriginCityName = 114
    elif OriginCityName == "Florence, SC":
        OriginCityName = 115
    elif OriginCityName == "Fort Dodge, IA":
        OriginCityName = 116
    elif OriginCityName == "Fort Lauderdale, FL":
        OriginCityName = 117
    elif OriginCityName == "Fort Leonard Wood, MO":
        OriginCityName = 118
    elif OriginCityName == "Fort Myers, FL":
        OriginCityName = 119
    elif OriginCityName == "Fort Smith, AR":
        OriginCityName = 120
    elif OriginCityName == "Fort Wayne, IN":
        OriginCityName = 121
    elif OriginCityName == "Fresno, CA":
        OriginCityName = 122
    elif OriginCityName == "Gainesville, FL":
        OriginCityName = 123
    elif OriginCityName == "Garden City, KS":
        OriginCityName = 124
    elif OriginCityName == "Gillette, WY":
        OriginCityName = 125
    elif OriginCityName == "Grand Forks, ND":
        OriginCityName = 126
    elif OriginCityName == "Grand Island, NE":
        OriginCityName = 127
    elif OriginCityName == "Grand Junction, CO":
        OriginCityName = 128
    elif OriginCityName == "Grand Rapids, MI":
        OriginCityName = 129
    elif OriginCityName == "Great Falls, MT":
        OriginCityName = 130
    elif OriginCityName == "Green Bay, WI":
        OriginCityName = 131
    elif OriginCityName == "Greensboro/High Point, NC":
        OriginCityName = 132
    elif OriginCityName == "Greenville, NC":
        OriginCityName = 133
    elif OriginCityName == "Greer, SC":
        OriginCityName = 134
    elif OriginCityName == "Guam, TT":
        OriginCityName = 135
    elif OriginCityName == "Gulfport/Biloxi, MS":
        OriginCityName = 136
    elif OriginCityName == "Gunnison, CO":
        OriginCityName = 137
    elif OriginCityName == "Gustavus, AK":
        OriginCityName = 138
    elif OriginCityName == "Hagerstown, MD":
        OriginCityName = 139
    elif OriginCityName == "Hancock/Houghton, MI":
        OriginCityName = 140
    elif OriginCityName == "Harlingen/San Benito, TX":
        OriginCityName = 141
    elif OriginCityName == "Harrisburg, PA":
        OriginCityName = 142
    elif OriginCityName == "Hartford, CT":
        OriginCityName = 143
    elif OriginCityName == "Hattiesburg/Laurel, MS":
        OriginCityName = 144
    elif OriginCityName == "Hayden, CO":
        OriginCityName = 145
    elif OriginCityName == "Hays, KS":
        OriginCityName = 146
    elif OriginCityName == "Helena, MT":
        OriginCityName = 147
    elif OriginCityName == "Hibbing, MN":
        OriginCityName = 148
    elif OriginCityName == "Hilo, HI":
        OriginCityName = 149
    elif OriginCityName == "Hilton Head, SC":
        OriginCityName = 150
    elif OriginCityName == "Hobbs, NM":
        OriginCityName = 151
    elif OriginCityName == "Honolulu, HI":
        OriginCityName = 152
    elif OriginCityName == "Hoolehua, HI":
        OriginCityName = 153
    elif OriginCityName == "Houston, TX":
        OriginCityName = 154
    elif OriginCityName == "Huntsville, AL":
        OriginCityName = 155
    elif OriginCityName == "Hyannis, MA":
        OriginCityName = 156
    elif OriginCityName == "Idaho Falls, ID":
        OriginCityName = 157
    elif OriginCityName == "Indianapolis, IN":
        OriginCityName = 158
    elif OriginCityName == "International Falls, MN":
        OriginCityName = 159
    elif OriginCityName == "Iron Mountain/Kingsfd, MI":
        OriginCityName = 160
    elif OriginCityName == "Islip, NY":
        OriginCityName = 161
    elif OriginCityName == "Ithaca/Cortland, NY":
        OriginCityName = 162
    elif OriginCityName == "Jackson, WY":
        OriginCityName = 163
    elif OriginCityName == "Jackson/Vicksburg, MS":
        OriginCityName = 164
    elif OriginCityName == "Jacksonville, FL":
        OriginCityName = 165
    elif OriginCityName == "Jacksonville/Camp Lejeune, NC":
        OriginCityName = 166
    elif OriginCityName == "Jamestown, ND":
        OriginCityName = 167
    elif OriginCityName == "Johnstown, PA":
        OriginCityName = 168
    elif OriginCityName == "Joplin, MO":
        OriginCityName = 169
    elif OriginCityName == "Juneau, AK":
        OriginCityName = 170
    elif OriginCityName == "Kahului, HI":
        OriginCityName = 171
    elif OriginCityName == "Kalamazoo, MI":
        OriginCityName = 172
    elif OriginCityName == "Kalispell, MT":
        OriginCityName = 173
    elif OriginCityName == "Kansas City, MO":
        OriginCityName = 174
    elif OriginCityName == "Kearney, NE":
        OriginCityName = 175
    elif OriginCityName == "Ketchikan, AK":
        OriginCityName = 176
    elif OriginCityName == "Key West, FL":
        OriginCityName = 177
    elif OriginCityName == "Killeen, TX":
        OriginCityName = 178
    elif OriginCityName == "King Salmon, AK":
        OriginCityName = 179
    elif OriginCityName == "Knoxville, TN":
        OriginCityName = 180
    elif OriginCityName == "Kodiak, AK":
        OriginCityName = 181
    elif OriginCityName == "Kona, HI":
        OriginCityName = 182
    elif OriginCityName == "Kotzebue, AK":
        OriginCityName = 183
    elif OriginCityName == "La Crosse, WI":
        OriginCityName = 184
    elif OriginCityName == "Lafayette, LA":
        OriginCityName = 185
    elif OriginCityName == "Lake Charles, LA":
        OriginCityName = 186
    elif OriginCityName == "Lanai, HI":
        OriginCityName = 187
    elif OriginCityName == "Lansing, MI":
        OriginCityName = 188
    elif OriginCityName == "Laramie, WY":
        OriginCityName = 189
    elif OriginCityName == "Laredo, TX":
        OriginCityName = 190
    elif OriginCityName == "Las Vegas, NV":
        OriginCityName = 191
    elif OriginCityName == "Latrobe, PA":
        OriginCityName = 192
    elif OriginCityName == "Lawton/Fort Sill, OK":
        OriginCityName = 193
    elif OriginCityName == "Lewisburg, WV":
        OriginCityName = 194
    elif OriginCityName == "Lewiston, ID":
        OriginCityName = 195
    elif OriginCityName == "Lexington, KY":
        OriginCityName = 196
    elif OriginCityName == "Liberal, KS":
        OriginCityName = 197
    elif OriginCityName == "Lihue, HI":
        OriginCityName = 198
    elif OriginCityName == "Lincoln, NE":
        OriginCityName = 199
    elif OriginCityName == "Little Rock, AR":
        OriginCityName = 200
    elif OriginCityName == "Long Beach, CA":
        OriginCityName = 201
    elif OriginCityName == "Longview, TX":
        OriginCityName = 202
    elif OriginCityName == "Los Angeles, CA":
        OriginCityName = 203
    elif OriginCityName == "Louisville, KY":
        OriginCityName = 204
    elif OriginCityName == "Lubbock, TX":
        OriginCityName = 205
    elif OriginCityName == "Lynchburg, VA":
        OriginCityName = 206
    elif OriginCityName == "Madison, WI":
        OriginCityName = 207
    elif OriginCityName == "Manchester, NH":
        OriginCityName = 208
    elif OriginCityName == "Manhattan/Ft. Riley, KS":
        OriginCityName = 209
    elif OriginCityName == "Marquette, MI":
        OriginCityName = 210
    elif OriginCityName == "Martha's Vineyard, MA":
        OriginCityName = 211
    elif OriginCityName == "Mason City, IA":
        OriginCityName = 212
    elif OriginCityName == "Medford, OR":
        OriginCityName = 213
    elif OriginCityName == "Melbourne, FL":
        OriginCityName = 214
    elif OriginCityName == "Memphis, TN":
        OriginCityName = 215
    elif OriginCityName == "Meridian, MS":
        OriginCityName = 216
    elif OriginCityName == "Miami, FL":
        OriginCityName = 217
    elif OriginCityName == "Midland/Odessa, TX":
        OriginCityName = 218
    elif OriginCityName == "Milwaukee, WI":
        OriginCityName = 219
    elif OriginCityName == "Minneapolis, MN":
        OriginCityName = 220
    elif OriginCityName == "Minot, ND":
        OriginCityName = 221
    elif OriginCityName == "Mission/McAllen/Edinburg, TX":
        OriginCityName = 222
    elif OriginCityName == "Missoula, MT":
        OriginCityName = 223
    elif OriginCityName == "Moab, UT":
        OriginCityName = 224
    elif OriginCityName == "Mobile, AL":
        OriginCityName = 225
    elif OriginCityName == "Moline, IL":
        OriginCityName = 226
    elif OriginCityName == "Monroe, LA":
        OriginCityName = 227
    elif OriginCityName == "Monterey, CA":
        OriginCityName = 228
    elif OriginCityName == "Montgomery, AL":
        OriginCityName = 229
    elif OriginCityName == "Montrose/Delta, CO":
        OriginCityName = 230
    elif OriginCityName == "Mosinee, WI":
        OriginCityName = 231
    elif OriginCityName == "Muskegon, MI":
        OriginCityName = 232
    elif OriginCityName == "Myrtle Beach, SC":
        OriginCityName = 233
    elif OriginCityName == "Nantucket, MA":
        OriginCityName = 234
    elif OriginCityName == "Nashville, TN":
        OriginCityName = 235
    elif OriginCityName == "New Bern/Morehead/Beaufort, NC":
        OriginCityName = 236
    elif OriginCityName == "New Haven, CT":
        OriginCityName = 237
    elif OriginCityName == "New Orleans, LA":
        OriginCityName = 238
    elif OriginCityName == "New York, NY":
        OriginCityName = 239
    elif OriginCityName == "Newark, NJ":
        OriginCityName = 240
    elif OriginCityName == "Newburgh/Poughkeepsie, NY":
        OriginCityName = 241
    elif OriginCityName == "Newport News/Williamsburg, VA":
        OriginCityName = 242
    elif OriginCityName == "Niagara Falls, NY":
        OriginCityName = 243
    elif OriginCityName == "Nome, AK":
        OriginCityName = 244
    elif OriginCityName == "Norfolk, VA":
        OriginCityName = 245
    elif OriginCityName == "North Bend/Coos Bay, OR":
        OriginCityName = 246
    elif OriginCityName == "North Platte, NE":
        OriginCityName = 247
    elif OriginCityName == "Oakland, CA":
        OriginCityName = 248
    elif OriginCityName == "Ogden, UT":
        OriginCityName = 249
    elif OriginCityName == "Ogdensburg, NY":
        OriginCityName = 250
    elif OriginCityName == "Oklahoma City, OK":
        OriginCityName = 251
    elif OriginCityName == "Omaha, NE":
        OriginCityName = 252
    elif OriginCityName == "Ontario, CA":
        OriginCityName = 253
    elif OriginCityName == "Orlando, FL":
        OriginCityName = 254
    elif OriginCityName == "Owensboro, KY":
        OriginCityName = 255
    elif OriginCityName == "Paducah, KY":
        OriginCityName = 256
    elif OriginCityName == "Pago Pago, TT":
        OriginCityName = 257
    elif OriginCityName == "Palm Springs, CA":
        OriginCityName = 258
    elif OriginCityName == "Panama City, FL":
        OriginCityName = 259
    elif OriginCityName == "Pasco/Kennewick/Richland, WA":
        OriginCityName = 260
    elif OriginCityName == "Pellston, MI":
        OriginCityName = 261
    elif OriginCityName == "Pensacola, FL":
        OriginCityName = 262
    elif OriginCityName == "Peoria, IL":
        OriginCityName = 263
    elif OriginCityName == "Petersburg, AK":
        OriginCityName = 264
    elif OriginCityName == "Philadelphia, PA":
        OriginCityName = 265
    elif OriginCityName == "Phoenix, AZ":
        OriginCityName = 266
    elif OriginCityName == "Pierre, SD":
        OriginCityName = 267
    elif OriginCityName == "Pittsburgh, PA":
        OriginCityName = 268
    elif OriginCityName == "Plattsburgh, NY":
        OriginCityName = 269
    elif OriginCityName == "Pocatello, ID":
        OriginCityName = 270
    elif OriginCityName == "Ponce, PR":
        OriginCityName = 271
    elif OriginCityName == "Portland, ME":
        OriginCityName = 272
    elif OriginCityName == "Portland, OR":
        OriginCityName = 273
    elif OriginCityName == "Portsmouth, NH":
        OriginCityName = 274
    elif OriginCityName == "Prescott, AZ":
        OriginCityName = 275
    elif OriginCityName == "Presque Isle/Houlton, ME":
        OriginCityName = 276
    elif OriginCityName == "Providence, RI":
        OriginCityName = 277
    elif OriginCityName == "Provo, UT":
        OriginCityName = 278
    elif OriginCityName == "Pueblo, CO":
        OriginCityName = 279
    elif OriginCityName == "Pullman, WA":
        OriginCityName = 280
    elif OriginCityName == "Punta Gorda, FL":
        OriginCityName = 281
    elif OriginCityName == "Raleigh/Durham, NC":
        OriginCityName = 282
    elif OriginCityName == "Rapid City, SD":
        OriginCityName = 283
    elif OriginCityName == "Redding, CA":
        OriginCityName = 284
    elif OriginCityName == "Reno, NV":
        OriginCityName = 285
    elif OriginCityName == "Rhinelander, WI":
        OriginCityName = 286
    elif OriginCityName == "Richmond, VA":
        OriginCityName = 287
    elif OriginCityName == "Riverton/Lander, WY":
        OriginCityName = 288
    elif OriginCityName == "Roanoke, VA":
        OriginCityName = 289
    elif OriginCityName == "Rochester, MN":
        OriginCityName = 290
    elif OriginCityName == "Rochester, NY":
        OriginCityName = 291
    elif OriginCityName == "Rock Springs, WY":
        OriginCityName = 292
    elif OriginCityName == "Rockford, IL":
        OriginCityName = 293
    elif OriginCityName == "Roswell, NM":
        OriginCityName = 294
    elif OriginCityName == "Sacramento, CA":
        OriginCityName = 295
    elif OriginCityName == "Saginaw/Bay City/Midland, MI":
        OriginCityName = 296
    elif OriginCityName == "Saipan, TT":
        OriginCityName = 297
    elif OriginCityName == "Salina, KS":
        OriginCityName = 298
    elif OriginCityName == "Salisbury, MD":
        OriginCityName = 299
    elif OriginCityName == "Salt Lake City, UT":
        OriginCityName = 300
    elif OriginCityName == "San Angelo, TX":
        OriginCityName = 301
    elif OriginCityName == "San Antonio, TX":
        OriginCityName = 302
    elif OriginCityName == "San Diego, CA":
        OriginCityName = 303
    elif OriginCityName == "San Francisco, CA":
        OriginCityName = 304
    elif OriginCityName == "San Jose, CA":
        OriginCityName = 305
    elif OriginCityName == "San Juan, PR":
        OriginCityName = 306
    elif OriginCityName == "San Luis Obispo, CA":
        OriginCityName = 307
    elif OriginCityName == "Sanford, FL":
        OriginCityName = 308
    elif OriginCityName == "Santa Ana, CA":
        OriginCityName = 309
    elif OriginCityName == "Santa Barbara, CA":
        OriginCityName = 310
    elif OriginCityName == "Santa Fe, NM":
        OriginCityName = 311
    elif OriginCityName == "Santa Maria, CA":
        OriginCityName = 312
    elif OriginCityName == "Santa Rosa, CA":
        OriginCityName = 313
    elif OriginCityName == "Sarasota/Bradenton, FL":
        OriginCityName = 314
    elif OriginCityName == "Sault Ste. Marie, MI":
        OriginCityName = 315
    elif OriginCityName == "Savannah, GA":
        OriginCityName = 316
    elif OriginCityName == "Scottsbluff, NE":
        OriginCityName = 317
    elif OriginCityName == "Scranton/Wilkes-Barre, PA":
        OriginCityName = 318
    elif OriginCityName == "Seattle, WA":
        OriginCityName = 319
    elif OriginCityName == "Sheridan, WY":
        OriginCityName = 320
    elif OriginCityName == "Shreveport, LA":
        OriginCityName = 321
    elif OriginCityName == "Sioux City, IA":
        OriginCityName = 322
    elif OriginCityName == "Sioux Falls, SD":
        OriginCityName = 323
    elif OriginCityName == "Sitka, AK":
        OriginCityName = 324
    elif OriginCityName == "South Bend, IN":
        OriginCityName = 325
    elif OriginCityName == "Spokane, WA":
        OriginCityName = 326
    elif OriginCityName == "Springfield, IL":
        OriginCityName = 327
    elif OriginCityName == "Springfield, MO":
        OriginCityName = 328
    elif OriginCityName == "St. Cloud, MN":
        OriginCityName = 329
    elif OriginCityName == "St. George, UT":
        OriginCityName = 330
    elif OriginCityName == "St. Louis, MO":
        OriginCityName = 331
    elif OriginCityName == "St. Petersburg, FL":
        OriginCityName = 332
    elif OriginCityName == "State College, PA":
        OriginCityName = 333
    elif OriginCityName == "Staunton, VA":
        OriginCityName = 334
    elif OriginCityName == "Stillwater, OK":
        OriginCityName = 335
    elif OriginCityName == "Stockton, CA":
        OriginCityName = 336
    elif OriginCityName == "Sun Valley/Hailey/Ketchum, ID":
        OriginCityName = 337
    elif OriginCityName == "Syracuse, NY":
        OriginCityName = 338
    elif OriginCityName == "Tallahassee, FL":
        OriginCityName = 339
    elif OriginCityName == "Tampa, FL":
        OriginCityName = 340
    elif OriginCityName == "Texarkana, AR":
        OriginCityName = 341
    elif OriginCityName == "Toledo, OH":
        OriginCityName = 342
    elif OriginCityName == "Traverse City, MI":
        OriginCityName = 343
    elif OriginCityName == "Trenton, NJ":
        OriginCityName = 344
    elif OriginCityName == "Tucson, AZ":
        OriginCityName = 345
    elif OriginCityName == "Tulsa, OK":
        OriginCityName = 346
    elif OriginCityName == "Twin Falls, ID":
        OriginCityName = 347
    elif OriginCityName == "Tyler, TX":
        OriginCityName = 348
    elif OriginCityName == "Valdosta, GA":
        OriginCityName = 349
    elif OriginCityName == "Valparaiso, FL":
        OriginCityName = 350
    elif OriginCityName == "Vernal, UT":
        OriginCityName = 351
    elif OriginCityName == "Victoria, TX":
        OriginCityName = 352
    elif OriginCityName == "Waco, TX":
        OriginCityName = 353
    elif OriginCityName == "Walla Walla, WA":
        OriginCityName = 354
    elif OriginCityName == "Washington, DC":
        OriginCityName = 355
    elif OriginCityName == "Waterloo, IA":
        OriginCityName = 356
    elif OriginCityName == "Watertown, NY":
        OriginCityName = 357
    elif OriginCityName == "Watertown, SD":
        OriginCityName = 358
    elif OriginCityName == "Wenatchee, WA":
        OriginCityName = 359
    elif OriginCityName == "West Palm Beach/Palm Beach, FL":
        OriginCityName = 360
    elif OriginCityName == "West Yellowstone, MT":
        OriginCityName = 361
    elif OriginCityName == "White Plains, NY":
        OriginCityName = 362
    elif OriginCityName == "Wichita Falls, TX":
        OriginCityName = 363
    elif OriginCityName == "Wichita, KS":
        OriginCityName = 364
    elif OriginCityName == "Williamsport, PA":
        OriginCityName = 365
    elif OriginCityName == "Williston, ND":
        OriginCityName = 366
    elif OriginCityName == "Wilmington, DE":
        OriginCityName = 367
    elif OriginCityName == "Wilmington, NC":
        OriginCityName = 368
    elif OriginCityName == "Worcester, MA":
        OriginCityName = 369
    elif OriginCityName == "Wrangell, AK":
        OriginCityName = 370
    elif OriginCityName == "Yakima, WA":
        OriginCityName = 371
    elif OriginCityName == "Yakutat, AK":
        OriginCityName = 372
    else:
        OriginCityName = 373

    # Making predictions
    prediction = classifier.predict(
        [[Airline, OriginCityName, Diverted, DistanceGroup, Quarter,
                       Month, DayofMonth, DayOfWeek, TaxiOut, DepTime,DepTimeBlk]])

    #if prediction == 1:
       # pred = 'DELAY'
    #else:
      #  pred = 'NO DELAY'
   # return pred

##<div style ="background-color:yellow;padding:13px">
# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """
    <div style ="background-color:blue;padding:13px">
      <h1 style ="color:black;text-align:center;">Fligt Delay Prediction System</h1>
    </div>
    """
    # display the front end aspect
    st.markdown(html_temp , unsafe_allow_html = True)

    # following lines create boxes in which user can enter data required to make prediction
    Airline = st.selectbox('Airline',("Air Wisconsin Airlines Corp","Alaska Airlines Inc.","Allegiant Air","American Airlines Inc.","Capital Cargo International","Comair Inc.",
                                      "Commutair Aka Champlain Enterprises, Inc.","Delta Air Lines Inc.","Empire Airlines Inc.","Endeavor Air Inc.",
                                      "Envoy Air","Frontier Airlines Inc.","GoJet Airlines LLC d/b/a United Express","Hawaiian Airlines Inc.","Horizon Air",
                                      "JetBlue Airways", "Mesa Airlines Inc.","Republic Airlines", "SkyWest Airlines Inc.","Southwest Airlines Co.","Spirit Air Lines","United Air Lines Inc."))
    OriginCityName = st.selectbox('OriginCityName',("Aberdeen, SD","Abilene, TX","Adak Island, AK","Aguadilla, PR","Akron, OH","Alamosa, CO ","Albany, GA","Albany, NY","Albuquerque, NM",
                                                    "Alexandria, LA","Allentown/Bethlehem/Easton, PA","Alpena, MI","Amarillo, TX","Anchorage, AK","Appleton, WI","Arcata/Eureka, CA","Asheville, NC",
                                                    "Ashland, WV","Aspen, CO","Atlanta, GA","Atlantic City, NJ","Augusta, GA","Austin, TX","Bakersfield, CA","Baltimore, MD","Bangor, ME","Barrow, AK","Baton Rouge, LA","Beaumont/Port Arthur, TX","Belleville, IL",
                                                    "Bellingham, WA","Bemidji, MN","Bend/Redmond, OR","Bethel, AK","Billings, MT","Binghamton, NY","Birmingham, AL","Bishop, CA","Bismarck/Mandan, ND","Bloomington/Normal, IL",
                                                    "Boise, ID","Boston, MA","Bozeman, MT","Brainerd, MN","Branson, MO","Bristol/Johnson City/Kingsport, TN","Brownsville, TX","Brunswick, GA","Buffalo, NY","Burbank, CA","Burlington, VT","Butte, MT","Cape Girardeau, MO","Casper, WY","Cedar City, UT","Cedar Rapids/Iowa City, IA","Champaign/Urbana, IL","Charleston, SC","Charleston/Dunbar, WV","Charlotte Amalie, VI","Charlotte, NC","Charlottesville, VA","Chattanooga, TN","Cheyenne, WY","Chicago, IL","Christiansted, VI","Cincinnati, OH","Clarksburg/Fairmont, WV","Cleveland, OH","Cody, WY","Cold Bay, AK","College Station/Bryan, TX","Colorado Springs, CO","Columbia, MO","Columbia, SC","Columbus, GA","Columbus, MS","Columbus, OH","Concord, NC","Cordova, AK","Corpus Christi, TX","Dallas, TX","Dallas/Fort Worth, TX","Dayton, OH","Daytona Beach, FL","Deadhorse, AK", "Decatur, IL","Del Rio, TX","Denver, CO","Des Moines, IA","Detroit, MI","Devils Lake, ND","Dickinson, ND","Dillingham, AK", "Dodge City, KS","Dothan, AL","Dubuque, IA", "Duluth, MN","Durango, CO","Eagle, CO","Eau Claire, WI","El Paso, TX.","Elko, NV","Elmira/Corning, NY","Erie, PA","Escanaba, MI","Eugene, OR","Evansville, IN","Everett, WA","Fairbanks, AK","Fargo, ND","Fayetteville, AR","Fayetteville, NC","Flagstaff, AZ","Flint, MI","Florence, SC","Fort Dodge, IA","Fort Lauderdale, FL","Fort Leonard Wood, MO","Fort Myers, FL","Fort Smith, AR", "Fort Wayne, IN","Fresno, CA",
                                                    "Gainesville, FL","Garden City, KS","Gillette, WY","Grand Forks, ND","Grand Island, NE","Grand Junction, CO","Grand Rapids, MI","Great Falls, MT","Green Bay, WI", "Greensboro/High Point, NC", "Greenville, NC","Greer, SC","Guam, TT","Gulfport/Biloxi, MS","Gunnison, CO","Gustavus, AK",
                                                    "Hagerstown, MD","Hancock/Houghton, MI","Harlingen/San Benito, TX","Harrisburg, PA","Hartford, CT","Hattiesburg/Laurel, MS","Hayden, CO","Hays, KS","Helena, MT","Hibbing, MN","Hilo, HI","Hilton Head, SC","Hobbs, NM","Honolulu, HI","Hoolehua, HI","Houston, TX", "Huntsville, AL","Hyannis, MA","Idaho Falls, ID","Indianapolis, IN","International Falls, MN","Iron Mountain/Kingsfd, MI","Islip, NY",
                                                    "Ithaca/Cortland, NY","Jackson, WY","Jackson/Vicksburg, MS","Jacksonville, FL","Jacksonville/Camp Lejeune, NC",
                                                    "Jamestown, ND","Johnstown, PA","Joplin, MO","Juneau, AK","Kahului, HI","Kalamazoo, MI","Kalispell, MT","Kansas City, MO","Kearney, NE","Ketchikan, AK","Key West, FL","Killeen, TX","King Salmon, AK","Knoxville, TN","Kodiak, AK","Kona, HI",
                                                    "Kotzebue, AK","La Crosse, WI","Lafayette, LA","Lake Charles, LA","Lanai, HI","Lansing, MI","Laramie, WY","Laredo, TX","Las Vegas, NV","Latrobe, PA","Lawton/Fort Sill, OK","Lewisburg, WV","Lewiston, ID","Lexington, KY","Liberal, KS","Lihue, HI","Lincoln, NE","Little Rock, AR","Long Beach, CA","Longview, TX","Los Angeles, CA",
                                                    "Louisville, KY","Lubbock, TX", "Lynchburg, VA","Madison, WI","Manchester, NH","Manhattan/Ft. Riley, KS","Marquette, MI",
                                                    "Martha's Vineyard, MA","Mason City, IA","Medford, OR","Melbourne, FL","Memphis, TN","Meridian, MS","Miami, FL",
                                                    "Midland/Odessa, TX","Milwaukee, WI","Minneapolis, MN","Minot, ND","Mission/McAllen/Edinburg, TX","Missoula, MT","Moab, UT","Mobile, AL","Moline, IL","Monroe, LA","Monterey, CA","Montgomery, AL","Montrose/Delta, CO","Mosinee, WI","Muskegon, MI","Myrtle Beach, SC","Nantucket, MA","Nashville, TN","New Bern/Morehead/Beaufort, NC","New Haven, CT","New Orleans, LA",
                                                    "New York, NY","Newark, NJ","Newburgh/Poughkeepsie, NY","Newport News/Williamsburg, VA","Niagara Falls, NY","Nome, AK",
                                                    "Norfolk, VA","North Bend/Coos Bay, OR","North Platte, NE", "Oakland, CA","Ogden, UT","Ogdensburg, NY","Oklahoma City, OK","Omaha, NE","Ontario, CA","Orlando, FL",
                                                    "Owensboro, KY","Paducah, KY","Pago Pago, TT", "Palm Springs, CA","Panama City, FL","Pasco/Kennewick/Richland, WA","Pellston, MI","Pensacola, FL","Peoria, IL","Petersburg, AK","Philadelphia, PA","Phoenix, AZ","Pierre, SD","Pittsburgh, PA", "Plattsburgh, NY","Pocatello, ID",
                                                    "Ponce, PR", "Portland, ME","Portland, OR","Portsmouth, NH","Prescott, AZ","Presque Isle/Houlton, ME","Providence, RI","Provo, UT","Pueblo, CO","Pullman, WA","Punta Gorda, FL","Raleigh/Durham, NC","Rapid City, SD","Redding, CA","Reno, NV",
                                                    "Rhinelander, WI","Richmond, VA","Riverton/Lander, WY","Roanoke, VA","Rochester, MN","Rochester, NY","Rock Springs, WY","Rockford, IL","Roswell, NM","Sacramento, CA","Saginaw/Bay City/Midland, MI","Saipan, TT","Salina, KS","Salisbury, MD","Salt Lake City, UT",
                                                    "San Angelo, TX","San Antonio, TX","San Diego, CA","San Francisco, CA","San Jose, CA","San Juan, PR","San Luis Obispo, CA","Sanford, FL","Santa Ana, CA","Santa Barbara, CA","Santa Fe, NM","Santa Maria, CA","Santa Rosa, CA","Sarasota/Bradenton, FL","Sault Ste. Marie, MI","Savannah, GA","Scottsbluff, NE","Scranton/Wilkes-Barre, PA",
                                                    "Seattle, WA","Sheridan, WY","Shreveport, LA","Sioux City, IA","Sioux Falls, SD", "Sitka, AK",
                                                    "South Bend, IN","Spokane, WA","Springfield, IL","Springfield, MO","St. Cloud, MN","St. George, UT","St. Louis, MO","St. Petersburg, FL","State College, PA",
                                                    "Staunton, VA","Stillwater, OK", "Stockton, CA","Sun Valley/Hailey/Ketchum, ID","Syracuse, NY","Tallahassee, FL","Tampa, FL","Texarkana, AR","Toledo, OH","Traverse City, MI","Trenton, NJ","Tucson, AZ","Tulsa, OK","Twin Falls, ID","Tyler, TX","Valdosta, GA", "Valparaiso, FL","Vernal, UT","Victoria, TX","Waco, TX","Walla Walla, WA","Washington, DC","Waterloo, IA","Watertown, NY","Watertown, SD","Wenatchee, WA","West Palm Beach/Palm Beach, FL","West Yellowstone, MT","White Plains, NY","Wichita Falls, TX","Wichita, KS","Williamsport, PA","Williston, ND","Wilmington, DE","Wilmington, NC","Worcester, MA","Wrangell, AK","Yakima, WA","Yakutat, AK","Yuma, AZ"))
    DistanceGroup = st.selectbox('Distance Group',("1(0-250 Miles)","2(251-500 Miles)","3(501-750 Miles)","4(751-1000 Miles)","5(1001-1250 Miles)",
                                                    "6(1251-1500 Miles)","7(1501-1750 Miles)","8(1751-2000 Miles)","9(2001-2250 Miles)",
                                                    "10(2501-2750 Miles)","11(2751-3000 Miles)"))
    Quarter=st.selectbox('Quarter',("1(Jan-Mar)","2(Apr-Jun)","3(Jul-Sep)","4(Oct-Dec)"))
    Month=st.selectbox('Month',("January","February","March","April","May","June","July","August","September","October", "November","December"))
    DayofMonth = st.number_input("Date", min_value=1, max_value=31, value=1, step=1)
    DayOfWeek = st.selectbox('Day of Week',("Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday"))
    TaxiOut = st.number_input("Taxi Out(Min)-Optional",min_value=0, max_value=2359, value=0000, step=1)
    Diverted= st.selectbox('Diverted-Optional',("False","True"))
    DepTime = st.number_input("Departure Time",min_value=0, max_value=2359, value=0000, step=1)
    DepTimeBlk = st.selectbox('Time Block',("0001-0559","0600-0659","0700-0759","0800-0859","0900-0959","1000-1059","1100-1159",
                                            "1200-1259","1300-1359","1400-1459","1500-1559","1600-1659","1700-1759", "1800-1859",
                                            "1900-1959","2000-2059","2100-2159","2200-2259","2300-2359"))
    result =""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(Airline, OriginCityName, Diverted, DistanceGroup, Quarter,Month, DayofMonth, DayOfWeek, TaxiOut, DepTime,DepTimeBlk)
        if result == 1:
            st.markdown(
                f'<div style="background-color:red; padding:10px;">Your Flight is Delay</div>'
        else:
                f'<div style="background-color:green; padding:10px;">Your Flight is No Delay</div>'
                unsafe_allow_html=True
            )
            

if __name__=='__main__':
    main()
