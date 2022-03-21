from .. import loader, utils

@loader.tds
class RPMod(loader.Module):
    """Модуль RPMod"""
    strings = {'name': 'RPMod'}

    async def client_ready(self, client, db):
        self.db = db
        self.db.set("RPMod", "status", True)

    async def rpmodcmd(self, message):
        """Напиши: .rpmod щоб включити/виключити RP режим."""
        status = self.db.get("RPMod", "status")
        if status is not False:
            self.db.set("RPMod", "status", False)
            await message.edit("<b>RP Режим <code>вимкнений</code></b>")
        else:
            self.db.set("RPMod", "status", True)
            await message.edit("<b>RP Режим <code>ввімкнений</code></b>")

    async def rplistcmd(self, message):
        """Напиши: .rplist щоб подивитися список RP команд."""
        await message.edit("<b>• чмок\n• чпок\n• кусь\n• обняти\n• шльоп\n• вбити\n• виїбати\n• звязати\n• вдарити\n• вїбати\n• відсосати\n• відлизати\n• задушити\n• вкрасти"
                           "\n• погладити\n• притягнути\n• згвалтували\n• відшльопати\n• наїбати\n• поцілувати\n• накурити\n• набухати\n• засосати\n• утопити\n• розстріляти\n• прижати\n• понюхати\n• віддатись\n• покормити\n• каструвати\n• пихнути\n• побажати солодких снів\n• лизнути\n• послати нахуй\n• щіпнути\n• дати чапалаха\n• полюбити\n• признатися в коханні\n• трахнути\n• заїбати\n• доїбатись\n• дати бан\n• примусити</b>")

    async def watcher(self, message):
        try:
            status = self.db.get("RPMod", "status")
            reply = await message.get_reply_message()
            user = await message.client.get_entity(reply.sender_id)
            me = (await message.client.get_me())
            if status is not False:
                if message.sender_id == me.id:
                    if message.text.lower() == "чмок":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> чмокнув <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "чпок":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> чпокнув <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "кусь":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кусьнув <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "обняти":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> обняв <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "шльоп":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> шльопнув <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "вбити":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> вбив <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "виїбати":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> виїбав <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "звязати":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> звязав <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "вдарити":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> вдарив <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "вїбати":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> вїбав <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "відсосати":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> відсосав у <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "відлизати":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> відлизав в <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "задушити":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> задушив <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "вкрасти":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> вкрав <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "погладити":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> погладив <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "притягнути":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> притягнув <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "згвалтувати":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> згвалтував <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "відшльопати":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> відшльопав <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "наїбати":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> наїбав <a href=tg://user?id={user.id}>{user.first_name}</a>") 
                    if message.text.lower() == "поцілувати":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> поцілував <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "накурити":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> накурив <a href=tg://user?id={user.id}>{user.first_name}</a>") 
                    if message.text.lower() == "набухати":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> набухав <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "засосати":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> засосав <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "втопити":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> втопив <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "розстріляти":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> розстріляв <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "прижати":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> прижав <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "понюхати":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> понюхав <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "віддатись":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> віддався <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "покормити":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> покормив <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "каструвати":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кастрував <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "пихнути":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> пихнув <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "побажати солодких снів ":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> побажав солодких снів <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "лизнути":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> лизнув <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "послати нахуй":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> послав нахуй <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "щіпнути":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> щіпнув <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "дати чапалаха":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> дав чапалаха <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "полюбити":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> полюбив <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "признатися в коханні":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> признався в коханні <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "трахнути":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> трахнув <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "заїбати":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> заїбав <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "доїбатись":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> доїбався до <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "дати бан":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> дав бан <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "примусити":
                       await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> примусив <a href=tg://user?id={user.id}>{user.first_name}</a>")
        except: pass
