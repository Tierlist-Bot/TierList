import src.list
import src.create
import src.delet
import src.perm


class Commande(src.list.List,
               src.create.Create,
               src.delet.Delet,
               src.perm.Permition):
    def traitment(self, message, prefix):
        """
        order processing

        Parameters:
            Commande : self
            discord.Message : message

        Return:
            str : reponse
        """
        commande = message.content.split(' ')
        reponse = "{}\nsend {}help for doc".format(message.author.mention,
                                                   prefix)
        if message.content.startswith("{}list".format(prefix)):
            if len(commande) == 1:
                return self.listTierlist(message.author.mention,
                                         message.guild.id)
            elif len(commande) == 2:
                return self.repWithTierList(commande,
                                            message.author.mention,
                                            message.guild.id)
            elif len(commande) == 4:
                if commande[2] == "cat":
                    return self.repWitheCat(commande,
                                            message.author.mention,
                                            message.guild.id)
                elif commande[2] == "name":
                    return self.repWitheName(commande,
                                             message.author.mention,
                                             message.guild.id)

        elif message.content.startswith("{}create".format(prefix)):
            if len(commande) == 2:
                return self.createTL(message, commande)

            elif len(commande) > 3:
                if commande[1] == "cat":
                    return self.createCat(message, commande)
                elif commande[1] == "name":
                    if len(commande) > 4:
                        return self.creatName(message, commande)

        elif message.content.startswith("{}delete".format(prefix)):
            if message.content.startswith("{}delete tierlist".format(prefix)):
                return self.delTierlsite(message, commande)

            elif message.content.startswith("{}delete cat".format(prefix)):
                return self.delCat(message, commande)

            elif message.content.startswith("{}delete name".format(prefix)):
                return self.delnom(message, commande)

        elif message.content.startswith("{}perm".format(prefix)):
            if message.content.startswith("{}perm add".format(prefix)):
                return self.addProprio(message)

            elif message.content.startswith("{}perm delete".format(prefix)):
                return self.removeProprio(message)

        elif message.content.startswith("{}prefix".format(prefix)):
            if len(commande) >= 2:
                data = self.load("src/prefix.json")
                data[str(message.guild.id)] = commande[1]
                self.save("src/prefix.json", data)
                return "{}\nThe prefix has been changed with '{}'".format(
                    message.author.mention,
                    commande[1])

        return reponse
