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
  from FastTelethonhelper import fast_download
  ```
- When you need to download file, 
    ```
    downloaded_location = await fast_download(client, msg, reply, download_folder, progress_bar_function)
    ```
    - `client` = Telegram Client(Required)
    - `msg` = The message object which has the file to be downloaded(Required)
    - `reply` = The message on which you want the progressbar(Optional)
    - `download_folder` = Location where you want file to be downloaded, defaults to ./downloads/ (Optional)
    - `progress_bar_function` = The function you want to use to display the string in progressbar, it needs to have 2 parameters done bytes and total bytes and must return a desired string, defaults to a function I wrote(Optional)
  
</br>
- The function returns the download location.

</br>
</br>

### Uploads:
- Usage
  ```
  from FastTelethonhelper import fast_upload
  ```
- When you need to upload file, 
  ```
  await fast_upload(client, file_location, reply, name, progress_bar_function)
  ```
  - `client` = TelegramClient(Required)
  - `file_location` = Where the file is located(Required)
  - `reply` = The message object you want the progressbar to appear(Optional)
  - `name` = Name of the file you want while uploading(Optional)
  - `progress_bar_function` = The function you want to use to display the string in progressbar, it needs to have 2 parameters done bytes and total bytes and must return a desired string, defaults to a function I wrote(Optional)
- This function returns the file object which you can use in send_message in telethon example 
  ``` 
  await bot.send_message(file=<what this function returns>)
  ```

</br>
</br>

# Credits
- [MiyukiKun](https://github.com/MiyukiKun) for getting this together
- [Loonami](https://github.com/LonamiWebs) for [telethon](https://github.com/LonamiWebs/Telethon)
- [Tulir Asokan](https://github.com/tulir) for [mautrix-telegram](https://github.com/tulir/mautrix-telegram)
