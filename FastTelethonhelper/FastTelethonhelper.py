from FastTelethon import upload_file, download_file
import time
import datetime as dt

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

async def download_with_progressbar(client, reply, msg):
    timer = Timer()

    async def progress_bar(downloaded_bytes, total_bytes):
        if timer.can_send():
            data = progress_bar_str(downloaded_bytes, total_bytes)
            await reply.edit(f"Downloading...\n{data}")

    file = msg.document
    filename = msg.file.name
    dir = f"downloads/"
    if not filename:
        filename = (
            "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
                    )
    download_location = dir + filename
    with open(download_location, "wb") as f:
        await download_file(
            client=client, 
            location=file, 
            out=f,
            progress_callback=progress_bar
        )
    await reply.edit("Finished downloading")
    return download_location

async def upload_with_progress_bar(client, reply, file_location, name=None, thumbnail=None):
    timer = Timer()
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
    reply.edit("Finished uploading")
    return the_message

async def download_without_progressbar(client, msg):
    file = msg.document
    filename = msg.file.name
    dir = f"downloads/"
    if not filename:
        filename = (
            "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
                    )
    download_location = dir + filename
    with open(download_location, "wb") as f:
        await download_file(
            client=client, 
            location=file, 
            out=f,
        )
    return download_location

async def upload_without_progress_bar(client, entity, file_location, name=None, thumbnail=None):
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
    return the_message

def progress_bar_str(done, total):
    percent = round(done/total*100, 2)
    bar = ["█","░"]
    strin = ""
    for i in range(round(percent)//5):
        strin = f"{strin}{bar[0]}"
    for i in range(20-(round(percent)//5)):
        strin = f"{strin}{bar[1]}"
    final = f"Percent: {percent}%\n{human_readable_size(done)}/{human_readable_size(total)}\n{strin}"
    return final
    