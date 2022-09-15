from re import A
from application import App, Account, SIP_HOST, SIP_PORT
import logging

if __name__ == "__main__":
    logging.basicConfig(filename="answerer.log",
    filemode='w',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO)

    logger = logging.getLogger('Answerer')

    account = Account(logger=logger, username="user2", password="user2")
    app = App(logger=logger, sip_host=SIP_HOST, sip_port=SIP_PORT, account=account)

    app.handle_events()

    app.destroy()