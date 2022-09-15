from application import App, Account, CallerCall, SIP_HOST, SIP_PORT
import pjsua2 as pj
import logging
import time

CALLED_USER = "user2"

if __name__ == "__main__":
    logging.basicConfig(filename="caller.log",
    filemode='w',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO)

    logger = logging.getLogger('Caller')

    account = Account(logger=logger, username="user1", password="user1")
    app = App(logger=logger, sip_host=SIP_HOST, sip_port=SIP_PORT, account=account)

    time.sleep(3)
    call = CallerCall(account, logger)
    call_op_prm = pj.CallOpParam()
    try:
        call.makeCall(f"sip:{CALLED_USER}@{SIP_HOST}:{SIP_PORT}", call_op_prm)
    except pj.Error as e:
        logger.error(f"Exception: {e.status} {e.reason}")
    except Exception as e:
        logger.error(f"Exception: {e}")


    app.handle_events()

    app.destroy()