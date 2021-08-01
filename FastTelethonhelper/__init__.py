import sys
import pathlib
import time
import datetime as dt
import os
import telethon
sys.path.insert(0, f"{pathlib.Path(__file__).parent.resolve()}\\")

from FastTelethon import upload_file, download_file
######################### CUSTOM ERRORS ############################
class Nothing_Defined_Error(Exception):
    def __init__(self,message="Define either a reply message(reply arg) or a message to edit(edit_message arg).\n For more info, Visit https://pypi.org/project/FastTelethonhelper/"):
        self.message=message
        super().__init__(self.message)

class Both_Defined_Error(Exception):
    def __init__(self,message="Define one of the two arguments(reply & edit_message). Defining both isn't allowed.\n For more info, Visit https://pypi.org/project/FastTelethonhelper/"):
        self.message=message
        super().__init__(self.message)
####################################################################
class Timer:
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False

def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size < 1024.0 or unit == 'PB':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"

async def download_with_progressbar(client, message, path, edit_message=None, end_message=None, reply=None):
    timer = Timer()
    if reply==None and edit_message==None:
        raise  Nothing_Defined_Error
    
    if reply!=None and edit_message!=None:
        raise Both_Defined_Error
    ################## Checking if the argument given is valid or not ################
    if reply==None:
        reply=edit_message
    try:
        _=reply.id
    except:
        raise telethon.errors.rpcbaseerrors.NotFoundError
    ####################################################################################
    async def progress_bar(downloaded_bytes, total_bytes):
        if timer.can_send():
            data = progress_bar_str(downloaded_bytes, total_bytes)
            await reply.edit(f"Downloading...\n{data}")
    file = message.document
    filename = message.file.name
    dir = f"{path}"
    try:
        if os.path.exists(path):
            pass
        else:
            os.makedirs(path)
    except SyntaxError:
        raise SyntaxError   
    if not filename:
        filename = (
            "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
                    )
    download_location = os.path.join(dir,filename)
    with open(download_location, "wb") as f:
        await download_file(
            client=client, 
            location=file, 
            out=f,
            progress_callback=progress_bar
        )
    if end_message!=None:
        await reply.edit(f"{end_message}")
    return download_location

async def upload_with_progress_bar(client, file_location, reply=None, edit_message=None, end_message=None, name=None, thumbnail=None):
    timer = Timer()
    if reply==None and edit_message==None:
        raise  Nothing_Defined_Error
    
    if reply!=None and edit_message!=None:
        raise Both_Defined_Error
    ################## Checking if the argument given is valid or not ################
    if reply==None:
        reply=edit_message
    try:
        _=reply.id
    except:
        raise telethon.errors.rpcbaseerrors.NotFoundError
    ###################################################################################
    if name == None:
        name = file_location.split("/")[-1]
    async def progress_bar(downloaded_bytes, total_bytes):
        if timer.can_send():
            data = progress_bar_str(downloaded_bytes, total_bytes)
            await reply.edit(f"Uploading...\n{data}")

    with open(file_location, "rb") as f:
        the_file = await upload_file(
            client=client,
            file=f,
            name=name,
            progress_callback=progress_bar
        )
    the_message = await client.send_message(
        reply.chat_id, file=the_file,
        force_document=True,
        thumb=thumbnail
    )
    if end_message!=None:
        await reply.edit(f"{end_message}")
    return the_message

async def download_without_progressbar(client, msg, path, end_message=None):
    file = msg.document
    filename = msg.file.name
    dir = f"{path}"
    try:
        if os.path.exists(path):
            pass
        else:
            os.makedirs(path)
    except SyntaxError:
        raise SyntaxError   
    if not filename:
        filename = (
            "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
                    )
    download_location =os.path.join(dir,filename)
    with open(download_location, "wb") as f:
        await download_file(
            client=client, 
            location=file, 
            out=f,
        )
    if end_message!=None:
        await msg.reply("")
    return download_location

async def upload_without_progress_bar(client, entity, file_location, end_message=None, name=None, thumbnail=None):
    if name == None:
        name = file_location.split("/")[-1]

    with open(file_location, "rb") as f:
        the_file = await upload_file(
            client=client,
            file=f,
            name=name,
        )
    the_message = await client.send_message(
        entity, file=the_file,
        force_document=True,
        thumb=thumbnail
    )
    if end_message!=None:
        await client.send_message(f"{end_message}")
    return the_message

def progress_bar_str(done, total):
    percent = round(done/total*100, 2)
    strin = "░░░░░░░░░░░░░░░░░░░░"
    strin = list(strin)
    for i in range(round(percent)//5):
        strin[i] = "█"
    strin = "".join(strin)
    final = f"Percent: {percent}%\n{human_readable_size(done)}/{human_readable_size(total)}\n{strin}"
    return final
    
