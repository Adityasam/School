var firebaseConfig = {
  apiKey: "AIzaSyDiWU5MsRFrTr5JEjoRwxMRPggPXflHnxI",
  authDomain: "arch-98ecf.firebaseapp.com",
  projectId: "arch-98ecf",
  storageBucket: "arch-98ecf.appspot.com",
  messagingSenderId: "71848723152",
  appId: "1:71848723152:web:4fa8569f674138fb32d4d5",
};

firebase.initializeApp(firebaseConfig);

const messaging = firebase.messaging();

function send_push(receiver, title = "", message = "", link = "") {
  var data = new FormData();
  data.append("usercode", receiver);
  var tokendata = load_ajax_data("/get_message_token", data);

  var mytoken =
    "cqz6PhC7nQYpDvl99Ab4It:APA91bEw4ELVxaqKC9D6GlwqlMEuGOGc_OBKS4BGknT93Tn77EO4brJw5R0iNZBpm46awt3bn3hdpVPeZZTr2fg0s_qP4NN2tGilz4dsAd0DObn0U_3yWWysjW4f02ZfSnl4jM3t0lhm";
  for (var i = 0; i < tokendata.length; i++) {
    const notificationPayload = {
      notification: {
        title: title,
        body: message,
        icon: "/static/img/logoblue.png",
        badge: "1",
        click_action: link,
      },
      to: tokendata[i]["token"],
    };

    // Send the notification using the FCM REST API
    fetch("https://fcm.googleapis.com/fcm/send", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization:
          "key=AAAAELqEgtA:APA91bHp3sEYR1_fdZOi-_xlAEEGZEUo-jHyLH3Tl8qXERWkGdVqcBeWGLVvtoF5dACWl6n1frMRSv5IPW4upcnZObY03VaA-5UDUp51zUwvQk5kiRSwMeq7ZeywXZkCOy50M4xqbLZs", // Replace with your FCM server key
      },
      body: JSON.stringify(notificationPayload),
    })
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error(error));
  }
}
