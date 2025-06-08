document.addEventListener('DOMContentLoaded', async () => {
    const form = document.querySelector('#registrationForm');
    const errorBox = document.querySelector('#formError');

    // тображения/скрытия пароля
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
            e.preventDefault();

            const firstName = form.querySelector('#firstName').value.trim();
            const email = form.querySelector('#email').value.trim();
            const password = form.querySelector('#password').value.trim();

            if (!firstName || !email || !password) {
                errorBox.textContent = "Нужно заполнить все поля";
                return;
            }
            errorBox.textContent = '';

            try {
                const response = await fetch(`http://localhost:8000/api/v1/register/register`, { 
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        login: firstName,
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
                console.log('Регистрация прошла успешно', data);

                // сохраняем данные пользователя
                localStorage.setItem('user', JSON.stringify({
                    isAuthenticated: true,
                    token: data.token || null, // добавляем токен ; проверить наличие на сервере
                    name: firstName,
                    email: email
                }));

                // Перенаправляем на главную
                window.location.href = '/client/index.html';

            } catch (err) {
                errorBox.textContent = 'Произошла ошибка при регистрации. Попробуйте снова';
                console.error('Ошибка регистрации:', err);
            }
        });
    }
});