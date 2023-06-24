import requests as r

nft_transactions = "https://etherscan.io/nft-transfers?a=0x90f37809cccf13705a1f5e9fca645ba3fd58773c"
nft_transaction_post_url = "https://etherscan.io/nft-transfers.aspx/GetTableData_NftTransfers"


headers = {
    "Host": "etherscan.io",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-User": "?1"
}


resp = r.get(url=nft_transactions, headers=headers)
print(resp.status_code)


headers = {
    "Host": "etherscan.io",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://etherscan.io/nft-transfers?a=0x90f37809cccf13705a1f5e9fca645ba3fd58773c",
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "1060",
    "Origin": "https://etherscan.io",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

false = False
true = True
null = None

payload = {
    "dataTableModel":
    {"draw": 2,
     "columns":
     [{"data": "preview", "name": "", "searchable": true, "orderable": false, "search":
       {"value": "", "regex": false}},
      {"data": "txhash", "name": "", "searchable": true, "orderable": false, "search":
       {"value": "", "regex": false}},
      {"data": "txMethod", "name": "", "searchable": true, "orderable": false, "search":
       {"value": "", "regex": false}},
      {"data": "dt", "name": "", "searchable": true, "orderable": false, "search": {"value": "", "regex": false}},
      {"data": "_from", "name": "", "searchable": true, "orderable": false, "search": {"value": "", "regex": false}},
      {"data": "arrow", "name": "", "searchable": true, "orderable": false, "search": {"value": "", "regex": false}},
      {"data": "_to", "name": "", "searchable": true, "orderable": false, "search": {"value": "", "regex": false}},
      {"data": "type", "name": "", "searchable": true, "orderable": false, "search": {"value": "", "regex": false}},
      {"data": "tokenAddress", "name": "", "searchable": true, "orderable": false,
       "search": {"value": "", "regex": false}}],
     "order": [],
     "start": 25, "length": 25, "search": {"value": "", "regex": false},
     "Ext": "0x90f37809cccf13705a1f5e9fca645ba3fd58773c"}}

data = r.post(nft_transaction_post_url, json=payload, headers=headers)
data_json = data.json()

print(data_json)
