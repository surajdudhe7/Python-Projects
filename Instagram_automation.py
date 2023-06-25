from instabot import Bot
bot=Bot
bot.login(username="abc0001",password="Abc@123")
bot.upload_photo("c:/users/photo.jpg")
bot.filter_medias('pqr')
bot.unfollow('pqr')
bot.send_message("I love python ",['pqr','abc'])
followers=bot.get_user_followers("abc")
for Followers in followers:
    print(bot.get_user_info(followers))
following=bot.get_user('username')
for Following in following:
    print(bot.get_user_info(following))