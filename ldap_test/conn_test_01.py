# from ldap3 import Server, Connection, ALL, NTLM
# server = Server('192.168.1.180', get_info=ALL)
# conn = Connection(server, user="rigasite\\Administrator", password="Drfault#543", authentication=NTLM)
# conn.bind()
# print(conn.result)
# print(conn.extend.standard.who_am_i())

from ldap3 import Server, Connection, ALL
from ldap3.utils.conv import escape_bytes

s = Server('192.168.1.180', get_info=ALL)
c = Connection(s, 'Administrator', 'Drfault#543')
c.bind()

binary_sid = b'....'  # your sid must be in binary format
attributes = ["givenName", "sn", "mail", "cn", "uid", "jpegPhoto"]
c.search('my_base', '(objectsid=' + escape_bytes(binary_sid) + ')', attributes=attributes)
print(c.entries)