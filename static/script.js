var ws;
    function getCurrentDateTime(){
        d = new Date();
        strd = ""
        if (d.getMonth()<10) strd+="0"
        strd+=(d.getMonth()+1)+"/";
        if (d.getDate()<10) strd+="0"
        strd += d.getDate()+"/"+(d.getYear()%100)+" "
        if (d.getHours()<10) strd+="0"
        strd+=d.getHours()+":"
        if (d.getMinutes()<10) strd+="0"
        strd+=d.getMinutes()+":";
        if (d.getSeconds()<10) strd+="0"
        strd+=d.getSeconds();
        return strd;
    }

    function createChatMsg(date, username, message) {
        var msg = document.createElement("div");

        var lidate = document.createElement("i");
        lidate.innerHTML = date+"  ";
        msg.appendChild(lidate);

        var liusername = document.createElement("b");
        liusername.innerHTML = username+": ";
        msg.appendChild(liusername);

        var dom_msg = document.createElement("span");
        dom_msg.innerHTML = message;
        msg.appendChild(dom_msg);

        return msg;
     }

    function openWS(messageContainer) {
        ws = new WebSocket("ws://"+document.domain+":8001/chat");
        ws.onopen = function(){
            messageContainer.appendChild(createChatMsg(getCurrentDateTime(), "[SYSTEM]", "Connection open"));
        }
        ws.onmessage = function(e) {
          var data = JSON.parse(e.data);
          messageContainer.appendChild(createChatMsg(data.date, data.username, data.message));
          messageContainer.scrollTop = messageContainer.scrollHeight;
        };
        ws.onclose = function(e) {
          openWS(messageContainer);
        };
        ws.onerror = function(error){
            console.log('Error detected: ' + error);
        }
    }

      function sendMessage() {
        var data = { username: document.getElementById("username").value,
                     message: document.getElementById("message").value,
                     date: getCurrentDateTime()};

        if(data.username && data.message) {
          ws.send(JSON.stringify(data));
          document.getElementById("message").value;
        }
      }

      window.onload = function() {
        var messageContainer = document.getElementById("chat");
        if("WebSocket" in window) {
          messageContainer.appendChild(createChatMsg(getCurrentDateTime(), "[SYSTEM]", "WebSocket is supported by your browser!"));
          messageContainer.appendChild(createChatMsg(getCurrentDateTime(), "[SYSTEM]", "Pick a username and start sending out messages."));
          openWS(messageContainer);
        }
        else {
          messageContainer.appendChild(createChatMsg(getCurrentDateTime(), "[SYSTEM]", "WebSocket is NOT supported by your browser!"));
        }
      }