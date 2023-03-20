data = [
        (1234,'Abhishek',32,35000),
        ( 4532,'Bharathi',27,29000),
        (3455,'Charan',31,37000),
        (9863,'Devi',42,52000), 
	    (4852, 'Eswar', 37, 56000), 
	    (6481, 'Fathima', 40, 65000), 
        (2793, 'Ganesh', 28, 45000)
   ]
for id,name,age,salary in data:
    sorted = sorted(key=lambda x:x[3])
    