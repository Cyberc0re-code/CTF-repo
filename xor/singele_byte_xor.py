import binascii
ct="9bfdb1b2aae1e3e1aaffb3fea6b2b4fb59450d4c0d5e44434a41480d4f545948e2ffa7edeeb4b6f5a9f1e2e0aaf1e2b4a4d1a3daf89dabd3a1c9a4d7b9cef3d3757e774d267c764d61237f627e216f"
ct_enc=binascii.unhexlify(ct)
for i in range(256):
	flag=''
	for j in range(len(ct_enc)):
		flag+=chr(ct_enc[j]^i)
	print(flag)
	
