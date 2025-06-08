//учитывает фильтр поиска
const loadMoreBtn = document.getElementById('loadMoreBtn');
let currentVisible = 8;

function updateCardVisibility() {
    const visibleCount = getVisibleCount();
    
    // скрываем все карточки
    document.querySelectorAll('#коллекция .col-md-3, #коллекция .cadrcol').forEach(card => {
        card.style.display = 'none';
    });
    
    // показываем только отфильтрованные в пределах видимости
    window.filteredCards.forEach((card, index) => {
        card.style.display = index < visibleCount ? 'block' : 'none';
    });

    if (loadMoreBtn) {
        loadMoreBtn.style.display = window.filteredCards.length > visibleCount ? 'block' : 'none';
    }
}

function getVisibleCount() {
    const width = window.innerWidth;
    if (width > 989) return currentVisible;
    if (width > 659) return Math.floor(currentVisible / 2);
    return Math.floor(currentVisible / 4);
}

if (loadMoreBtn) {
    loadMoreBtn.addEventListener('click', () => {
        currentVisible += 8;
        updateCardVisibility();
    });
}

function initGallery() {
    if (!window.filteredCards || window.filteredCards.length === 0) {
        window.filteredCards = Array.from(document.querySelectorAll('#коллекция .col-md-3, #коллекция .cadrcol'));
    }
    updateCardVisibility();
    window.addEventListener('resize', updateCardVisibility);
}

document.addEventListener('DOMContentLoaded', initGallery);




//фильтр для 3 коллекций
document.addEventListener('DOMContentLoaded', function() {
    // обработчики кликов на коллекции
    document.querySelector('.gold-collection').addEventListener('click', function(e) {
        e.preventDefault();
        applyCollectionFilter('золото');
    });

    document.querySelector('.diamond-collection').addEventListener('click', function(e) {
        e.preventDefault();
        applyCollectionFilter('бриллиант');
    });

    document.querySelector('.platinum-collection').addEventListener('click', function(e) {
        e.preventDefault();
        applyCollectionFilter('платина');
    });

    // функция для применения фильтра и скролла
    function applyCollectionFilter(material) {
        //прокрутка к разделу коллекции
        const collectionSection = document.getElementById('коллекция');
        collectionSection.scrollIntoView({ behavior: 'smooth' });

        // сброс предыдущих фильтров
        document.querySelectorAll('.material-filter').forEach(checkbox => {
            checkbox.checked = false;
        });

        // установка нужного фильтра
        const materialIdMap = {
            'золото': 'gold',
            'бриллиант': 'diamond',
            'платина': 'platinum'
        };

        const checkboxId = materialIdMap[material];
        if (checkboxId) {
            const checkbox = document.getElementById(checkboxId);
            if (checkbox) {
                checkbox.checked = true;
                
                // имитация клика на кнопку "Применить"
                setTimeout(() => {
                    document.getElementById('applyFilters').click();
                }, 500);
            }
        }
    }
});




//фильтр для категорий коллекций
// Обработчики для категорий
document.querySelectorAll('.icon-item[data-type]').forEach(item => {
    item.addEventListener('click', function(e) {
        e.preventDefault();
        const type = this.getAttribute('data-type');
        applyCategoryFilter(type);
    });
});

// Функция для применения фильтра категории
function applyCategoryFilter(type) {
    // 1. Прокрутка к разделу коллекции
    const collectionSection = document.getElementById('коллекция');
    if (collectionSection) {
        collectionSection.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }

    // 2. Находим все чекбоксы типа
    const typeCheckboxes = document.querySelectorAll('.type-filter');
    if (!typeCheckboxes.length) return;

    // 3. Сброс всех фильтров типа
    typeCheckboxes.forEach(checkbox => {
        checkbox.checked = false;
    });

    // 4. Находим нужный чекбокс
    let targetCheckbox = null;
    typeCheckboxes.forEach(checkbox => {
        if (checkbox.value === type) {
            targetCheckbox = checkbox;
        }
    });

    // 5. Если чекбокс найден - отмечаем его
    if (targetCheckbox) {
        targetCheckbox.checked = true;
        
        // 6. Находим кнопку применения фильтров
        const applyButton = document.getElementById('applyFilters');
        if (applyButton) {
            // 7. Даем время для скролла перед применением фильтра
            setTimeout(() => {
                applyButton.click();
            }, 800);
        }
    }
}