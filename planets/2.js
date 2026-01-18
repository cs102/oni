const container = document.getElementById("container")

fetch("https://jsonplaceholder.typicode.com/todos")
	.then((response) => response.json())
	
	.then((json) => {
		json.forEach((item) => {
			container.innerHTML += `<div class='item'>
			userId: ${item.userId}
			id: ${item.id}
			title: ${item.title}
			completed: ${item.completed}
			</div>`
		})
	})

