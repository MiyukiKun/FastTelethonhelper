# FastTelethon helper

- Make use of FastTelethon to upload and download files

## Usage:
</br>

## Installation:
  ```
  pip install FastTelethonhelper
  ```

### Downloads:
- Usage
  ```
  from FastTelethonhelper import download_with_progressbar
  ```
- When you need to download file, 
    ```
    downloaded_location = await download_with_progressbar(client, reply, message)
    ```
- The function returns the download location.
- `reply` is the message object you want the progress bar to be displayed on
- `message` is the message object that contains the file you need to download.
- There is a similar function without progressbar where you dont need to give `reply` object, rest is same
</br>
</br>

### Uploads:
- Usage
  ```
  from FastTelethonhelper import upload_with_progressbar
  ```
- When you need to upload file, 
  ```
  await upload_with_progressbar(client, reply, file_location, name, thumbnail)
  ```
- This function returns the message object(the one in which file was sent)
- `reply` is the message object you want the progress bar to be displayed on
- `file_location` is where the file is located that you want to upload
- `name` (optional) if you want to change the name of file you are uploading, leave as None if you dont want to change it.
- `thumbnail`(optional) the thumbnail of the file you want to display when sending the file
- Note* the file will be sent in same chat as the progressbar display message.
- There is a similar function without progressbar where you  need to give `entity` of chat you want to send file to instead of `reply` object, rest is same

</br>
</br>

# Credits
- [MiyukiKun](https://github.com/MiyukiKun) for getting this together
- [Loonami](https://github.com/LonamiWebs) for [telethon](https://github.com/LonamiWebs/Telethon)
- [Tulir Asokan](https://github.com/tulir) for [mautrix-telegram](https://github.com/tulir/mautrix-telegram)
