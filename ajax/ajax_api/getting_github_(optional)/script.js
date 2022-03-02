function get_git(){
    fetch("https://api.github.com/users/adion81")
    .then(response => response.json() )
    .then(coderData => {
        console.log(coderData)
        var coder_name = coderData['name']
        var coder_followers = coderData['followers']
        var coder_avatar = coderData['avatar_url']
        var info = document.querySelector('#info')
        var avatar = document.querySelector('#avatar')
        info.innerHTML = coder_name + ' has ' + coder_followers +' followers.'
        avatar.src = coder_avatar
    })
    .catch(err => console.log(err) )
}

function search(){
    var user_input = document.querySelector('#username')
    var search_value = user_input.value
    fetch(`https://api.github.com/users/${search_value}`)
    .then(response => response.json() )
    .then(coderData => {
        console.log(coderData)
        var coder_name = coderData['name']
        var coder_followers = coderData['followers']
        var coder_avatar = coderData['avatar_url']
        var info = document.querySelector('#info')
        var avatar = document.querySelector('#avatar')
        info.innerHTML = coder_name + ' has ' + coder_followers +' followers.'
        avatar.src = coder_avatar
    })
    .catch(err => console.log(err) )
}