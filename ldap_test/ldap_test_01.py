from ldap3 import Server, Connection, ALL, NTLM, SIMPLE

LDAP_HOST = '192.168.1.180'
LDAP_PORT = '389'
LDAP_PASSWORD = 'admin@321'
LDAP_BASE_DN = "cn=Users,dc=rigasite,dc=com"
LDAP_DOMAIN = "rigasite.com"
LDAP_USER = "Administrator"
LDAP_GROUP = ""
LDAP_SSL = False
EMAIL_DOMAIN = "example.com"
LDAP_EXCLUDED_ACCOUNTS = "Administrator,TestAccount,Guest,krbtgt,test"
LDAP_IS_AD = True
LDAP_IS_AD_SIMPLE = False


def clean_value(value):
    cleaned_value = str(value)
    if cleaned_value == "[]":
        cleaned_value = ""
    return cleaned_value


def search_ad_users(conn, excluded_accounts):
    attributes = [
        "givenName",
        "sn",
        "sAMAccountName",
        "mail",
        "thumbnailPhoto",
        "userAccountControl",
    ]
    query = "(objectCategory=person)"
    if len(LDAP_GROUP) > 0:
        query = "(&(objectClass=person)(memberOf=%s))" % LDAP_GROUP
    conn.search(LDAP_BASE_DN, query, attributes=attributes)
    return [
        {
            "first_name": clean_value(entry.givenName),
            "last_name": clean_value(entry.sn),
            "email": clean_value(entry.mail),
            "desktop_login": clean_value(entry.sAMAccountName),
            "thumbnail": entry.thumbnailPhoto.raw_values,
            "active": bool(entry.userAccountControl.value & 2) is False,
        }
        for entry in conn.entries
        if clean_value(entry.sAMAccountName) not in excluded_accounts
    ]


def search_ldap_users(conn, excluded_accounts):
    attributes = ["givenName", "sn", "mail", "cn", "uid", "jpegPhoto"]
    conn.search(
        LDAP_BASE_DN, "(objectclass=person)", attributes=attributes
    )
    return [
        {
            "first_name": clean_value(entry.givenName),
            "last_name": clean_value(entry.sn),
            "email": clean_value(entry.mail),
            "desktop_login": clean_value(entry.uid),
            "thumbnail": entry.jpegPhoto.raw_values,
        }
        for entry in conn.entries
        if clean_value(entry.uid) not in excluded_accounts
    ]


def get_ldap_users():
    excluded_accounts = LDAP_EXCLUDED_ACCOUNTS.split(",")
    ldap_server = "%s:%s" % (LDAP_HOST, LDAP_PORT)
    SSL = LDAP_SSL
    if LDAP_IS_AD_SIMPLE:
        user = LDAP_USER
        authentication = SIMPLE
        SSL = True
    elif LDAP_IS_AD:
        user = "%s\%s" % (LDAP_DOMAIN, LDAP_USER)
        authentication = NTLM
    else:
        user = "uid=%s,%s" % (LDAP_USER, LDAP_BASE_DN)
        authentication = SIMPLE

    server = Server(ldap_server, get_info=ALL, use_ssl=SSL)
    print(server)
    conn = Connection(
        server,
        user=user,
        password=LDAP_PASSWORD,
        authentication=authentication,
        raise_exceptions=True,
        auto_bind=True,
    )
    if LDAP_IS_AD:
        return search_ad_users(conn, excluded_accounts)
    else:
        return search_ldap_users(conn, excluded_accounts)


ldap_users = get_ldap_users()
# print(ldap_users)
for user in ldap_users:
    print(user)
