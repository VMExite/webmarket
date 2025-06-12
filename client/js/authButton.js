document.addEventListener('DOMContentLoaded', () => {
    const authButton = document.getElementById('authButton');
    const user = JSON.parse(localStorage.getItem('user'));

    if (user && user.isAuthenticated) {
        authButton.textContent = 'Личный кабинет';
        authButton.href = '/client/pages/personal account.html';
        authButton.classList.remove('s1');
        const span = authButton.querySelector('span');
        if (span) span.remove();
    }
});