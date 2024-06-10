document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const toggleBtn = document.getElementById('toggle-btn');
    const menuItems = document.querySelectorAll('.sidenav_menuitem_button');

    toggleBtn.addEventListener('click', function() {
        sidebar.classList.toggle('collapsed');

        menuItems.forEach(item => {
            if (sidebar.classList.contains('collapsed')) {
                item.style.backgroundImage = `url(${item.getAttribute('data-icon')})`;
            } else {
                item.style.backgroundImage = 'none';
            }
        });
    });

    // Collapse sidebar by default on smaller screens
    if (window.innerWidth <= 768) {
        sidebar.classList.add('collapsed');
        menuItems.forEach(item => {
            item.style.backgroundImage = `url(${item.getAttribute('data-icon')})`;
        });
    }
});