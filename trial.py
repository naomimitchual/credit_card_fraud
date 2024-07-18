def decode(message_file):
    """
    function to decode a messsage file depending on the pyramid formed from the numbers in the respective words.
    input: message file
    ouput: decode message
    """
    nums = [] # list to hold all the numbers
    look_up = {} # a  look dictionary associating every number with a word
    with open(message_file, "r") as file_obj: # read the file and get all numbers and associated words
        for line in file_obj:
            num, msg = line.split() 
            nums.append(int(num))
            look_up[int(num)] =  msg
        file_obj.close()
    
    nums.sort() # sort numbers to form a pyramid
    pyramid = []
    level = 1

    while len(nums) != 0:
        if len(nums)>= level:
            try:
                pyramid.append(nums[0:level])
                nums = nums[level:]
                level += 1
            except Exception as e:
                print("an error occurred: {e}")

    return ' '.join([look_up[i[-1]] for i in pyramid]) # get every last number for every level

print(decode(message_file="coding_qual_input.txt"))










