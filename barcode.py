import barcode
import datetime
import os
from barcode.writer import ImageWriter

# membaca daftar kode dari file
with open('code_list.txt', 'r') as f:
    codes = f.read().splitlines()

# membuat folder "Voucher" jika belum ada
folder = "Voucher"
if not os.path.exists(folder):
    os.makedirs(folder)

# membuat barcode dan menyimpannya dalam format PNG
for i, code in enumerate(codes):
    code128 = barcode.get('code128', code, writer=ImageWriter())
    filename = f"{i+1}_{datetime.date.today().strftime('%Y-%m-%d')}_{code}.png"
    code128.save(os.path.join(folder, filename))
