const postForm = document.getElementById('postForm');
const postsContainer = document.getElementById('posts');

async function fetchPosts() {
    const response = await fetch('http://127.0.0.1:5000/posts');
    const posts = await response.json();
    displayPosts(posts);
}

function displayPosts(posts) {
    postsContainer.innerHTML = '';
    posts.forEach((post, index) => {
        const postElement = document.createElement('div');
        postElement.className = 'post';
        postElement.innerHTML = `
            <h3>${post.title}</h3>
            <p>${post.content}</p>
            <button onclick="deletePost(${index})">Delete</button>
        `;
        postsContainer.appendChild(postElement);
    });
}

postForm.addEventListener('submit', async function(event) {
    event.preventDefault();
    const title = document.getElementById('title').value.trim();
    const content = document.getElementById('content').value.trim();

    if (!title || !content) {
        alert('Please fill in both fields');
        return;
    }

    await fetch('http://127.0.0.1:5000/posts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title, content })
    });

    postForm.reset();
    fetchPosts();
});

async function deletePost(index) {
    await fetch(`http://127.0.0.1:5000/posts/${index}`, {
        method: 'DELETE'
    });
    fetchPosts();
}

// Initial fetch to load posts on page load
fetchPosts();
