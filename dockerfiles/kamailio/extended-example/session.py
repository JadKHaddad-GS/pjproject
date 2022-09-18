from application import App, Account, CallerCall, SIP_HOST, SIP_PORT
import pjsua2 as pj
import logging
import time
from multiprocessing import Process


def app(name, caller_usernaname, called_username):
    app = App(sip_host=SIP_HOST, sip_port=SIP_PORT, name=name, run_time=30)
    account_1 = Account(username=caller_usernaname, password=caller_usernaname)
    account_2 = Account(username=called_username, password=called_username)
    call = CallerCall(account_1, account_2.username)
    time.sleep(3)
    try:
        call.makeCall(
            f"sip:{account_2.username}@{SIP_HOST}:{SIP_PORT}", pj.CallOpParam()
        )
    except pj.Error as e:
        logging.error(f"Exception: {e.status} {e.reason}")
    except Exception as e:
        logging.error(f"Exception: {e}")

    app.handle_events()
    app.destroy()


if __name__ == "__main__":
    logging.basicConfig(
        filename="session.log",
        filemode="a",
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )

    app = App(sip_host=SIP_HOST, sip_port=SIP_PORT, name="app", run_time=10, handle_events_timeout=10)
    account_1 = Account(username="user1", password="user1")
    account_2 = Account(username="user2", password="user2")
    call = CallerCall(account_1, account_2.username)
    
    account_3 = Account(username="user3", password="user3")
    account_4 = Account(username="user4", password="user4")
    call_2 = CallerCall(account_3, account_4.username)

    account_5 = Account(username="user5", password="user5")
    account_6 = Account(username="user6", password="user6")
    call_3 = CallerCall(account_5, account_6.username)
    
    try:
        call.makeCall(
            f"sip:{account_2.username}@{SIP_HOST}:{SIP_PORT}", pj.CallOpParam()
        )
        call_2.makeCall(
            f"sip:{account_4.username}@{SIP_HOST}:{SIP_PORT}", pj.CallOpParam()
        )
        call_3.makeCall(
            f"sip:{account_6.username}@{SIP_HOST}:{SIP_PORT}", pj.CallOpParam()
        )
    except pj.Error as e:
        logging.error(f"Exception: {e.status} {e.reason}")
    except Exception as e:
        logging.error(f"Exception: {e}")

    # not receiving incoming calls for user4 and user6 (Busy here)
    app.handle_events()
    app.destroy()

    # run in different processes

    # p1 = Process(target=app, args=("app1", "user1", "user2"))
    # p1.start()

    # p2 = Process(target=app, args=("app2", "user3", "user4"))
    # p2.start()

    # p3 = Process(target=app, args=("app3", "user5", "user6"))
    # p3.start()

    # p4 = Process(target=app, args=("app4", "user7", "user8"))
    # p4.start()

    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
