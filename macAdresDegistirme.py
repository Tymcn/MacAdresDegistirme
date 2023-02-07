import subprocess
import optparse

parseObject=optparse.OptionParser()
parseObject.add_option("-i","--interface",dest="interface",help="İNTERFACE OLUŞTURULDU")
parseObject.add_option("-m","--mac",dest="macAdres",help="MAC ADRES OLUŞTURULDU")

(userinputs,arguments)=parseObject.parse_args()

userInterface=userinputs.interface
userMacAdres=userinputs.macAdres

print("MAC ADRESİNİZ DEĞİŞTİRİLDİ.")


subprocess.call(["ifconfig",userInterface,"down"])
subprocess.call(["ifconfig",userInterface,"hw","ether",userMacAdres])
subprocess.call(["ifconfig",userInterface,"up"])