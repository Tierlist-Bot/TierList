from discord import Embed


class Help:
    def __init__(self):
        # Basic Help
        self.basicHelp = Embed(title="TierList Bot's Command",
                               description=("With this bot you" +
                                            " can classify objects " +
                                            "in categories that are" +
                                            " more commonly called " +
                                            "Tier Lists."))
        self.basicHelp.add_field(name="```help <command>``` :",
                                 value="""There are 4 commandes :
```list show create delete perm prefix```""")

        # show help
        self.showHelp = Embed(title=":mag_right:show:mag:",
                              description=("You can show tierlist " +
                                           "with an image"))
        self.showHelp.add_field(name="```show tierlist \"tl\"```",
                                value="Show tl tierlist with an image")
        self.showHelp.add_field(name="```show cat \"tl\" \"cat\"```",
                                value=("show \"cat\" in \"tl\" tierlist" +
                                       " with an image"))

        # list help
        self.listHelp = Embed(title=":mag_right:list:mag:",
                              description=("You can list your tierlist " +
                                           "without formatting"))
        self.listHelp.add_field(name="```list```",
                                value="List every tierlist in your guild")
        self.listHelp.add_field(name="```list \"tl\"```",
                                value=("lists the elements of" +
                                       " a \"tl\" without formatting"))
        self.listHelp.add_field(name=("```list \"tl\" cat \"cat\"```"),
                                value=("list the elements of the " +
                                       "\"cat\" as parameters " +
                                       "in the \"tl\" " +
                                       " also as parameter"))
        self.listHelp.add_field(name=("```list \"tl \"" +
                                      "name \"name\"```"),
                                value=("show the category of " +
                                       "the \"name\" as a" +
                                       "parameter in the" +
                                       " \"tl\" as a parameter"))

        # create help
        self.createHelp = Embed(title=":hammer_pick:Create:hammer_pick:",
                                description=("You can create your tierlist"))
        self.createHelp.add_field(name=("```create \"tl\"```"),
                                  value=("create an empty tierlsit with the" +
                                         " \"tl\" parameter name"))
        self.createHelp.add_field(name=("```create cat \"tl\" " +
                                        "\"cat 1\" \"cat2\" ...```"),
                                  value=("Create an empty category in " +
                                         "the \"tl\" tierlist"))
        self.createHelp.add_field(name=("```create name \"tl\" " +
                                        "\"cat\" \"name1\" \"name 2\" ...```"),
                                  value=("create \"name1\" \"name2\" ... in" +
                                         " the category \"cat\" in the" +
                                         " \"tl\" tierlist"))

        # create help
        self.deleteHelp = Embed(title=":x:Delete:x:",
                                description=("You can delete your tierlist"))
        self.deleteHelp.add_field(name=("```delete tierlist " +
                                        "\"tl1\" \"tl2\"```"),
                                  value=("Delete \"tl1\" \"tl2\" tierlist"))
        self.deleteHelp.add_field(name=("```delete cat \"tl\" " +
                                        "\"cat 1\" \"cat2\" ...```"),
                                  value=("Delete category in " +
                                         "the \"tl\" tierlist"))
        self.deleteHelp.add_field(name=("```delete name \"tl\" \"cat\"" +
                                        " \"pose 1\" \"pose 2\" ...```"),
                                  value=("Delete the objects in position " +
                                         "\"pose 1\" \"pose 2\" ... in" +
                                         " the category \"cat\" in the" +
                                         " \"tl\" tierlist"))

        # create help
        self.permHelp = Embed(title=":lock:Perm:unlock:",
                              description=("You can change " +
                                           "tierlist permition"))
        self.permHelp.add_field(name=("```perm add \"tl\" " +
                                      "\"@user 1\" \"@user 2\"```"),
                                value=("Add \"@user 1\" \"@user 2\" ... " +
                                       "in modertor list of \"tl\" tierlist"))
        self.permHelp.add_field(name=("```perm delete \"tl\" " +
                                      "\"@user 1\" \"@user 2\" ...```"),
                                value=("Delete \"@user 1\" \"@user 2\" ... " +
                                       "in modertor list of \"tl\" tierlist"))

        # prefix help
        self.prefixHelp = Embed(title="```prefix \"prefix\"```",
                                description=("You can change your " +
                                             "prefix for your server"))

    async def helpTraitment(self, message, prefix):
        """
        send help message

        Parameters:
            Help : self
            discrod.Message : message
            str : prefix

        Retrun:
            void
        """
        if message.content == prefix + "help":
            await message.channel.send(embed=self.basicHelp)
        elif message.content == prefix + "help list":
            await message.channel.send(embed=self.listHelp)
        elif message.content == prefix + "help create":
            await message.channel.send(embed=self.createHelp)
        elif message.content == prefix + "help delete":
            await message.channel.send(embed=self.deleteHelp)
        elif message.content == prefix + "help perm":
            await message.channel.send(embed=self.permHelp)
        elif message.content == prefix + "help prefix":
            await message.channel.send(embed=self.prefixHelp)
        elif message.content == prefix + "help show":
            await message.channel.send(embed=self.showHelp)
        return
