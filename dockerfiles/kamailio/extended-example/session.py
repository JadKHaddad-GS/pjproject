from application import App, Account, CallerCall, SIP_HOST, SIP_PORT
import pjsua2 as pj
import logging
import time

if __name__ == "__main__":
    logging.basicConfig(filename="session.log",
    filemode='w',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO)

    account_1 = Account(username="user1", password="user1")
    account_2 = Account(username="user2", password="user2")
    account_3 = Account(username="user3", password="user3")
    account_4 = Account(username="user4", password="user4")
    app = App(sip_host=SIP_HOST, sip_port=SIP_PORT, accounts=[account_1, account_2, account_3, account_4])

    app.handle_events()

    app.destroy()