// Fetch todos from the backend and display them

function fetchTodos() {
    $.ajax({
        url: '/todos',
        method: 'GET',
        success: function(response) {
            $('#todos-list').empty();
            response.forEach(function(todo) {
                $('#todos-list').append(`<li>${todo.title} - Completed: ${todo.completed}</li>`);
            });
            console.log(response)
        },
        error: function(xhr, status, error) {
            console.error(error);
        }
    });
}

// Add a new todo
function addTodo() {
    let title = $('#writetodo').val();
    if (title) {
        $.ajax({
            url: '/todos',
            method: 'POST',
            action:'/todos',
            
            data:JSON.stringify({ title: title, user_id:1 }), // Change user_id as needed
            ContentType:'application/json',
            success: function(response) {
                fetchTodos();
                $('#writetodo').val('');
                console.log(response);
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    }
    
}

// Call fetchTodos() when the page loads
$(document).ready(function() {
    fetchTodos();
});
