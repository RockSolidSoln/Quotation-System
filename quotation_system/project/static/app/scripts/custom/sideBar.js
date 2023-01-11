// JavaScript for toggling the sidebar on and off
var button = document.getElementById('sidebar-button');
var sidebar = document.getElementById('sidebar');
var main = document.getElementById('main');

button.addEventListener('click', function() {
  if (sidebar.style.display === 'block') {
    sidebar.style.display = 'none';
    button.classList.remove('clicked');
    main.style.marginLeft = '0px';
    
  } else {
    sidebar.style.display = 'block';
    button.classList.add('clicked');
    main.style.marginLeft = '120px';
    
  }
});