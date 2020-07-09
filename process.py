log_file = open("um-server-01.txt")
# opening files kept on a server?


def sales_reports(log_file):
	# defining a function (specifically reviewing a file containing orders)
    for line in log_file: 
    	# checking each line in a file/document
        line = line.rstrip()
        # rstrip removes trailing characters or spaces of a string.
        day = line[0:3] 
        # when I ran the code in vagrant the first 3 characters of
        # every line were Tue, so this must be to know or change the 
        # day of the week that we want to look at in the report.
        if day == "Mon":
        	# email from ubermelon lead said to look at 
        	# Monday's data, so switched Tue to Mon to only 
        	# view Monday data.
            print(line)
            # prints all of Monday's orders/sales delivered

sales_reports(log_file)
# calling the function (or running the report with the above specified data)
