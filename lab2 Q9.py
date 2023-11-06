from datetime import datetime
dep_time = input("Enter departure time (HH:MM): ")
arr_time = input("Enter arrival time (HH:MM): ")
dep_datetime = datetime.strptime(dep_time, "%H:%M")
arr_datetime = datetime.strptime(arr_time, "%H:%M")
trip_time = arr_datetime - dep_datetime
print(trip_time) #this print time in a format but can't display hours and minutes individually
# <trip_time> is a structure deal with 'seconds' item -> so triptime will be hours and minutes separately
   #for ex: triptime is  1:20     to convert it to seconds:  (1*60*60 + 20*60)=4800 sec
                                                    #     to get time in hour :   4800/(60*60)=1.33333  so hours in integer type =1 hour
hours = trip_time.seconds//3600
minutes = (trip_time.seconds%3600)//60              #     to get time in min :   to calc %  [1.33333-1=.33333] then .33333*3600=1200  so 1200/60 =20min
print("Trip time: {} hrs and {} min".format(hours, minutes))
