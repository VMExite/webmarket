document.addEventListener("DOMContentLoaded", () => {
    const cardsContainer = document.querySelector(".row.text-center");
    const sortButtons = document.querySelectorAll("[data-sort]");

    sortButtons.forEach(button => {
        button.addEventListener("click", () => {
        const sortType = button.dataset.sort;
        const cards = Array.from(cardsContainer.children);

        let sortedCards = cards;

        if (sortType === "price") {
            sortedCards = cards.sort((a, b) => {
            return getPrice(a) - getPrice(b);
            });
        } else if (sortType === "new") {
            sortedCards = cards.sort((a, b) => {
            return getId(b) - getId(a); // больше id = новее
            });
        } else if (sortType === "popularity") {
            sortedCards = cards.reverse(); // просто переворачиваю,нет логики
        }

        // перерисовываем карточки в нужном порядке
        cardsContainer.innerHTML = "";
        sortedCards.forEach(card => cardsContainer.appendChild(card));
        });
    });

    function getPrice(card) {
        return parseInt(card.dataset.price || 0);
    }

    function getId(card) {
        return parseInt(card.dataset.id || 0);
    }
});
