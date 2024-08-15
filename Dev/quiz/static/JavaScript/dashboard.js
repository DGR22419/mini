// script.js

function createQuiz() {
    // Redirect to the create quiz page
    alert('Redirecting to Create Quiz Page');
    window.location.href = "/q/create";
}

function joinQuiz() {
    // Redirect to the join quiz page
    alert('Redirecting to Join Quiz Page');
    window.location.href = "/q/join_room";
}

// function logout() {
//     // Redirect to the join quiz page
//     // alert('Redirecting to Join Quiz Page');
//     window.location.href = "/logout/";
// }

document.getElementById("logout-btn").addEventListener("click", function(event) {
            event.preventDefault(); // Prevent the default action of the link
            logout2(); // Call the logout function
        });

        function logout2() {
            fetch('/logout/', {
                method: 'POST',
                
            }).then(response => {
                if (response.ok) {
                    window.location.href = "/"; // Redirect to login page after logout
                } else {
                    alert("Logout failed");
                }
            });
        }