import python_whatsapp_bot as pwb

with open ("API.key", "r") as file:
    API_TOKEN = "flux_e6e10242g5m4y3y4y714u3ii3692q151g652y1yl4p12z426z144d5d5x4m" #file.readline().strip()
    NUMBER_ID = 669612896230116 #file.readline()
    bot = pwb.Whatsapp(token=API_TOKEN, number_id=NUMBER_ID)

bot.send_message(11992889494, 'testandoo')