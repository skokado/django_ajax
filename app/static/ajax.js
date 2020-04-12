document.getElementById("btn").addEventListener("click", function() {
    var result = document.getElementById("result");
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4){  // 通信が完了した後
            if (xhr.status === 200) {  // サーバから正常なレスポンスが返ってきたとき
                result.textContent = xhr.responseText;
            } else {  // サーバエラーが発生したとき
                result.textContent = "エラーが発生しました"
            }
        } else { // 通信が完了する前
            result.textContent = "通信中..."
        }
    }
    encoded_name = encodeURIComponent(document.getElementById("name").value)
    xhr.open("GET", "ajax?name=" + encoded_name, true);
    xhr.send(null);
}, false);
