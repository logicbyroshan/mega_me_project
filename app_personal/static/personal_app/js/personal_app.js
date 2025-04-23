function copyCode(btn) {
    const code = btn.nextElementSibling.querySelector('code');
    const text = code.innerText;
  
    navigator.clipboard.writeText(text).then(() => {
      btn.innerText = "Copied!";
      setTimeout(() => {
        btn.innerText = "Copy";
      }, 1500);
    }).catch(err => {
      console.error("Copy failed", err);
      btn.innerText = "Error";
    });
  }