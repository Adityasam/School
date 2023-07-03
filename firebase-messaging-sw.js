if ('function' === typeof importScripts) {
    importScripts('https://www.gstatic.com/firebasejs/7.6.1/firebase-app.js');
    importScripts('https://www.gstatic.com/firebasejs/7.6.1/firebase-messaging.js');
    addEventListener('message', onMessage);


    function onMessage(e) {
        // do some work here 
    }
}

var config = {
    messagingSenderId: "71848723152",
    apiKey: "AIzaSyDiWU5MsRFrTr5JEjoRwxMRPggPXflHnxI",
    projectId: "arch-98ecf",
    appId: "1:71848723152:web:4fa8569f674138fb32d4d5"
};
firebase.initializeApp(config);

const messaging = firebase.messaging();
const broadcast = new BroadcastChannel('firebase-channel');

messaging.setBackgroundMessageHandler(payload => {
    console.log(payload);
    const notif = (payload.data);
    const notifTitle = notif.title;
    const notifBody = notif.body;

    broadcast.postMessage({
        notificationTitle: notifTitle,
        notificationBody: notifBody
    });

});

