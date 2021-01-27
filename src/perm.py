import src.folder


class Permition(src.folder.FileFunction):
    def addProprio(self, message):
        """
        This function add owner of tierlist

        Permeters:
            Permition : self
            discord.message : message

        return
            str : reponse
        """
        commande = message.content.split(" ")
        data = self.load("tierList/" + str(message.guild.id) + ".json")
        reponse = "{}\n".format(message.author.mention)
        if commande[2] not in data["perm"]:
            return (reponse +
                    "'{}' doesn't exist").format(commande[2])
        elif len(message.mentions) == 0:
            return (reponse +
                    "you must ping members")
        for personne in message.mentions:
            if (str(personne.id) not in data["perm"][commande[2]] or
                    data["perm"][commande[2]][str(personne.id)] is False):
                data["perm"][commande[2]][str(personne.id)] = True
                reponse += ("-> '{}'  was added as "
                            "admin in this tierlist\n").format(
                    personne.name)
            else:
                reponse += ("-> '{}' was already "
                            "an admin of the tierlist\n").format(personne.name)

        self.save("tierList/" + str(message.guild.id) + ".json", data)
        return reponse

    def removeProprio(self, message):
        """
        This function delete owner of tierlist

        Permeters:
            Permition : self
            discord.message : message

        return
            str : reponse
        """
        commande = message.content.split(" ")
        data = self.load("tierList/" + str(message.guild.id) + ".json")
        reponse = "{}\n".format(message.author.mention)
        if commande[2] not in data["perm"]:
            return (reponse +
                    "'{}' doesn't exist").format(commande[2])
        for personne in message.mentions:
            if (str(personne.id) in data["perm"][commande[2]] and
                    data["perm"][commande[2]][str(personne.id)] is True):
                data["perm"][commande[2]][str(personne.id)] = False
                reponse += "-> '{}' was deleted in this tierlist\n".format(
                    personne.name)
            else:
                reponse += "-> '{}' was not an admin of the tierlist\n".format(
                    personne.name)
        self.save("tierList/" + str(message.guild.id) + ".json", data)
        return reponse
