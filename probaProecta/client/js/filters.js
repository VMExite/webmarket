document.addEventListener('DOMContentLoaded', () => {
    const cards = Array.from(document.querySelectorAll('#коллекция .col-md-3, #коллекция .cadrcol'));
    const loadMoreBtn = document.getElementById('loadMoreBtn');
    const applyBtn = document.getElementById('applyFilters');
    let visibleCount = 8;
    let filteredCards = [];
    
    // Функция показа/скрытия карточек
    function updateVisibility() {
        let currentLimit = visibleCount;
        
        // сначала скрываем все карточки
        cards.forEach(card => card.style.display = 'none');
        
        filteredCards.slice(0, currentLimit).forEach(card => {
            card.style.display = 'block';
        });
        
        if (loadMoreBtn) {
            loadMoreBtn.style.display = filteredCards.length > currentLimit ? 'block' : 'none';
        }
    }
    
    //фильтрация
    function applyFilters() {
        const materials = Array.from(document.querySelectorAll('.material-filter:checked')).map(el => el.value);
        const types = Array.from(document.querySelectorAll('.type-filter:checked')).map(el => el.value);
        const priceRanges = Array.from(document.querySelectorAll('.price-filter:checked')).map(el => el.value);
        
        filteredCards = cards.filter(card => {
            const cardMaterial = card.dataset.material || '';
            const cardType = card.dataset.type || '';
            const cardPrice = parseInt(card.dataset.price) || 0;
            
            const materialMatch = materials.length === 0 || materials.includes(cardMaterial);
            const typeMatch = types.length === 0 || types.includes(cardType);
            
            let priceMatch = !priceRanges.length;
            if (!priceMatch) {
                priceMatch = priceRanges.some(range => {
                    if (range === '60000-1000000') {
                        return cardPrice >= 60000; // Особый случай для "60 000+"
                    }
                    const [min, max] = range.split('-').map(Number);
                    return cardPrice >= min && cardPrice <= max;
                });
            }
            
            return materialMatch && typeMatch && priceMatch;
        });
        
        visibleCount = 8;
        updateVisibility();
    }
    
    if (loadMoreBtn) {
        loadMoreBtn.addEventListener('click', () => {
            visibleCount += 8;
            updateVisibility();
        });
    }
    
    if (applyBtn) {
        applyBtn.addEventListener('click', applyFilters);
    }
    
    window.addEventListener('resize', updateVisibility);
    
    filteredCards = [...cards];
    updateVisibility();
});