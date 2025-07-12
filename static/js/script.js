document.getElementById("length").addEventListener("input", function() {
  document.getElementById("length-value").textContent = this.value;
});

function generatePassword() {
  const length = document.getElementById("length").value;
  fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ length: length })
  })
    .then(response => response.json())
    .then(data => {
      document.getElementById("output").value = data.password;
    })
    .catch(error => console.error("Error:", error));
}

function copyPassword() {
  const output = document.getElementById("output");
  output.select();
  document.execCommand("copy");
  alert("Password copied!");
}