async function summarizeText() {
    let text = document.getElementById("inputText").value;
    if (!text) {
        alert("Please enter some text!");
        return;
    }

    let response = await fetch("http://localhost:5000", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    });

    let data = await response.json();
    document.getElementById("summary").innerText = data.summary;
}
