from speedtest import Speedtest

st = Speedtest()

print("welcome to dz wifi speed counter")
print("your speed is being counting. it may take less than a minute")
print("your conection's doenload speed is:  ",st.download(),"bites")
print("your conection's upload speed is:  ",st.upload(),"bites")