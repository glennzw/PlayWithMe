#!/usr/bin/python
# -*- coding: utf-8 -*-
# See who you can play games with
import steamapi
import collections
from prettytable import PrettyTable

def listFriends(steamkey,rootuser):
        """
        Return list of friends for rootuser
        """
        steamapi.core.APIConnection(api_key=steamkey)
        me = steamapi.user.SteamUser(userurl=rootuser)
        return map(str, me.friends)

def playWithMe(steamkey,rootuser,friendsfilter=None,minWhoHave=2):
        """
        Create a table of who has what games. 'rootuser' will be the
        steam user whose friends are retrieved (likely your steam name).
        All friends are checked unless a list of friends is supplied via
        friendsfilter.
        """

        steamapi.core.APIConnection(api_key=steamkey)
        me = steamapi.user.SteamUser(userurl=rootuser)
        friends = me.friends
        almal = friends + [me]
        games = {}

        for name in almal:
          if (friendsfilter and name.name in friendsfilter) or friendsfilter is None:
            for game in name.games:
              tmp = games.setdefault(game.name,[])
              games[game.name].append(name.name)

        _ = sorted(games.items(), key=lambda x: len(x[1]), reverse=True)
        sgames = collections.OrderedDict(sorted(games.items(), key=lambda x: len(x[1]), reverse=True))

        numGamers = len(sgames.items()[0][1])
        tbl = PrettyTable()
        tbl.field_names = ["Game"] + ["Gamer_" + s for s in map(str, range(1,numGamers+1))]

        for game, names in sgames.iteritems():
          if len(names) > minWhoHave :
            #print "%s|%s" %(game, "|".join(names))
            row = [game] + names + [''] * (numGamers - len(names))
            tbl.add_row(row)
        print tbl

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print "Usage:\n\t%s <steamAPIkey> [username] [friendsFilterList] [minimumWhoHaveGame]" % __file__
        print "\t%s <steamAPIkey> [username] -listfriends" % __file__
        exit(-1)
    key, rootuser = sys.argv[1], sys.argv[2]
    friends, minh = None, 2
    if len(sys.argv) > 3:
        if sys.argv[3] == "-listfriends":
            print ",".join(listFriends(key, rootuser))
            exit(0)
        friends = sys.argv[3].split(",")
    if len(sys.argv) > 4:
        minh = int(sys.argv[4])
    playWithMe(key, rootuser, friends, minh)
