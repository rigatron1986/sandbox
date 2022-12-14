import os

from tqdm import tqdm

import dropbox


def upload(
        access_token,
        file_path,
        target_path,
        timeout=20000,
        chunk_size=4 * 1024 * 1024,
):
    dbx = dropbox.Dropbox(access_token, timeout=timeout)
    with open(file_path, "rb") as f:
        file_size = os.path.getsize(file_path)
        chunk_size = 4 * 1024 * 1024
        if file_size <= chunk_size:
            print(dbx.files_upload(f.read(), target_path))
        else:
            with tqdm(total=file_size, desc="Uploaded") as pbar:
                upload_session_start_result = dbx.files_upload_session_start(
                    f.read(chunk_size)
                )
                pbar.update(chunk_size)
                cursor = dropbox.files.UploadSessionCursor(
                    session_id=upload_session_start_result.session_id,
                    offset=f.tell(),
                )
                commit = dropbox.files.CommitInfo(path=target_path)
                while f.tell() < file_size:
                    if (file_size - f.tell()) <= chunk_size:
                        print(
                            dbx.files_upload_session_finish(
                                f.read(chunk_size), cursor, commit
                            )
                        )
                    else:
                        dbx.files_upload_session_append(
                            f.read(chunk_size),
                            cursor.session_id,
                            cursor.offset,
                        )
                        cursor.offset = f.tell()
                    pbar.update(chunk_size)


upload(
    access_token='sl.A6iJXSOb4LOoCkwy9xeqJq8Eu0l-mOTPQtMQqKq4KZYH4USwpMyOOheNbvXzdlIWQtcq3e5H3bGX0fdYsJQRS6tuziDsKDbFzTrRkPinbVuNWq3lUbDAMPeN8CXHfcpqJqss-Zbp',
    file_path="D:/temp/Splash Splash Love LOVE Ep 2 [Eng Sub] Ur Choice.mp4",
    target_path='/temp/Splash Splash Love LOVE Ep 2 [Eng Sub] Ur Choice.mp4'
)
