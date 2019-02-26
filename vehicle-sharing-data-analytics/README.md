# Vehicle-Sharing Coding Exercise

The input to your program is a text file containing a list of events from a completed simulation. The format of the events is:

| Data        | Type           | Description  |
| ------------- |-------------| -----|
| timestamp       | Integer        | The time in seconds since the start of the simulation |
| vehicle_id       | String        | The id of the associated  vehicle, e.g. JK5T |
| event_type       | String        | The type of the event is one of START_RIDE, END_RIDE, DROP |
| x       | Double        | The x coordinate of the location of where the event happened in the simulation |
| y       | Double        | The y coordinate of the location of where the event happened in the simulation |
| user_id       | Integer        | The id of the associated user or NULL if the event does not have an associated user |
   
Each column is separated by a comma (,) and each line represents a single event. The list is ordered by time starting with the first event that happened.

## Goal:

The goal of the program is to parse a list of such events and print out to the command line (stdout) answers to the following questions. A list of sample events of one completed simulation is sent as a separate file, so you can test your code with them. Assume each question has exactly one valid answer, each bird has been dropped off as its first event and all rides have a start and end event.

## Questions:

1. What is the total number of vehicles dropped off in the simulation?
2. Which vehicle ends up the farthest away from its drop location? What is the distance?
3. Which vehicle has traveled the longest distance in total on all of its rides? How far is it?

