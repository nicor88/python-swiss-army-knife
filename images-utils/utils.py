def delete_date_symbols(date,dateFormat):
    if(dateFormat == 'YYYY-MM-DD HH:MM:SS'):
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        hours = date[11:13]
        minutes = date[14:16]
        seconds = date[17:19]
        formattedDate=year+month+day+hours+minutes+seconds
        return formattedDate
    else:
        return 'pass a date formatted as YYYY-MM-DD HH:MM:SS'