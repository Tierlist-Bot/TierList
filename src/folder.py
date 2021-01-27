import json
import os


class FileFunction():
    def load(self, name):
        """
        load json file

        Parameters :
            FileFunction : self
            discord.Guild.id : id of tierlist's guild

        Return :
            dict : data in json file
        """
        try:
            f = open(name, "r")
            person_dict = json.load(f)
            return person_dict
        except FileNotFoundError:
            self.createfolder(name)
            return {"perm": dict()}

    def createfolder(self, name):
        """
        create json file with guildid

        Paramters :
            FileFunction : self
            discord.guild : guild

        Return :
            None
        """
        data = {"perm": dict()}
        with open(name, "w") as output:
            json.dump(data, output)

    def deletFolder(slef, name):
        """
        remove json file

        Paramters :
            FileFunction : self
            discord.guild : guild

        Return :
            None
        """
        os.remove(name)

    def save(self, name, data):
        """
        save data in json file

        Parameters :
            FileFunction : self
            int : guildID
            dic : data

        Retrun :
            None
        """
        with open(name, "w") as output:
            json.dump(data, output)
