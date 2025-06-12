document.addEventListener('DOMContentLoaded', () => {
    const userData = JSON.parse(localStorage.getItem('user'));
    const authButton = document.getElementById('authButton');
    const userProfile = document.getElementById('userProfile');
    const usernameElement = document.getElementById('username');

    // Проверка авторизации
    if (userData?.isAuthenticated) {
        if (authButton) authButton.style.display = 'none';
        if (userProfile) userProfile.style.display = 'block';
        if (usernameElement && userData.name) {
            usernameElement.textContent = userData.name;
        }
    }
});
