import csv  
import pandas as pd
### To elemenate , from the from the cells which have no contant
def convert_null(cell):
    if cell=="":
        return ''
    return "," + cell

##Read csv file
df = pd.read_csv("C:\\Users\\devop\\Desktop\\visualcode\\Python\\output\\op.csv", converters = { 
        'sprint': convert_null, 'sprint.1': convert_null, 'sprint.2': convert_null, 
        'sprint.3': convert_null, 'sprint.4': convert_null, 'sprint.5': convert_null,
        'sprint.6': convert_null, 'sprint.7': convert_null, 'sprint.8': convert_null,
        'sprint.9': convert_null, 'sprint.10': convert_null, 'sprint.11': convert_null,
        'label': convert_null, 'label.1': convert_null, 'label.2': convert_null,
        'label.3': convert_null, 'label.4': convert_null, 'label.5': convert_null,
        'label.6': convert_null, 'label.7': convert_null, 'label.8': convert_null,
        'label.9': convert_null, 'label.10': convert_null, 'label.11': convert_null,
})

####To find number of columns with name sprint*
loop = 1
count_sprint = 0
while loop <= 10:
    sprint = "sprint.%s" %loop
    if sprint in df.columns:
        count_sprint = count_sprint + 1
    loop = loop + 1
print("sprint count is:", count_sprint)

####To find number of columns with name label*
loop = 1
count_label = 0
while loop <= 10:
    label = "label.%s" %loop
    if label in df.columns:
        count_label = count_label + 1
    loop = loop + 1
print("labels count is:", count_label)

###instood of converters in df
b = "'sprint': convert_null,\n"
j = 1
while j <= count_sprint:
    a = "'sprint.%s'" %j + ": convert_null,\n"
    b = b + a 
    j = j + 1
print(b)

## To append all the sprint*
df['Sprint'] = df['sprint']
i = 1
while i <= count_sprint:
    a = "sprint.%s" %i
    df['Sprint'] = df['Sprint'] + df['%s' %a]
    i = i + 1

## To append all the label*
df['Label'] = df['label']
i = 1
while i <= count_label:
    a = "label.%s" %i
    df['Label'] = df['Label'] + df['%s' %a]
    i = i + 1

## To write output to the csv file
df.to_csv('C:\\Users\\devop\\Desktop\\visualcode\\Python\\output\\new.csv', columns=['S.no', 'Sprint', 'Test', 'Label'], index=False)
