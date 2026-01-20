// ASYNC AWAIT
const url = 'https://jsonplaceholder.typicode.com/users'
fetch(url)
    .then((response) => {
      if (!response.ok) throw new Error('Something went wrong organic life form!');
      return response.json(); // Extract JSON string to a JS Object
      console.log(response)
    })
    .then((dataArray) => {
      console.log(dataArray)
      
      list.innerHTML = dataArray
      .map(({ id, name, email, address, company }) => {
        return `<li class="list-item" "data-uid="${id}">
        <p>${name}</p>
        <p>${email}</p>
        <p>${address.city}</p>
		<p>${company.catchPhrase}</p>
        </li>`;
      })
    .join('');
      //console.log(dataArray);

    })
    .catch(err=> {
      console.warn(err.message);
    });

	
