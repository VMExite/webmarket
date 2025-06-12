document.addEventListener('DOMContentLoaded', () => {
    const logoutButton = document.getElementById('logoutButton');
    const userData = JSON.parse(localStorage.getItem('user'));

    if (logoutButton) {
        logoutButton.addEventListener('click', async () => {
            try {
                const response = await fetch('http://localhost:8000/api/v1/auth/logout', {
                    method: 'POST',
                    headers: {
                        'Authorization': `Bearer ${userData?.token}`,
                        'Content-Type': 'application/json'
                    }
                });

                // Очищаем localStorage в любом случае
                localStorage.removeItem('user');

                window.location.href = '/webmarket/client/index.html';
            } catch (err) {
                console.error('Ошибка сети:', err);
                localStorage.removeItem('user');
                window.location.href = '/webmarket/client/index.html';
            }
        });
    }
});
