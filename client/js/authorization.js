document.addEventListener('DOMContentLoaded', async () => {
    const form = document.querySelector('#loginForm');
    const errorBox = document.querySelector('#formError');

    // отображения/скрытия пароля
    const passwordInput = document.querySelector('#password');
    const eyeIcon = document.querySelector('.eye-icon i');

    if (passwordInput && eyeIcon) {
        document.querySelector('.eye-icon').addEventListener('click', () => {
            const isPassword = passwordInput.type === 'password';
            passwordInput.type = isPassword ? 'text' : 'password';
            eyeIcon.classList.toggle('bi-eye');
            eyeIcon.classList.toggle('bi-eye-slash');
        });
    }

    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault(); // отменяем перезагрузку страницы

            const email = form.querySelector('#email').value.trim();
            const password = form.querySelector('#password').value.trim();

            if (!email || !password) {
                errorBox.textContent = "Нужно заполнить все поля";
                return;
            }
            errorBox.textContent = '';

            try {
                const response = await fetch(`http://localhost:8000/api/v1/auth/login`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        email: email,
                        password: password,
                    })
                });
                
                if (!response.ok) {
                    const errorData = await response.json();
                    errorBox.textContent = errorData.message || `Ошибка: ${response.status}`;
                    return;
                }

                const data = await response.json();
                console.log('Авторизация прошла успешно', data);

                // сохраняем данные пользователя
                localStorage.setItem('user', JSON.stringify({
                    isAuthenticated: true,
                    token: data.token, // сохраняем токен; проверить наличие
                    name: data.user?.name,
                    email: email
                }));

                window.location.href = '/client/index.html';

            } catch (err) {
                errorBox.textContent = 'Произошла ошибка при авторизации. Попробуйте снова';
                console.error(err);
            }
        });
    }

    // После успешного входа
    const data = await response.json();

    localStorage.setItem('user', JSON.stringify({
        isAuthenticated: true,
        token: data.token, // Сохраняем токен
        name: data.user?.name,
        email: email
    }));

    window.location.href = '/client/index.html';
    
});