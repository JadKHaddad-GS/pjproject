#include <pjsua2.hpp>
#include <iostream>

using namespace pj;

// Subclass to extend the Account and get notifications etc.
class MyAccount : public Account {
public:
    virtual void onRegState(OnRegStateParam &prm) {
        AccountInfo ai = getInfo();
        std::cout << (ai.regIsActive? "*** Register:" : "*** Unregister:")
                  << " code=" << prm.code << std::endl;
    }
};

int main()
{
    Endpoint ep;

    ep.libCreate();

    // Initialize endpoint
    EpConfig ep_cfg;
    ep.libInit( ep_cfg );

    // Create SIP transport. Error handling sample is shown
    TransportConfig tcfg;
    tcfg.port = 0;
    try {
        ep.transportCreate(PJSIP_TRANSPORT_UDP, tcfg);
    } catch (Error &err) {
        std::cout << err.info() << std::endl;
        return 1;
    }

    // Start the library (worker threads etc)
    ep.libStart();
    std::cout << "*** PJSUA2 STARTED ***" << std::endl;

    // Configure an AccountConfig
    AccountConfig acfg;
    acfg.idUri = "sip:user1@kamailio5.5.0-trusty:5060";
    acfg.regConfig.registrarUri = "sip:kamailio5.5.0-trusty:5060";
    AuthCredInfo cred("digest", "*", "user1", 0, "user1");
    acfg.sipConfig.authCreds.push_back( cred );

    // Create the account
    MyAccount *acc = new MyAccount;
    acc->create(acfg);

    // Here we don't have anything else to do..
    pj_thread_sleep(10000);

    // Delete the account. This will unregister from server
    delete acc;

    // This will implicitly shutdown the rary
    return 0;
}
//g++ ./main.cpp -lg7221codec -lgsmcodec -lilbccodec -lpj -lpjsip-simple -lpjsip-ua -lpjsip -lpjsua -lpjsua2 -lpjlib-util -lpjmedia-audiodev -lresample -lspeex -lsrtp -lwebrtc -lyuv -lpjmedia-codec -lpjmedia-videodev -lpjmedia -lpjnath -o main

