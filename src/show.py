from PIL import Image, ImageDraw
from discord import File
import urllib.request
import src.folder


class Show(src.folder.FileFunction):
    def catDraw(self, data, key, color):
        taille = len(data[key])
        x = 880
        y = 80 * (taille // 10 + 1)
        out = Image.new("RGB", (x, y))

        cat = Image.new("RGB", (80, y))
        ImageDraw.floodfill(cat, (0, 0), color)
        catD = ImageDraw.Draw(cat)
        textFormat = ""
        for j in range(0, len(key)):
            if key[j] == "-":
                textFormat += " "
            else:
                textFormat += key[j]
            if (j + 1) % 11 == 0:
                textFormat += "\n"
        catD.multiline_text((5, 5), textFormat, fill=(0, 0, 0), align="center")
        out.paste(cat, (0, 0))

        for i in range(len(data[key])):
            try:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) " +
                    "AppleWebKit/537.36 (KHTML, like Gecko) " +
                    "Chrome/41.0.2228.0 Safari/537.3"}
                fd = urllib.request.Request(
                    url=data[key][i], headers=headers)
                image_file = urllib.request.urlopen(fd)
                im = Image.open(image_file)
                im.thumbnail((80, 80))
            except Exception:
                textFormat = ""
                for j in range(0, len(data[key][i])):
                    textFormat += (data[key][i][j])
                    if (j + 1) % 11 == 0:
                        textFormat += "\n"
                im = Image.new("RGB", (80, 80))
                d = ImageDraw.Draw(im)
                d.multiline_text((5, 5), textFormat)

            out.paste(im, ((i * 80) % 800 + 80, 80 * (i // 10)))
        return out

    def tlDraw(self, dic):
        x = 880
        y = 0
        for key in dic:
            taille = len(dic[key])
            y += 80 * (taille // 10 + 1)
        out = Image.new("RGB", (x, y))
        y = 0
        color = len(dic)
        for key in dic:
            img = self.catDraw(dic,
                               key,
                               (int(255 * (color / len(dic))),
                                int(255 * (((len(dic) + 1) -
                                            color + 2) / (len(dic)))),
                                127))
            taille = len(dic[key])
            out.paste(img, (0, y))
            y += 80 * (taille // 10 + 1)
            color -= 1
        return out

    async def showTrait(self, message, prefix):
        commande = message.content.split(" ")
        data = self.load("tierList/{}.json".format(message.guild.id))
        if message.content.startswith(prefix + "show tierlist"):
            tierlist = self.tlDraw(data[commande[2]])
            tierlist.save("tierlistImg/" + str(message.guild.id) + ".png")
            file = File("tierlistImg/" + str(message.guild.id) + ".png")
            await message.channel.send("{}\n".format(message.author.mention),
                                       file=file)
            self.deletFolder("tierlistImg/" + str(message.guild.id) + ".png")
            return
        elif message.content.startswith(prefix + "show cat"):
            color = len(data[commande[2]])
            finalcolor = (0, 0, 0)
            for key in data[commande[2]]:
                colorKey = (int(255 * (color / len(data[commande[2]]))),
                            int(255 *
                                (((len(data[commande[2]]) + 1) - color + 2) /
                                 (len(data[commande[2]])))),
                            127)
                if key == commande[3]:
                    finalcolor = colorKey
            self.catDraw(data[commande[2]], commande[3], finalcolor).save(
                "tierlistImg/" + str(message.guild.id) + ".png")
            file = File("tierlistImg/" + str(message.guild.id) + ".png")
            await message.channel.send("{}\n".format(message.author.mention),
                                       file=file)
            self.deletFolder("tierlistImg/" + str(message.guild.id) + ".png")
            return
        await message.channel.send(
            "{}\nsend {}help for doc".format(message.author.mention,
                                             prefix))
