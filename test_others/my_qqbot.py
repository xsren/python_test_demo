# encoding: utf-8
"""
@author: xsren 
@contact: bestrenxs@gmail.com
@site: xsren.me

@version: 1.0
@license: Apache Licence
@file: my_qqbot.py
@time: 2017/5/29 下午4:54

"""

from qqbot import QQBotSlot as qqbotslot, RunBot

ts = [u'NB田',u'田NB',u'田BN']

@qqbotslot
def onQQMessage(bot, contact, member, content):
    print contact, content, member
    # if content == '-hello':
    #     bot.SendTo(contact, '你好，我是QQ机器人')
    # elif content == '-stop':
    #     bot.SendTo(contact, 'QQ机器人已关闭')
    #     bot.Stop()
    if u"矿大703" in contact.name.decode('utf8'):
        if u"见龙在田" in member.nick.decode('utf8'):
            bot.SendTo(contact, content)
            for t in ts:
                bot.SendTo(contact, t)


if __name__ == '__main__':
    RunBot(qq="1028730267")
