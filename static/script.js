var ws; //global WebSocket connection varieble
var message_container
var input_message;
    function createChatMsg(date, username, message) {
        //adding new messages to message_container
        var msg = document.createElement("div");

        var lidate = document.createElement("i");
        lidate.innerHTML = (new Date(date)).toLocaleString()+"  ";
        msg.appendChild(lidate);

        var liusername = document.createElement("b");
        liusername.innerHTML = username+": ";
        msg.appendChild(liusername);

        var dom_msg = document.createElement("span");
        dom_msg.innerHTML = message;
        msg.appendChild(dom_msg);

        message_container.appendChild(msg);
     }

    function openWS() {
        //opening WebSocket connection
        ws = new WebSocket("ws://"+document.domain+":"+_port+"/chat");
        ws.onopen = function(){
        //Invoked when a new WebSocket is opened.
            createChatMsg(Date(), "[SYSTEM]", "Connection open");
        }
        ws.onmessage = function(e) {
        //Handle incoming messages on the WebSocket
          var data = JSON.parse(e.data);
          createChatMsg(data.date, data.username, data.message);
          message_container.scrollTop = message_container.scrollHeight;
        };
        ws.onclose = function(e) {
        //Invoked when the WebSocket is closed.
          openWS();
        };
        ws.onerror = function(error){
        //Invoked when the WebSocket is closed.
            console.log('Error detected: ' + error);
        }
    }

      function sendMessage() {
      //Sending message to server in JSON format
        var data = { username: _username,
                     message: input_message.value};

        if(data.username && data.message) {
          ws.send(JSON.stringify(data));
          input_message.value="";
        }
      }

      window.onload = function() {
        //initializing global variables and handlers
        message_container = document.getElementById("chat");
        input_message  = document.getElementById("message");
        input_message.addEventListener('keypress', function(e) {
          if (e.keyCode == 13) {
            sendMessage()
          }
        });
        var date = new Date()
        console.log(date);
        //Checking if webbrowser allowing WebSockets
        if("WebSocket" in window) {

          createChatMsg(date, "[SYSTEM]", "WebSocket is supported by your browser!");
          openWS();
        }
        else {
          createChatMsg(date, "[SYSTEM]", "WebSocket is NOT supported by your browser!");
        }
      }
