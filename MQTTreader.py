from tkinter import *
import re

# 
def ValueAdder(value, endVal, data):
    
    array = []

    for x in range(value, endVal):

        array.append(data[x])

    #print(array)
    return array

def EvalElement(data):
    
    count = 0
    for i in data:
        fullstr = i

        if (fullstr.find("|") != -1):            
            #print("Contains substring")
            return count
        count += 1

def PrintElements(words, values):
    count = 0
    array = []
    print("---------------------------------------------------")
    for i in words:
        string = i + ": " + values[count]
        array.append(string)
        count += 1
    return array

def close_window():
    window.destroy()
    exit()

def parsing_loop(mqttData):
    
    #mqttData = 'dateTimestamp;dateTimestampUtc;iValue29;vGPSlongitude;vGPSlatitude;iValue26;vDEFlevel;vGSMsignalQuality;vGPSsignalQuality;vPrimaryStatus;vGroundSpeed;iValue28;iValue27;statYieldTonsHa;alarmCritical;alarmFiltersOil;alarmEngine;iValue1;iValue2;iValue3;iValue4;iValue5;iValue6;iValue7;iValue8;iValue9;iValue10;iValue11;iValue12;iValue13;iValue14;iValue15;iValue16;iValue17;iValue18;iValue19;iValue20;iValue21;iValue22;iValue23;iValue24;iValue25;bValue10;bValue11;alarmShafts;alarmPropelSystem;alarmElectrical;alarmTemperature;vGPSaltitude;vGPScompassBearing;vSecundaryStatus;vCustomDistance;vCustomHectars;vCustomTons;fValue2;vEngCoolantTemp;vEngSpd;vEngLoad;vEngFuelrate;vEngIntakeManTemp;|2022-06-03 12:44:25.982;2022-06-03 15:40:03.571;0.00;-78.0909347534;43.0608367920;0.00;0.00;-77;50;1;0.00;0.0;0.0;;0;0;0;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0;0.00;0;0;0;0;0.00;0.00;;0.0;0.00;0.0;0.0;0.0;;;;0.0;'

    mqttData_split = mqttData.split(';')
    mqttData_len = len(mqttData_split)
    half_len = mqttData_len / 2
    #print(mqttData_len)
    #print(mqttData_split)

    # Finds the value of element to start adding values into ValueArray

    start_count = EvalElement(mqttData_split)
    word_end_cnt = start_count
    start_wrd_count = 0

    WordArray = ValueAdder(start_wrd_count, word_end_cnt, mqttData_split)
    ValueArray = ValueAdder(start_count, mqttData_len, mqttData_split)

    formArray = PrintElements(WordArray, ValueArray)

    return formArray

def click():
    entered_text = textentry.get()
    output.delete(0.0, END)
    try:
        mqttData = entered_text        
    except:
        mqttData = "ERROR"
    dataArray = parsing_loop(mqttData)
    x=0
    for x in range(len(dataArray)):
        output.insert(END, dataArray[x]+"\n")


window = Tk()
window.title("MQTT READER")
window.configure(background="black")

#create label
Label(window, text="Enter the data to be parsed:", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)

#text entry
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

#add a submit button
Button(window, text="SUBMIT", width=6, command=click) .grid(row=3, column=0, sticky=W)

# add another label
Label (window, text="\nDATA:", bg="black",fg="white",font="none 12 bold") .grid(row=4,column=0,sticky=W)

#create output text box
output = Text(window,width=75, height=70, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

# exit label 
Label(window, text="Click To exit", bg="black", fg="white", font="none 12 bold") .grid(row=6, column=0, sticky=W)

Button(window, text="Exit", width=14, command=close_window) .grid(row=7,column=0, sticky=E)


window.mainloop()