function copyToClipboard(text) {
	navigator.clipboard
		.writeText(text)
		.then(() => {
			console.log("Text copied to clipboard");
		})
		.catch((err) => {
			console.error("Failed to copy text: ", err);
		});
}

document.getElementById("btn-copy").addEventListener("click", function (event) {
	event.preventDefault();
	var link = document.getElementsByTagName("a").innerText;
	copyToClipboard(link);
	var messageDiv = document.getElementById("message");
	messageDiv.textContent = "Link copied to clipboard!";
});
