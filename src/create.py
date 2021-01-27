import src.folder


class Create(src.folder.FileFunction):
    def createTL(self, message, commande):
        """
        creat TierList

        Paramters :
            Create : self
            discord.Message : message
            list : commande

        Return :
            str : reply

        """
        data = self.load("tierList/{}.json".format(message.guild.id))
        if commande[1] in data:
            reponse = ("{}\n"
                       "Tierlist '{}'"
                       " already exist").format(message.author.mention,
                                                commande[1])
            return reponse
        data[commande[1]] = dict()
        data["perm"][commande[1]] = dict()
        data["perm"][commande[1]][str(message.author.id)] = True
        self.save("tierList/{}.json".format(message.guild.id), data)
        reponse = "{}\nTier list '{}'".format(message.author.mention,
                                              commande[1])
        reponse += " was create"
        return reponse

    def createCat(self, message, commande):
        """
        creat Creat category in Tierlist

        Paramters :
            Create : self
            discord.Message : message
            list : commande

        Return :
            str : reply

        """
        data = self.load("tierList/{}.json".format(message.guild.id))
        if commande[2] not in data:
            return ("{}\nTierlist '{}'"
                    " doesn't exist").format(message.author.mention,
                                             commande[2])

        if ((str(message.author.id) not in data["perm"][commande[2]] or
             data["perm"][commande[2]][str(message.author.id)] is False)
                and message.author.guild_permissions.administrator is False):
            return ("{}\n"
                    "You can't modify this Tierlist").format(
                        message.author.mention)

        reponse = "{}\nCategory\n".format(message.author.mention)
        for i in range(3, len(commande)):
            if commande[i] in data[commande[2]]:
                reponse += "{} -> already exist\n".format(commande[i])
            else:
                data[commande[2]][commande[i]] = []
                reponse += "{}\n".format(commande[i])

        self.save("tierList/{}.json".format(message.guild.id), data)
        reponse += ("was created in the"
                    " tier list -> '{}'").format(commande[2])
        return reponse

    def creatName(self, message, commande):
        """
        creat name in category in Tierlist

        Paramters :
            Create : self
            discord.Message : message
            list : commande

        Return :
            str : reply

        """
        data = self.load("tierList/{}.json".format(message.guild.id))
        if commande[2] not in data:
            return ("{}\nTierlist '{}'"
                    " doesn't exist").format(message.author.mention,
                                             commande[1])
        if ((str(message.author.id) not in data["perm"][commande[2]] or
             data["perm"][commande[2]][str(message.author.id)] is False)
                and message.author.guild_permissions.administrator is False):
            return ("{}\n"
                    "You can't modify this Tierlist").format(
                        message.author.mention)

        if commande[3] not in data[commande[2]]:
            return ("{}\nCategory "
                    "'{}' doesn't exist").format(message.author.mention,
                                                 commande[2])
        reponse = "{} :\n".format(message.author.mention)
        for i in range(4, len(commande)):
            if commande[i] in data[commande[2]][commande[3]]:
                reponse += "{} -> already exist\n".format(commande[i])
            else:
                data[commande[2]][commande[3]].append(commande[i].lower())
                reponse += "{}\n".format(commande[i])
        self.save("tierList/{}.json".format(message.guild.id), data)

        reponse += ("was created in the tier list -> '{}'\n "
                    "in category -> '{}'\n").format(commande[2],
                                                    commande[3])
        return reponse
