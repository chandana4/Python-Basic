from time import localtime

activities = {8: 'Getting ready for College',
              9: 'College starting',
	      15:'Studying',
              17: 'Back from college',
              18: 'Resting',
              20: 'Eating',
              22: 'Resting' }

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]
	print "The time is ",hour
        break
else:
    print 'Unknown Activity!'
