document.addEventListener('DOMContentLoaded', function() {
    const gallery = document.getElementById('gallery');
    const sortButtons = document.querySelectorAll('[data-sort]');
    const loadMoreBtn = document.getElementById('loadMoreBtn');
    let currentVisible = 8;
    let currentSort = 'popularity';

    // Инициализация глобальной переменной для фильтрованных карточек
    if (!window.filteredCards) {
        window.filteredCards = Array.from(gallery.querySelectorAll('.cadrcol'));
    }

    //обновления видимости карточек
    function updateCardVisibility() {
        const visibleCount = getVisibleCount();
        
        window.filteredCards.forEach((card, index) => {
            card.style.display = index < visibleCount ? 'block' : 'none';
        });

        if (loadMoreBtn) {
            loadMoreBtn.style.display = window.filteredCards.length > visibleCount ? 'block' : 'none';
        }
    }

    // определения кол-ва видимых карточек
    function getVisibleCount() {
        const width = window.innerWidth;
        if (width > 989) return currentVisible;
        if (width > 659) return Math.floor(currentVisible / 2);
        return Math.floor(currentVisible / 4);
    }

    function applySort(sortType) {
        currentSort = sortType;
        
        switch(sortType) {
            case 'price':
                window.filteredCards.sort((a, b) => {
                    const priceA = parseInt(a.dataset.price) || 0;
                    const priceB = parseInt(b.dataset.price) || 0;
                    return priceA - priceB;
                });
                break;
                
            case 'new':
                window.filteredCards.sort((a, b) => {
                    const idA = parseInt(a.dataset.id) || 0;
                    const idB = parseInt(b.dataset.id) || 0;
                    return idB - idA;
                });
                break;
                
            case 'popularity':
                // Восстанавливаем исходный порядок (как в DOM)
                window.filteredCards = Array.from(gallery.querySelectorAll('.cadrcol'));
                break;
        }

        // Перерисовываем галерею
        renderGallery();
    }

    // функция перерисовки галереи
    function renderGallery() {
        // сохраняем текущую позицию прокрутки
        const scrollPosition = window.scrollY;
        
        // очищаем галерею
        gallery.innerHTML = '';
        
        // добавляем отсортированные карточки
        window.filteredCards.forEach(card => {
            gallery.appendChild(card);
        });
        
        // обновляем видимость
        updateCardVisibility();
        
        // Восстанавливаем позицию прокрутки
        window.scrollTo(0, scrollPosition);
    }

    // обработчики для кнопок сортировки
    sortButtons.forEach(button => {
        button.addEventListener('click', function() {
            // убираем активный класс у всех кнопок
            sortButtons.forEach(btn => btn.classList.remove('active'));
            
            // добавляем активный класс текущей кнопке
            this.classList.add('active');
            
            applySort(this.dataset.sort);
        });
    });

    if (loadMoreBtn) {
        loadMoreBtn.addEventListener('click', function() {
            currentVisible += 8;
            updateCardVisibility();
        });
    }

    function initGallery() {
        // активируем сортировку по популярности по умолчанию
        const defaultSortBtn = document.querySelector('[data-sort="popularity"]');
        if (defaultSortBtn) {
            defaultSortBtn.classList.add('active');
            applySort('popularity');
        }
        
        // Обновляем видимость при изменении размера окна
        window.addEventListener('resize', updateCardVisibility);
    }

    initGallery();

    //обработчик события для кнопки стрелочка
    document.getElementById('sortButton').addEventListener('click', function() {
        const icon = this.querySelector('.sort-icon');
        icon.classList.toggle('rotated');
    });
    
});











