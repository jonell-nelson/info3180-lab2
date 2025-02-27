document.addEventListener('DOMContentLoaded', function () {
    const followButton = document.querySelector('.follow-button');

    if (followButton) {
        followButton.addEventListener('click', function () {
            if (followButton.textContent === 'Follow') {
                followButton.textContent = 'Following';
                followButton.style.backgroundColor = '#28a745'; // Green color
            } else {
                followButton.textContent = 'Follow';
                followButton.style.backgroundColor = '#007bff'; // Blue color
            }
        });
    }
});