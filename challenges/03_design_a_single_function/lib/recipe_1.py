def reading_time_calculator(passage):
    if passage == None:
        raise Exception("Error: None")

    time_taken = passage/200
    absolute_time_taken = time_taken
    time_in_minutes = int(absolute_time_taken)
    
    if time_taken == 0:
        return "No text provided"
    elif time_taken == 1:
        time_in_minutes = int(time_taken)
        sentence = str(int(time_in_minutes)) + " minute to read"
    elif time_taken > 1:
        time_in_seconds = int((absolute_time_taken - time_in_minutes)*60)
        if time_in_minutes > 1:
            sentence = str(time_in_minutes) + " minutes " + str(time_in_seconds) + " seconds to read" 
        else:
            sentence = str(time_in_minutes) + " minute " + str(time_in_seconds) + " seconds to read"
    elif time_taken < 1:
        time_in_seconds = int((absolute_time_taken - time_in_minutes)*60)
        absolute_time_in_seconds = (absolute_time_taken - time_in_minutes)*60
        if absolute_time_in_seconds <= 1:
            sentence = "Less than 1 second to read"
        else:
            sentence = str(time_in_seconds) + " seconds to read"


    return sentence