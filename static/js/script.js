async function checkPhishing() {
    const emailContent = document.getElementById("emailInput").value;

    if (!emailContent) {
        alert("Please paste an email to check.");
        return;
    }

    const emailContent1 = document.getElementById("emailInput").value.trim();

    if (!emailContent) {
    alert("Please paste an email to check.");
    return;
    }

    const wordCount = emailContent1.split(/\s+/).length;

    if (wordCount < 20) {
    alert("The email content must be at least 20 words long.");
    return;
}

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: emailContent })
    });

    const data = await response.json();

    const resultElement = document.getElementById("result");

    if (data.prediction) {
        resultElement.textContent = `Prediction: ${data.prediction}`;
        resultElement.classList.remove("phishing", "not-phishing");
        resultElement.classList.add(data.prediction.toLowerCase().replace(" ", "-"));
    } else {
        resultElement.textContent = "Error: Could not determine the result.";
        resultElement.classList.remove("phishing", "not-phishing");
        resultElement.classList.add("phishing");
    }
}
