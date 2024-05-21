Pseudo code for - Overprice

OPEN and READ the file 
READ each line in the file
LOOP through each line 
PARSE out contents (product, date, price) - remove date
CREATE 1 dictionary (k=v), key=item , value = tuple/list of count_over $4 and count of product
INCREMENT count of product - keep count of every product we come across - in the dictionary value[1]
2nd INCREMENT count of product_over $4 - in the dictionary value[0] - use if statement

LOOP through dictionary 
PRINT key=product, percentage = value[0]/value[1] * 100

DINGS:
No stripping of lines and split, we can argue for PARSE
No conditional statements