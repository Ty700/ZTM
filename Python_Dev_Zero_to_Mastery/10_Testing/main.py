def do_stuff(num):
    try:
        if num:
            return int(num) + 5
        else:
            return 'Please enter a number'
        
    except (TypeError, ValueError) as error:
        return error

