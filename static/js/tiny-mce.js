function wrapTablesInTinyMCE() {
    const content = document.querySelector('.tiny-mce-content-detailed');
    if (!content) return;
  
    const tables = content.querySelectorAll('table');
    tables.forEach(table => {
      if (!table.parentElement.classList.contains('table-wrapper')) {
        const wrapper = document.createElement('div');
        wrapper.className = 'table-wrapper';
        table.parentNode.insertBefore(wrapper, table);
        wrapper.appendChild(table);
      }
    });
  }
  
  // Run it when DOM is loaded
  document.addEventListener("DOMContentLoaded", wrapTablesInTinyMCE);
  