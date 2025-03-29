async function checkEmail() {
    const emailContent = document.getElementById("emailInput").value;

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: emailContent })
    });

    const result = await response.json();
    const resultDiv = document.getElementById("result");

    if (result.prediction === "Phishing") {
        resultDiv.innerHTML = "🚨 <span style='color: red;'>This email is a PHISHING attempt!</span>";
    } else {
        resultDiv.innerHTML = "✅ <span style='color: green;'>This email is SAFE.</span>";
    }
}
