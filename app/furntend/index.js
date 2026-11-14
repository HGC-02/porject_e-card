async function postData(
  payload = {
    test: "hello world",
  },
) {
  try {
    const response = await fetch(window.location.origin + "/rec", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const result = await response.json();
    console.log("Created:", result);
  } catch (error) {
    console.error("Error posting data:", error);
  }
}

async function QrCode() {
  const response = await fetch(window.location.origin + "/qr");

  // Check if the HTTP request was successful (status 200-299)
  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }

  // Parse the response body as JSON
  const data = await response.json();
  const img = document.getElementById("QR");
  const name = document.getElementById("name");
  name.textContent = data.qr_name;
  console.log("hi:", data.qr_name);
  console.log(data.file_name);
  console.log(data);

  img.src = "qr/" + data.file_name;
  return data;
}
QrCode();
