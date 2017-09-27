import requests
from openpyxl import load_workbook

# replace the delete_list.xls with you own xls' file name
xls_data = load_workbook(filename="delete_list.xlsx")
xls_table = xls_data.worksheets[0]
xls_rows = xls_table.max_row


def run():

    url = 'https://openapi.youku.com/v2/videos/destroy.json'

    # replace your private parameter below(client_id / access_token)
    payloads = {'client_id':'99989a******dd0b','access_token':'6253aa*******7bdc905c9ff','video_id':'str'}
    delete_videos(xls_rows,url,payloads)


def delete_videos(rows,url,payloads):
    
    for i in range(1,rows+1):
        id = xls_table.cell(row=i,column=1).value
        payloads['video_id'] = id
        print(payloads)
        requests.get(url, params=payloads)

run()