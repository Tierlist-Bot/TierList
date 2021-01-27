#!/usr/bin/python3.9
import src.folder


class List(src.folder.FileFunction):
    def listTierlist(self, mention, guildID):
        """
        return list of tierlist with commande :
        tl?list

        Paramters:
            MyCommand : slef
            str : mention
            int : guildID

        Return :
            str : message to send
        """
        data = self.load("tierList/{}.json".format(guildID))
        reponse = "{}\n".format(mention)
        if len(data) == 0:
            return reponse + "There is no tier list for the moment"
        for tierlist in data:
            if tierlist != "perm":
                reponse += "-> {}\n".format(tierlist)
        return reponse

    def repWithTierList(self, commande, mention, guildID):
        """
        Show a tier list with the command :
        tl?"tierlist"

        Paramters :
            MyCommand : self
            discord.Message : message
            int : guildID

        Return :
            str : message to send
        """
        data = self.load("tierList/{}.json".format(guildID))
        if commande[1] not in data:
            return "{}\n This category doesn't exist".format(mention)
        reponse = "{}\n__**{} :**__\n".format(mention,
                                              commande[1])

        for cat in data[commande[1]]:
            reponse += "\t__" + str(cat) + " :__\n"
            for name in range(len(data[commande[1]][cat])):
                reponse += str(name) + " -> " + \
                    data[commande[1]][cat][name] + "\n"
            reponse += "\n"

        return reponse

    def repWitheCat(self, commande, mention, guildID):
        """
        Show a category in tierlist with the command :
        tl?"tierlist" cat "cat"

        Paramters :
            MyCommand : self
            list : commande
            str : mention
            int : guildID

        Return :
            str : message to send
        """
        data = self.load("tierList/{}.json".format(guildID))
        reponse = "{}\n__{}__ :\n".format(mention,
                                          commande[2])
        if commande[1] not in data:
            return "{}\n{} doesn't exist".format(mention,
                                                 commande[1])
        if commande[3] not in data[commande[1]]:
            return "{}\n{} doesn't exist in '{}' list".format(mention,
                                                              commande[3],
                                                              commande[1])
        for name in range(len(data[commande[1]][commande[3]])):
            reponse += str(name) + " -> " + \
                str(data[commande[1]][commande[3]][name]) + "\n"
        return reponse

    def repWitheName(self, commande, mention, guildID):
        """
        Show a category in tierlist with the command :
        tl?"tierlist" name "name"

        Paramters :
            MyCommand : self
            list : commande
            str : mention
            int : guildID

        Return :
            str : message to send
        """
        data = self.load("tierList/{}.json".format(guildID))
        if commande[1] not in data:
            return "{}\nCategory doesn't exist".format(mention)
        for cat in data[commande[1]]:
            if commande[3].lower() in data[commande[1]][cat]:
                return "{}\n{} -> {}".format(mention,
                                             commande[3],
                                             cat)
        return "{}\n'{}' isn't in the tierlist".format(mention,
                                                       commande[3])
