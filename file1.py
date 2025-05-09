#!/bin/python3
import pyotp
import qrcode
#create a TOTP object 
T = pyotp.TOTP('3232323232323232')
print(T)
print(T.now)

#User enters an OTP 
user_otp = float(input("Enter an OTP: "))
#Verify the entered otp
if T.verify(user_otp):
	print("OTP is valid!")
else:
	print("invalid OTP")
#Generate the provisioning URI
auth_str = T.provisioning_uri(name="xk0DolapotheEthicalHacker",issuer_name="DolapotheEthicalHacker")
ing = qrcode.make(auth_str)
ing.show() #This will show the qrcode
