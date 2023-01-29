
let form = document.getElementById('login-form')

form.addEventListener('submit', (e) => {
    e.preventDefault() // to prevent the form from refreshing so that we can perform other actions 

    let formData = {
        'username': form.username.value,
        'password': form.password.value
    }

    fetch('http://127.0.0.1:8000/api/users/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('DATA:', data.access)
        if(data.access){
            localStorage.setItem('token', data.access)
            window.location = 'file:///E:/Files/Others/UdemyCourses/Python%20Django%20-%20Complete%20Course/Project/frontend/projects-list.html'
        } else {
            alert('Username or password incorrect!')
        }
    })
    
})