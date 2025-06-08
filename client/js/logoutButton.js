document.addEventListener('DOMContentLoaded', () => {
    const user = JSON.parse(localStorage.getItem('user'));
    const logoutButton = document.getElementById('logoutButton');

    if (!user || !user.isAuthenticated) {
        window.location.href = '/client/pages/registration.html';
        return;
    }

    logoutButton.addEventListener('click', () => {
        localStorage.removeItem('user');
        window.location.href = '/client/index.html';
    });
});