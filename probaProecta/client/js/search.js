
/*
export function debounce(func, timeout = 650) {
    let timer;
    return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => { func.apply(this, args); }, timeout);
    };
}

export function setupSearch() {
    document.addEventListener("DOMContentLoaded", () => {
        const searchInput = document.querySelector('#searchInput');
        if (!searchInput) return;

        const filterCards = (query) => {
            const cards = document.querySelectorAll('#коллекция .col-md-3');
            let hasMatches = false;
            
            cards.forEach(card => {
                const text = card.innerText.toLowerCase();
                const isMatch = text.includes(query);
                card.style.display = isMatch ? '' : 'none';
                if (isMatch) {
                    hasMatches = true;
                }
            });
        };

        //с помощью enter
        /*searchInput.addEventListener('keyup', (e) => {
            if (e.key === 'Enter') {
                const query = e.target.value.toLowerCase().trim();
                filterCards(query);
                
                document.getElementById('коллекция').scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });*/

        /*searchInput.addEventListener('input', debounce((e) => {
            const query = e.target.value.toLowerCase().trim();
            filterCards(query);
            
            document.getElementById('коллекция').scrollIntoView({
                behavior: 'smooth'
            });
        }));
    });
};
setupSearch();

*/




//с учетом кнопки Показать еще
export function debounce(func, timeout = 650) {
    let timer;
    return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => { func.apply(this, args); }, timeout);
    };
}

// глоб. перемен. для хранения отфильтрованных карточек
window.filteredCards = [];

export function setupSearch() {
    document.addEventListener("DOMContentLoaded", () => {
        const searchInput = document.querySelector('#searchInput');
        if (!searchInput) return;

        let currentQuery = '';
        let currentVisible = 8;

        const filterCards = (query) => {
            currentQuery = query.toLowerCase().trim();
            const allCards = Array.from(document.querySelectorAll('#коллекция .col-md-3, #коллекция .cadrcol'));
            
            // фильтруем
            window.filteredCards = allCards.filter(card => {
                const text = card.innerText.toLowerCase();
                return currentQuery === '' || text.includes(currentQuery);
            });

            updateCardVisibility();
        };

        function updateCardVisibility() {
            const visibleCount = getVisibleCount();
            
            //скрываем все карточки
            document.querySelectorAll('#коллекция .col-md-3, #коллекция .cadrcol').forEach(card => {
                card.style.display = 'none';
            });
            
            // показываем только отфильтрованные карточки в пределах видимости
            window.filteredCards.forEach((card, index) => {
                card.style.display = index < visibleCount ? 'block' : 'none';
            });

            // видимость кнопки
            const loadMoreBtn = document.getElementById('loadMoreBtn');
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

        searchInput.addEventListener('input', debounce((e) => {
            currentVisible = 8; // сбрасываем счетчик при новом поиске
            filterCards(e.target.value);
            document.getElementById('коллекция').scrollIntoView({ behavior: 'smooth' });
        }));
    });
}
setupSearch();