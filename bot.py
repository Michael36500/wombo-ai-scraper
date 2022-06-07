# import os
# if os.path.isfile("config\mazes_org_uuid_and_cookie.json"):
#     os.remove("config\mazes_org_uuid_and_cookie.json")

# Import instabot library

# Create a variable bot.
# Login
from instabot import Bot
import random as rn
import hastags
import cv2
# hstgs = ["#braintrain "], ["#maze "], ["#mazes "], ["#labyrinth "], ["#labyrinths "], ["#brain "], ["#puzzle "], ["#play "], ["#escape "], ["#think "], ["#puzzling "], ["#puzzlelove "], ["#creative "], ["#fun "], ["#fun "], ["#games "], ["#gamesforkids "], ["#kids "], ["#mind "], ["#puzzleart"], ["#pattern "], ["#font "], ["#number "], ["#patterns "], ["#patterndesign "], ["#numbers "], ["#elfontheshelf "], ["#numberone "], ["#fontana "], ["#number1 "], ["#fonts "], ["#handmadefont "], ["#crochetpattern "], ["#ageisjustanumber "], ["#mathias777_numbers "], ["#surfacepatterndesign "], ["#surfacepattern "], ["#electricblue "], ["#rectangle "], ["#numbercake "], ["#fontanaditrevi "], ["#patternmaking "], ["#fontainebleau "], ["#fontaine "], ["#patterndesigner "], ["#patternlove "], ["#knittingpattern "], ["#numberfive "], ["#printandpattern "], ["#strengthinnumbers "], ["#patternart "], ["#fontdesign "], ["#fonte "], ["#numbernine "], ["#babynumber2 "], ["#sewingpattern "], ["#patternobserver "], ["#angelnumbers "], ["#numberplate "], ["#number2 "], ["#patternmaker "], ["#backnumber "], ["#numberonefan "], ["#patternplay "], ["#number3 "], ["#number5 "], ["#numberplates "], ["#mynumberone "], ["#fontainebleaumiami "], ["#amigurumipattern "], ["#patterncutting "], ["#sewingpatterns "], ["#numbercakes "], ["#patterndrafting "], ["#number4 "], ["#freepattern "], ["#floralpattern "], ["#fontstyle "], ["#elfontheshelfideas "], ["#patternbank "], ["#surfacepatterndesigner "], ["#patternsinnature "], ["#babynumber3 "], ["#paintbynumbers "], ["#repeatpattern "], ["#amigurumipatterns "], ["#patternator "], ["#number1fan "], ["#patternmixing "], ["#patternshirt "], ["#number7 "], ["#fontandroid "], ["#secretnumber "], ["#fontanna "], ["#bloemfontein "], ["#embroiderypattern "], ["#patterned "], ["#numbertwo "], ["#patternlover "], ["#fontstudio "], ["#patternoftheday "], ["#patterndesigners "], ["#mynumber1 "], ["#number15 "], ["#numberof1 "], ["#numbersdontlie "], ["#fontcandy "], ["#fonttattoo "], ["#geometricpattern "], ["#vipnumbers "], ["#numberofthebeast "], ["#number11 "], ["#numberof2 "], ["#patternwork "], ["#numbered "], ["#numbersix "], ["#patternaddict "], ["#numberfiveedit "], ["#numberlikh "], ["#fontsamsung "], ["#number_9th "], ["#numberx9th "], ["#patternmaster "], ["#acnhpatterns "], ["#patternartist "], ["#fontenova "], ["#number1dad "], ["#jualfont "], ["#number12 "], ["#patternedpaper "], ["#patterndesigns "], ["#fontpack "], ["#surfacepatterns "], ["#patternonpattern "], ["#numberseven "], ["#fontanellato "], ["#paintingbynumbers "], ["#simplicitypatterns "], ["#clairefontaine "], ["#fontaneria "], ["#blueelectric "], ["#patterntattoo "], ["#fontmurah "], ["#patterntester "], ["#fontain "], ["#numberballoons "], ["#numberofn "], ["#patterninspiration "], ["#fontedavida "], ["#numberthree "], ["#number_one "], ["#fontainecards "], ["#numberfour "], ["#patternlicious "], ["#fontromeu "], ["#numberonedad "], ["#patternaday "], ["#patternedtiles "], ["#patternseverywhere "], ["#patternlife "], ["#patternity "], ["#fontina "], ["#patternillustration "], ["#fontibon "], ["#numbersugar "], ["#fontananails "], ["#fontlucu "], ["#fonthill "], ["#patternplanetme "], ["#fontanacalifornia "]
# hstgs = hastags.chs_hst()



# def chs_hst():
#     hst = []
#     for _ in range (30):
#         hst.append(hstgs[rn.randint(0,169)])
#     print(hst)
#     hst = str(hst)

#     hst = hst.replace("[", "")
#     hst = hst.replace("]", "")
#     hst = hst.replace("'", "")
#     hst = hst.replace(",", "")

#     return hst


def login():
    global bot
    bot = Bot()
    bot.login(username="_steampunk_art_", password="B0TB0T")
def upload(path):
    global bot

    img = cv2.imread(path)
    img = img[0 : 957, 0 : 957]        #crop malých, mnou zmenšeny
    # l = len(path)
    # cv2.imwrite(str(path[:l - 4]) + ".jpeg", img)
    # img = cv2.resize(img, (520, 520), interpolation = cv2.INTER_NEAREST)
    cv2.imwrite(path, img)
    # print(hastags.chs_hst())
    bot.upload_photo(path, caption="What a cool picture of STEAMPUNK world! \n\n\n {}".format(hastags.chs_hst()))
    # bot.upload_photo(path, caption="What a cool picture of STEAMPUNK world! \n\n\n #worldseries #worldcup2018 #dogsofinstaworld #disneyworld #catsofworld#steampunklamps #steampunkpendant #steampunklighting #steampunklamps #steampunkaccessories #steampunknai #steampunkdoll #steampunk #steampunkfashion #steampunkgirls #steampunkartwork #steampunks #steampunkcouture #steampunklove #steampunkitalia#worldofwalker #worldskillsrussia #worldsstrongestman #towereiffel #buildingourhome #worldstarmusic #buildingblackwealth #windowtreatment #windows7 #windowwashing#bengalcatworld #cavapooworld #worldrecord #windowtreatments #worldrecord #catsworld #worldwidedance #whoruntheworld #beardedvillainsworldwide #worldstreetfeature")
    # bot.upload_photo(str(path[:l - 4]) + ".jpeg", caption="What a cool picture of STEAMPUNK world! \n\n\n {}".format(hastags.chs_hst()))



