document.addEventListener('DOMContentLoaded', async () => {
    const form = document.getElementById('registrationForm');
    const errorBox = document.getElementById('formError');
    const submitBtn = document.getElementById('submitBtn');
    const passwordInput = document.getElementById('password');
    const eyeIcon = document.querySelector('.eye-icon i');

    // откр/закр глаз
    if (passwordInput && eyeIcon) {
        document.querySelector('.eye-icon').addEventListener('click', () => {
            const isPassword = passwordInput.type === 'password';
            passwordInput.type = isPassword ? 'text' : 'password';
            eyeIcon.classList.toggle('bi-eye');
            eyeIcon.classList.toggle('bi-eye-slash');
        });
    }

    // валидация email
    function isValidEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            submitBtn.disabled = true;
            errorBox.textContent = '';

            const login = form.querySelector('#login').value.trim();
            const email = form.querySelector('#email').value.trim();
            const password = form.querySelector('#password').value.trim();

            if (!login || !email || !password) {
                errorBox.textContent = "Все поля обязательны для заполнения";
                submitBtn.disabled = false;
                return;
            }

            if (!isValidEmail(email)) {
                errorBox.textContent = "Введите корректный email";
                submitBtn.disabled = false;
                return;
            }

            if (password.length < 6) {
                errorBox.textContent = "Пароль должен содержать минимум 6 символов";
                submitBtn.disabled = false;
                return;
            }

            try {
                const response = await fetch('http://localhost:8000/api/v1/register/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        login: login,
                        email: email,
                        password: password,
                        is_active: true,
                        is_superuser: false,
                        is_verified: false
                    })
                });

                const data = await response.json();

                if (!response.ok) {
                    throw new Error(data.detail || 'Ошибка регистрации');
                }

                // успешная регистрация
                localStorage.setItem('user', JSON.stringify({
                    isAuthenticated: true,
                    userId: data.id,
                    email: data.email,
                    login: data.login
                }));

                window.location.href = '/webmarket/client/index.html';

            } catch (error) {
                console.error('Ошибка регистрации:', error);
                errorBox.textContent = error.message || 'Произошла ошибка при регистрации';
            } finally {
                submitBtn.disabled = false;
            }
        });
    }
});