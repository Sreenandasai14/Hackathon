document.getElementById("advisoryForm").addEventListener("submit", function (event) {
    event.preventDefault();   // 🔥 THIS STOPS REFRESH COMPLETELY

    let crop = document.getElementById("crop").value;
    let stage = document.getElementById("stage").value;
    let weather = document.getElementById("weather").value;

    fetch("http://127.0.0.1:5000/advisory", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            crop: crop,
            stage: stage,
            weather: weather
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("output").innerHTML =
            "<b>Advisory:</b> " + data.message;
    })
    .catch(err => {
        document.getElementById("output").innerHTML =
            "❌ Backend not running";
        console.error(err);
    });
});
