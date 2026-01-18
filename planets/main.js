const myBox = document.getElementById("new_word_family");

const loadWordFamily = number => {
	fetch('./ack.html')
		.then(res => {
			if (res.ok){
			return res.text();
		}
	})
	.then(WordFamily => {
		targetEl.innerHTML = WordFamily;
	});
};

myBox = addEventListener("click", loadWordFamily);
