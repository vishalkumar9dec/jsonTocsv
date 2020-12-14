import json
import convertFile.dbOperations as DB
import ntpath

#Global Valiables
source_dir = '/var/opt/app/json_logs/logs.json'
dest_dir = '/var/opt/app/csv_logs'


'''Function definitions'''
DB.createTable()

def convertToCSV():
    try:
        with open(source_dir+'logs.json') as fname:
            if fname.split(".")[1] != "json":
               print("ERROR : Input file is not in JSON format")
            else:
                data = json.load(fname)
                output_file = dest_dir+fname.split(".")[0] + "_converted.csv"
                for i in range(len(data['Records'])):
                    try:
                        uname = data['Records'][i]['userIdentity']['sessionContext']['sessionIssuer']['userName']
                    except:
                        uname = ""
                    try:
                        eventname = data['Records'][i]['eventName']
                    except:
                        eventname = ""
                    try:
                        eventtime = data['Records'][i]['eventTime']
                    except:
                        eventtime = ""
                    try:
                        eventsource = data['Records'][i]['eventSource']
                    except:
                        eventsource = ""
                    try:
                        eventtype = data['Records'][i]['eventType']
                    except:
                        eventtype = ""

                    DB.truncateTable()
                    DB.insertData(uname, eventname, eventtype, eventsource, eventtime)
                    data_db = DB.queryData()

                try:
                    with open(output_file, 'a') as file:
                        file.write('Username,EventName,EventTime,EventSource,EventType\n')
                        for row in data_db:
                            file.write(row[0] + ',' + row[1] + ',' + row[2] + ',' + row[3] + ',' + row[4] + '\n')
                        print("Json file converted to CSV successfully and import to DB !")
                except:
                    print("Oops! Some Error Occurred")
                    print("This will be logged into a logfile.")

    except IOError:
        print("File not available for processing")
        print("Please check the source directory")