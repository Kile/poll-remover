import json

from discord import Locale
from typing import Dict

# Load the config from the JSON file
with open("config.json") as f:
    CONFIG = json.load(f)

TOKEN = CONFIG["token"]

PREFIX = "." # Is never used

LANGS: Dict[Locale, Dict[str, str]] = {
    Locale.american_english: {
        "title": "Poll deleted",
        "description": "Hi **{user}**, I just deleted the poll you posted in the server **{server}** because it is under Poll Bot Protection:tm:. You are not allowed to create polls in this server without Manage Server permissions!",
        "invite_text": "Invite me to get rid of polls for anyone without Manage Server permissions!",
        "button": "Get Poll Protection for your server",
        "button_short": "Invite me",
        "why": "Why am I not allowed to create polls?",
        "why_desc": "Discord currently does not offer a sepeate permission to restrict creating polls. " +
                    "Polls can be abused to spam chat with big message chunks, but can also circumvent automod. " +
                    "This bot is a workaround for that."
    },
    Locale.german: {
        "title": "Poll gelöscht",
        "description": "Hallo **{user}**, ich habe gerade einen Poll gelöscht, den du im Server **{server}** gepostet hast, weil dieser unter Poll Bot Protection:tm: steht. Du darfst in diesem Server keine Polls senden, ohne Manage Server Permissions zu haben!",
        "invite_text": "Lade mich in deinen Server ein, um Polls für jeden ohne Manage Server Permissions zu entfernen!",
        "button": "Hol dir Poll Protection für deinen Server",
        "button_short": "Lade mich ein",
        "why": "Warum darf ich keine Polls erstellen?",
        "why_desc": "Discord bietet derzeit keine extra Permission an, das Erstellen von Polls zu beschränken. " +
                    "Polls können missbraucht werden, um den Chat mit großen Nachrichtenblöcken zu spammen, können aber auch den Automod umgehen. " +
                    "Dieser Bot ist ein Workaround dafür."
    },
    Locale.latin_american_spanish: { # This and anything after is AI generatated, so it may not be accurate
        "title": "Encuesta eliminada",
        "description": "Hola **{user}**, acabo de eliminar la encuesta que publicaste en el servidor **{server}** porque está bajo la protección de Poll Bot:tm:. ¡No puedes crear encuestas en este servidor sin permisos de Administrar servidor!",
        "invite_text": "¡Invítame para eliminar encuestas para cualquiera sin permisos de Administrar servidor!",
        "button": "Obtén Protección de Encuestas para tu servidor",
        "button_short": "Invítame",
        "why": "¿Por qué no puedo crear encuestas?",
        "why_desc": "Discord actualmente no ofrece un permiso separado para restringir la creación de encuestas. " +
                    "Las encuestas pueden ser abusadas para llenar el chat con grandes bloques de mensajes, pero también pueden eludir el automod. " +
                    "Este bot es una solución alternativa para eso."
    },
    Locale.french: {
        "title": "Sondage supprimé",
        "description": "Salut **{user}**, je viens de supprimer le sondage que tu as posté dans le serveur **{server}** car il est sous la protection de Poll Bot:tm:. Vous n'êtes pas autorisé à créer des sondages dans ce serveur sans les autorisations de Gérer le serveur!",
        "invite_text": "Invitez-moi pour supprimer les sondages pour quiconque sans les autorisations de Gérer le serveur!",
        "button": "Obtenez une protection de sondage pour votre serveur",
        "button_short": "Invitez-moi",
        "why": "Pourquoi ne puis-je pas créer de sondages?",
        "why_desc": "Discord n'offre actuellement pas de permission distincte pour restreindre la création de sondages. " +
                    "Les sondages peuvent être abusés pour spammer le chat avec de gros blocs de messages, mais peuvent également contourner l'automod. " +
                    "Ce bot est une solution de contournement pour cela."
    },
    Locale.spain_spanish: {
        "title": "Encuesta eliminada",
        "description": "Hola **{user}**, acabo de eliminar la encuesta que publicaste en el servidor **{server}** porque está bajo la protección de Poll Bot:tm:. ¡No puedes crear encuestas en este servidor sin permisos de Administrar servidor!",
        "invite_text": "¡Invítame para eliminar encuestas para cualquiera sin permisos de Administrar servidor!",
        "button": "Obtén Protección de Encuestas para tu servidor",
        "button_short": "Invítame",
        "why": "¿Por qué no puedo crear encuestas?",
        "why_desc": "Discord actualmente no ofrece un permiso separado para restringir la creación de encuestas. " +
                    "Las encuestas pueden ser abusadas para llenar el chat con grandes bloques de mensajes, pero también pueden eludir el automod. " +
                    "Este bot es una solución alternativa para eso."
    },
    Locale.turkish: {
        "title": "Anket silindi",
        "description": "Merhaba **{user}**, Poll Bot Koruma:tm: altında olduğu için **{server}** sunucusunda yayınladığınız anketi sildim. Sunucuda Sunucu Yönetimi izinlerine sahip olmadan anket oluşturamazsınız!",
        "invite_text": "Sunucunuzdaki herkes için anketleri kaldırmak için beni davet edin!",
        "button": "Sunucunuz için Anket Koruma alın",
        "button_short": "Beni davet et",
        "why": "Neden anket oluşturamıyorum?",
        "why_desc": "Discord şu anda anket oluşturmayı sınırlamak için ayrı bir izin sunmuyor. " +
                    "Anketler, sohbeti büyük mesaj bloklarıyla doldurmak için kötüye kullanılabilir, ancak aynı zamanda otomatik modu atlayabilir. " +
                    "Bu bot bunun için bir çözüm yolu."
    },
}

# Add British English as an alias for American English
LANGS[Locale.british_english] = LANGS[Locale.american_english]