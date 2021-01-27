import src.folder


class Delet(src.folder.FileFunction):
    def delTierlsite(self, message, commande):
        """
        delet tierlist with command tl?delet tierlist "tierlist"

        Paramters :
            Delet : self
            discord.Message : message
            list: commande

        Return :
            str : message to send
        self :
        """
        data = self.load("tierList/{}.json".format(message.guild.id))
        reponse = "{}\n".format(message.author.mention)
        for i in range(2, len(commande)):
            if commande[i] in data:
                if ((str(message.author.id) not in data["perm"][commande[2]] or
                     data["perm"][commande[2]][str(message.author.id)] is
                     False) and message.author.guild_permissions.administrator
                        is False):
                    reponse += ("You Can't "
                                "delete '{}' tierlist\n").format(commande[i])
                else:
                    reponse += "'{}' was delete\n".format(commande[i])
                    del data[commande[i]]
                    del data["perm"][commande[i]]
            else:
                reponse += "'{}' doesn't exist\n".format(commande[i])
        self.save("tierList/{}.json".format(message.guild.id), data)
        return reponse

    def delCat(self, message, commande):
        """
        delet category with command tl?delet cat "tierlist" "category"

        Paramters :
            Delet : self
            discord.Message : message
            list: commande

        Return :
            str : message to send
        self :
        """
        data = self.load("tierList/{}.json".format(message.guild.id))
        if commande[2] not in data:
            return "{}\n'{}' doesn't exist".format(message.author.mention,
                                                   commande[1])
        if ((str(message.author.id) not in data["perm"][commande[2]] or
             data["perm"][commande[2]][str(message.author.id)] is False)
                and message.author.guild_permissions.administrator is False):
            return ("{}\n"
                    "You can't modify this Tierlist").format(
                        message.author.mention)
        reponse = "{}\n".format(message.author.mention)
        for i in range(3, len(commande)):
            if commande[i] in data[commande[2]]:
                reponse += "{}\n".format(commande[i])
                del data[commande[2]][commande[i]]
            else:
                reponse += "{} doesn't exist\n".format(commande[i])
        reponse += "was delete"
        self.save("tierList/{}.json".format(message.guild.id), data)
        return reponse

    def delnom(self, message, commande):
        """
        delet name with command tl?delet name "tierlist" "category" "name"

        Paramters :
            Delet : self
            discord.Message : message
            list: commande

        Return :
            str : message to send
        self :
        """
        data = self.load("tierList/{}.json".format(message.guild.id))
        if commande[2] not in data:
            return "{}\n'{}' doesn't exist".format(message.author.mention,
                                                   commande[1])
        if ((str(message.author.id) not in data["perm"][commande[2]] or
             data["perm"][commande[2]][str(message.author.id)] is False)
                and message.author.guild_permissions.administrator is False):
            return ("{}\n"
                    "You can't modify this Tierlist").format(
                        message.author.mention)

        if commande[3] not in data[commande[2]]:
            return "{}\n'{}' doesn't exist".format(message.author.mention,
                                                   commande[1])
        reponse = "{}\n".format(message.author.mention)
        deletepos = []
        for i in range(4, len(commande)):
            if (int(commande[i]) >= 0 and
                    int(commande[i]) < len(data[commande[2]][commande[3]])):
                deletepos.append(int(commande[i]))
            else:
                reponse += "{} -> doesn't exist\n".format(commande[i])

        deletepos = sorted(deletepos)
        for i in range(len(deletepos) - 1, -1, -1):
            del data[commande[2]][commande[3]][deletepos[i]]
            reponse += "{} -> was deleted\n".format(deletepos[i])
        self.save("tierList/{}.json".format(message.guild.id), data)
        return reponse
