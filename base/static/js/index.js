async function getStats(endpoint, id) {
    URL = 'http://127.0.0.1:8000/api/'+endpoint;
    const response = await fetch(URL);
    const data = await response.json();
    console.log(data);
    document.getElementById(id).innerHTML = JSON.stringify(data, null, 2);
}