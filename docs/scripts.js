fetch("https://api.github.com/repos/CreativeWiz17/phy/commits")
.then(response => response.json())

.then(data => 
    {

    const commitsDiv = document.getElementById("commits");

    commitsDiv.innerHTML = "";

    data.slice(0, 5).forEach(commit => {

        commitsDiv.innerHTML += `
            <p>${commit.commit.message}</p>
        `;

    });

    }
    );