from pyrogram import Client
from pyrogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery, InlineQueryResultArticle, InputTextMessageContent

api_id = 3330082
api_hash = 'a8c8207cff88b514f9906e2f58ddb123'
bot_token = '1602446423:AAGzEXvQiLgC8AE-rT9emdcTsJmffcg1e2c'

##############################################################################################################################################

round = 0
table = [[('1','block00'), ('2','block01'), ('3','block02')],[('4','block10'), ('5','block11'), ('6','block12')],[('7','block20'), ('8','block21'), ('9','block22')]]

def IKM2D(table):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, cbd) for text, cbd in row] for row in table])
def IKM(data):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, cbd) for text, cbd in row] for row in data])


client = Client(session_name = 'My_Bot', bot_token = bot_token, api_id = api_id, api_hash = api_hash)
Ps = []

#====================================================================================================================================================

@client.on_message()
def handle_message(bot,message) :
    if message.text :
        if message.text == '/start' :
            bot.send_message(message.chat.id, '''π  Hi

π  Thanks for playing with my XO Bot !''', reply_markup = ReplyKeyboardMarkup([['ββ­οΈ Play β­οΈβ'], ['π Credit π']]))

        elif message.text == 'π Credit π' :
            bot.send_message(message.chat.id, '''π₯  Written & Developed by  π₯
            
            π Yousof Asadi π :
               @Yousof_Asadi''')

        elif message.text == 'ββ­οΈ Play β­οΈβ':
            bot.send_message(message.chat.id,'''π’ Sorry , this bot is inline.
βΊοΈ You can use it by typing @XO_YA_bot in a group or private chat of your friends. ''', reply_markup = ReplyKeyboardRemove())

########################################################################################################################################

def check_winner (table) :

    if table[0][0][0] == table[0][1][0] == table[0][2][0] :
        return table[0][0][0]
    elif table[1][0][0] == table[1][1][0] == table[1][2][0] :
        return table[1][0][0]
    elif table[2][0][0] == table[2][1][0] == table[2][2][0] :
        return table[2][0][0]
    elif table[0][0][0] == table[1][0][0] == table[2][0][0] :
        return table[0][0][0]
    elif table[0][1][0] == table[1][1][0] == table[2][1][0] :
        return table[0][1][0]
    elif table[0][2][0] == table[1][2][0] == table[2][2][0] :
        return table[0][2][0]
    elif table[1][1][0] == table[2][2][0] == table[0][0][0] :
        return table[1][1][0]
    elif table[1][1][0] == table[2][0][0] == table[0][2][0] :
        return table[1][1][0]

###########################################################################################################################
round = 0
@client.on_callback_query()
def handle_callback_query(bot, query) :
    global round, Ps, table

    if not query.from_user.username in Ps :
       Ps += [query.from_user.username]

    if query.data.startswith('block') :

        i = int(query.data[5])
        j = int(query.data[6])


        if round % 2 == 0 and query.from_user.username == Ps[1] :
            if table[i][j][0] == 'πΎοΈοΈ' or table[i][j][0] == 'β':
                bot.answer_callback_query(query.id, '''π Please choose another block
    This one is chosen !!!''', show_alert=True)
            else :
                table[i][j] = ('β', query.data)
                round += 1
                bot.edit_inline_text(query.inline_message_id, f'''βπΎοΈ Game
                            
β­ Turn: @{Ps[0]} as πΎοΈ''', reply_markup=IKM2D(table))

        elif round % 2 != 0 and query.from_user.username == Ps[0] :
            if table[i][j][0] == 'πΎοΈοΈ' or table[i][j][0] == 'β' :
                bot.answer_callback_query(query.id, '''π Please choose another block
    This one is chosen !!!''' , show_alert=True)
            else :
                table[i][j] = ('πΎοΈοΈ', query.data)
                round += 1
                bot.edit_inline_text(query.inline_message_id, f'''βπΎοΈ Game

β­ Turn: @{Ps[1]} as β''', reply_markup=IKM2D(table))

        elif round % 2 != 0 and query.from_user.username == Ps[1] :
            bot.answer_callback_query(query.id, 'π It`s not your turn !!! ', show_alert=True)

        elif round % 2 == 0 and query.from_user.username == Ps[0] :
            bot.answer_callback_query(query.id, 'π It`s not your turn !!! ', show_alert=True)

        if check_winner(table) :
            bot.edit_inline_text(query.inline_message_id , f'''π₯³ @{query.from_user.username} Wins as {check_winner(table)}
            
Play Again :)!!! πͺ''', reply_markup= IKM([[('ββ­οΈ Play Again β­οΈβ','start0')]]))
            bot.answer_callback_query(query.id, 'π₯³π₯³π₯³ You won !!!!!', show_alert=True)
            Ps = []
            round = 0
            table = [[('1', 'block00'), ('2', 'block01'), ('3', 'block02')], [('4', 'block10'), ('5', 'block11'), ('6', 'block12')], [('7', 'block20'), ('8', 'block21'), ('9', 'block22')]]

        elif round == 9 :
            bot.edit_inline_text(query.inline_message_id , 'π² Tie! Play Again :)', reply_markup= IKM([[('ββ­οΈ Play Again β­οΈβ','start0')]]))
            Ps = []
            round = 0
            table = [[('1', 'block00'), ('2', 'block01'), ('3', 'block02')], [('4', 'block10'), ('5', 'block11'), ('6', 'block12')], [('7', 'block20'), ('8', 'block21'), ('9', 'block22')]]

    elif query.data == 'start0' and query.from_user.username == Ps[0]:
        bot.edit_inline_text(query.inline_message_id,'π₯± Waiting for second player ...', reply_markup=IKM([[('ββ­οΈ Tap to Play β­οΈβ', 'start1')]]))
        bot.answer_callback_query(query.id, '''π₯± Wait for another player ...
You are the first player !!''', show_alert=True)

    elif query.data == 'start1' and query.from_user.username == Ps[0] :
        bot.answer_callback_query(query.id, 'π₯± Wait for another player ...', show_alert=True)

    elif query.data == 'start1' and query.from_user.username == Ps[1]:
        bot.answer_callback_query(query.id, '''π Accepted ...
You are the second player !!''', show_alert=True)
        bot.edit_inline_text(query.inline_message_id, f'''βπΎοΈ Game
        
π Rule: Second player always starts the match as β !!

β­ Turn:  @{query.from_user.username} as β''', reply_markup=IKM2D(table))
    elif query.data == 'start0' and query.from_user.username == Ps[1]:
        bot.edit_inline_text(query.inline_message_id, 'π₯± Waiting for second player ...', reply_markup=IKM([[('ββ­οΈ Tap to Play β­οΈβ', 'start1')]]))
        bot.answer_callback_query(query.id, '''π₯± Wait for another player ...
You are the first player !!''', show_alert=True)


##############################################################################################################################################################
@client.on_inline_query()
def handle_inline_query(bot, query) :
    results = [InlineQueryResultArticle('π Credit π', InputTextMessageContent('''π₯  Written & Developed by  π₯
            
            π Yousof Asadi π :
               @Yousof_Asadi''')), InlineQueryResultArticle('π₯ Play with Friends π²', InputTextMessageContent('''π  Hi

π  Thanks for playing with my βπΎοΈ Bot !

π Rule: Second player always starts the math as β !!'''), reply_markup= IKM([[('ββ­οΈ Tap to Play β­οΈβ','start0')]]))]
    bot.answer_inline_query(query.id, results)

################################################################################################################################

client.run()