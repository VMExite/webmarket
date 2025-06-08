document.addEventListener('DOMContentLoaded', () => {
    const userData = JSON.parse(localStorage.getItem('user'));
    const authButton = document.getElementById('authButton');
    const userProfile = document.getElementById('userProfile');
    const logoutBtn = document.getElementById('logoutBtn');
    const usernameElement = document.getElementById('username');

    // Проверка авторизации
    if (userData?.isAuthenticated) {
        authButton.style.display = 'none';
        userProfile.style.display = 'block';
        if (usernameElement && userData.name) {
            usernameElement.textContent = userData.name;
        }
    }

    // Обработка выхода
    if (logoutBtn) {
        logoutBtn.addEventListener('click', async (e) => {
            e.preventDefault();
            
            try {
                const response = await fetch('http://localhost:8000/api/v1/auth/logout', {
                    method: 'POST',
                    headers: {
                        'Authorization': `Bearer ${userData.token}`,
                        'Content-Type': 'application/json'
                    }
                });

                if (response.ok) {
                    localStorage.removeItem('user');
                    window.location.href = '/client/index.html';
                } else {
                    console.error('Ошибка выхода:', await response.text());
                }
            } catch (err) {
                console.error('Ошибка сети:', err);
                // очищаем localStorage даже если бэкенд недоступен
                localStorage.removeItem('user');
                window.location.reload();
            }
        });
    }
});