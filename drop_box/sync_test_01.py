import dropbox
import os
import time
import contextlib

token = 'sl.A6iJXSOb4LOoCkwy9xeqJq8Eu0l-mOTPQtMQqKq4KZYH4USwpMyOOheNbvXzdlIWQtcq3e5H3bGX0fdYsJQRS6tuziDsKDbFzTrRkPinbVuNWq3lUbDAMPeN8CXHfcpqJqss-Zbp'
dbx = dropbox.Dropbox(token)
# dropbox_data = dbx.users_get_current_account()
# print dir(dropbox_data)
# print dropbox_data.account_type.is_pro()
# print dir(dropbox_data.name)
# members = dbx.sharing_list_file_members('/ribbonRig.txt')
# print members
# dbx.files_upload("C:/Users/pavith/Downloads/unnamed-file-621.png",
#                  '/unnamed-file-621.png')
# download_folder = 'C:/Users/pavith/Downloads'
download_folder = 'D:/temp'

CHUNK_SIZE = 4 * 1024 * 1024


@contextlib.contextmanager
def stopwatch(message):
    """Context manager to print how long a block of code took."""
    t0 = time.time()
    try:
        yield
    finally:
        t1 = time.time()
        print('Total elapsed time for %s: %.3f' % (message, t1 - t0))


for f in os.listdir(download_folder):
    if 'Christina Perri ' in f:
        source_path = os.path.join(download_folder, f)
        target_path = os.path.join('/temp', f).replace('\\', '/')
        print source_path
        print target_path
        file_size = os.path.getsize(source_path)
        with open(source_path, 'rb') as g:
            data = g.read()
        # with stopwatch('upload %d bytes' % len(data)):
        #     dbx.files_upload(data, target_path)
        if file_size <= CHUNK_SIZE:
            dbx.files_upload(g.read(), target_path)
        else:
            upload_session_start_result = dbx.files_upload_session_start(
                data
            )
            cursor = dropbox.files.UploadSessionCursor(
                session_id=upload_session_start_result.session_id,
                offset=data.tell(),
            )
        #     upload_session_start_result = dbx.files_upload_session_start(g.read(CHUNK_SIZE))
        #     cursor = dropbox.files.UploadSessionCursor(session_id=upload_session_start_result.session_id,
        #                                                offset=g.tell())
        #     commit = dropbox.files.CommitInfo(path=target_path)
        #     while g.tell() < file_size:
        #         if (file_size - g.tell()) <= CHUNK_SIZE:
        #             print dbx.files_upload_session_finish(g.read(CHUNK_SIZE),
        #                                                   cursor,
        #                                                   commit)
        #         else:
        #             dbx.files_upload_session_append(g.read(CHUNK_SIZE),
        #                                             cursor.session_id,
        #                                             cursor.offset)
        #             cursor.offset = g.tell()
# for entry in dbx.files_list_folder('').entries:
#     print(entry.name)

f = ['__class__', '__delattr__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__',
     '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
     '__slots__', '__str__', '__subclasshook__', '_account_id_value', '_account_type_value', '_all_field_names_',
     '_all_fields_', '_country_value', '_disabled_value', '_email_value', '_email_verified_value',
     '_has_required_fields', '_is_paired_value', '_locale_value', '_name_value', '_process_custom_annotations',
     '_profile_photo_url_value', '_referral_link_value', '_root_info_value', '_team_member_id_value', '_team_value',
     'account_id', 'account_type', 'country', 'disabled', 'email', 'email_verified', 'is_paired', 'locale', 'name',
     'profile_photo_url', 'referral_link', 'root_info', 'team', 'team_member_id']
account = ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__',
           '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
           '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_basic_validator',
           '_business_validator', '_catch_all', '_get_val_data_type', '_is_tag_present', '_permissioned_tagmaps',
           '_pro_validator', '_process_custom_annotations', '_tag', '_tagmap', '_value', 'basic', 'business',
           'is_basic', 'is_business', 'is_pro', 'pro']
name = ['__class__', '__delattr__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__',
        '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
        '__slots__', '__str__', '__subclasshook__', '_abbreviated_name_value', '_all_field_names_', '_all_fields_',
        '_display_name_value', '_familiar_name_value', '_given_name_value', '_has_required_fields',
        '_process_custom_annotations', '_surname_value', 'abbreviated_name', 'display_name', 'familiar_name',
        'given_name', 'surname']
