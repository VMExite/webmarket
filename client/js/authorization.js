document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#loginForm');
    const errorBox = document.querySelector('#formError');
    const passwordInput = document.querySelector('#password');
    const eyeIcon = document.querySelector('.eye-icon i');

    // Переключение видимости пароля
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
            e.preventDefault();

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
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                    body: new URLSearchParams({
                        grant_type: 'password',
                        username: email,
                        password: password
                    })
                });

                const data = await response.json();

                if (!response.ok) {
                    if (data.detail === "LOGIN_BAD_CREDENTIALS") {
                        errorBox.innerHTML = 'Пользователь не найден или неверный пароль. <a href="/webmarket/client/pages/registration.html">Зарегистрироваться</a>';
                    } else {
                        errorBox.textContent = data.detail || `Ошибка авторизации (${response.status})`;
                    }
                    return;
                }

                console.log('Авторизация успешна:', data);

                // Сохраняем access_token в localStorage
                localStorage.setItem('authToken', data.access_token);

                // Перенаправляем на главную страницу
                window.location.href = '/webmarket/client/index.html';

            } catch (err) {
                console.error('Ошибка авторизации:', err);
                errorBox.textContent = 'Ошибка сети. Попробуйте снова';
            }
        });
    }
});
