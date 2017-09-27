import requests
import json
import xlrd

# replace the delete_list.xls with you own xls' file name
xls_data = xlrd.open_workbook("delete_list.xls")
xls_table = xls_data.sheet_by_index(0)
xls_rows = xls_table.nrows


def run():

    url = 'https://openapi.youku.com/v2/videos/destroy.json'

    # replace your private parameter below(client_id / access_token / video_page)
    payloads = {'client_id':'99989a******dd0b','access_token':'6253aa*******7bdc905c9ff','video_id':50}
    delete_videos(xls_rows,url,payloads)


def delete_videos(rows,url,payloads):
    # this fuction get the all json files and deal with the data
    for i in range(rows):
        payloads['video_id'] = str(xls_table.cell(i,0))
        print(payloads['video_id'])
        requests.get(url, params=payloads)

run()