from application import App, Account, CallerCall, SIP_HOST, SIP_PORT
import pjsua2 as pj
import logging
import time

if __name__ == "__main__":
    logging.basicConfig(
        filename="session.log",
        filemode="w",
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )

    app = App(sip_host=SIP_HOST, sip_port=SIP_PORT, name="app1")

    account_1 = Account(username="user1", password="user1")
    account_2 = Account(username="user2", password="user2")
    # account_3 = Account(username="user3", password="user3")
    # account_4 = Account(username="user4", password="user4")
    # account_5 = Account(username="user5", password="user5")
    # account_6 = Account(username="user6", password="user6")
    # account_7 = Account(username="user7", password="user7")
    # account_8 = Account(username="user8", password="user8")

    call_1 = CallerCall(account_1, account_2.username)
    # call_3 = CallerCall(account_3, account_4.username)
    # call_5 = CallerCall(account_5, account_6.username)
    # call_7 = CallerCall(account_7, account_8.username)

    time.sleep(3)
    try:
        call_1.makeCall(
            f"sip:{account_2.username}@{SIP_HOST}:{SIP_PORT}", pj.CallOpParam()
        )
        # call_3.makeCall(f"sip:{account_4.username}@{SIP_HOST}:{SIP_PORT}", pj.CallOpParam())
        # call_5.makeCall(f"sip:{account_6.username}@{SIP_HOST}:{SIP_PORT}", pj.CallOpParam())
        # call_7.makeCall(f"sip:{account_8.username}@{SIP_HOST}:{SIP_PORT}", pj.CallOpParam())
    except pj.Error as e:
        logging.error(f"Exception: {e.status} {e.reason}")
    except Exception as e:
        logging.error(f"Exception: {e}")

    app.handle_events()

    app.destroy()
