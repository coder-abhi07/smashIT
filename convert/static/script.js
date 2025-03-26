document.addEventListener('DOMContentLoaded', function() {
  

  lucide.createIcons();
  const Authform = document.querySelector(".auth-form form");
  
  
    let errorToastShown = false; // flag to prevent duplicate toasts
  
    if (Authform) {
      Authform.addEventListener("submit", async (event) => {
         
          
          // If a toast is already showing, exit early
          if (errorToastShown) return;
          
          // Optionally, wait a tick (or await any other asynchronous tasks)
          await new Promise(resolve => setTimeout(resolve, 0));
          
          const fa = document.getElementsByClassName("tailwind");
          const hasError = [...fa].some(el => el.innerText.trim().length > 0);
          
          if (hasError) {
              errorToastShown = true;
              console.log("error toast");
              showToast('Fix The Errors', 'error');
              // Reset the flag after a short delay if needed
              setTimeout(() => {
                  errorToastShown = false;
              }, 1000);
          }
      });
  } 
 

  const themeToggleBtn = document.getElementsByClassName('theme-toggle')[0];
  
  function getThemePreference() {
    if (localStorage.getItem('theme') === 'dark' || 
      (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      return 'dark';
    }
    return 'light';
  }
  
  function setTheme(theme) {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }
  }
  
  // Set initial theme
  setTheme(getThemePreference());
  
  // Toggle theme when button is clicked
  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', function() {
      const currentTheme = document.documentElement.classList.contains('dark') ? 'dark' : 'light';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      setTheme(newTheme);
      showToast(`${newTheme.charAt(0).toUpperCase() + newTheme.slice(1)} mode activated`, 'info');
    });
  }
  
  // Listen for changes in system preference
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    if (!localStorage.getItem('theme')) { // Only if the user hasn't manually set a preference
      setTheme(e.matches ? 'dark' : 'light');
    }
  });
  
  // Mobile Menu Toggle
  const mobileMenuBtn = document.querySelector('.mobile-menu-button');
  const mobileMenu = document.querySelector('.mobile-menu');
  
  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', function() {
      mobileMenu.style.display = mobileMenu.style.display === 'block' ? 'none' : 'block';
    });

    const themeToggleBtn2 = document.getElementById('themeToggle2');
    if (themeToggleBtn2) {
      themeToggleBtn2.addEventListener('click', function() {
        const currentTheme = document.documentElement.classList.contains('dark') ? 'dark' : 'light';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
        showToast(`${newTheme.charAt(0).toUpperCase() + newTheme.slice(1)} mode activated`, 'info');
      });
    }
    
    // User Dropdown Toggle
  const userMenuBtn2 = document.getElementById('userMenuButton2');
  const userDropdown2 = document.getElementById('userDropdown2');
  
  if (userMenuBtn2 && userDropdown2) {
    userMenuBtn2.addEventListener('click', function(event) {
      event.stopPropagation();
      userDropdown2.classList.toggle('active');
    });
    
    // Close dropdown when clicking outside
    document.addEventListener('click', function(event) {
      if (!userMenuBtn2.contains(event.target) && !userDropdown2.contains(event.target)) {
        userDropdown2.classList.remove('active');
      }
    });
  }
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
      if (!mobileMenuBtn.contains(event.target) && !mobileMenu.contains(event.target)) {
        mobileMenu.style.display = 'none';
      }
    });
  }
  
  // User Dropdown Toggle
  const userMenuBtn = document.getElementById('userMenuButton');
  const userDropdown = document.getElementById('userDropdown');
  
  if (userMenuBtn && userDropdown) {
    userMenuBtn.addEventListener('click', function(event) {
      event.stopPropagation();
      userDropdown.classList.toggle('active');
    });
    
    // Close dropdown when clicking outside
    document.addEventListener('click', function(event) {
      if (!userMenuBtn.contains(event.target) && !userDropdown.contains(event.target)) {
        userDropdown.classList.remove('active');
      }
    });
  }


  
  // Logout Button
  const logoutBtn = document.getElementById('logoutButton');
  const mobileLogoutBtn = document.querySelector('.logout-button');
  
  function handleLogout() {
    showToast('Successfully logged out', 'success');
    setTimeout(() => {
      window.location.href = '/';
    }, 1500);
  }
  
  if (logoutBtn) {
    logoutBtn.addEventListener('click', handleLogout);
  }
  
  if (mobileLogoutBtn) {
    mobileLogoutBtn.addEventListener('click', handleLogout);
  }
  
  
  // // Authentication Forms
  // const loginForm = document.getElementById('loginForm');
  // const registerForm = document.getElementById('registerForm');
    
  // if (loginForm) {
  //   loginForm.addEventListener('submit', function(event) {
  //     event.preventDefault();
  //     const username = document.getElementById('username').value;
  //     const password = document.getElementById('password').value;
      
  //     if (!username || !password) {
  //       showToast('Please fill in all fields', 'error');
  //       return;
  //     }
      
  //     // Simulate login process
  //     showToast('Logging in...', 'info');
      
  //     setTimeout(() => {
  //       showToast('Login successful!', 'success');
  //       setTimeout(() => {
  //         window.location.href = '/';
  //       }, 1000);
  //     }, 1500);
  //   });
  // }
  
  // if (registerForm) {
  //   registerForm.addEventListener('submit', function(event) {
  //     event.preventDefault();
  //     const username = document.getElementById('username').value;
  //     const password1 = document.getElementById('password1').value;
  //     const password2 = document.getElementById('password2').value;
  //     const terms = document.getElementById('terms').checked;
      
  //     if (!username || !password1) {
  //       showToast('Please fill in all fields', 'error');
  //       return;
  //     }
      
  //     if (!terms) {
  //       showToast('Please accept the Terms of Service', 'error');
  //       return;
  //     }
  //     // Password validation
  //     if (password1.length < 8 || !/[A-Z]/.test(password1) || !/[0-9]/.test(password1)) {
  //       
  //       return;
  //     }
      
  //     // Simulate registration process
  //     showToast('Creating your account...', 'info');
      
  //     setTimeout(() => {
  //       showToast('Account created successfully!', 'success');
  //       setTimeout(() => {
  //         console.log("kuch nhi")
  //       }, 1000);
  //     }, 1500);
  //   });
  // }

  //dashboard

    // File upload functionality
    const uploadArea = document.getElementById('upload-area');
    const fileInput = document.getElementById('file-input');
    const browseBtn = document.getElementById('browse-btn');
    const filesContainer = document.getElementById('files-container');
    const filesList = document.getElementById('files-list');
    const fileCount = document.getElementById('file-count');
    const clearBtn = document.getElementById('clear-btn');
    const analyzeBtn = document.getElementById('analyze-btn');
    const progressContainer = document.getElementById('progress-container');
    const progressValue = document.getElementById('progress-value');
    const progressPercentage = document.getElementById('progress-percentage');
    const uploadHeading = document.getElementById('upload-heading');

    // Set logo from provided image
    // const logoImg = document.getElementById('logo-img');
    // logoImg.src = document.querySelector('img[alt="Question Paper Analyzer Logo"]').src;

    // Handle file selection
    // browseBtn.addEventListener('click', () => {
    //   fileInput.click();
    // });
    browseBtn.addEventListener("click", function (event) {
      // event.preventDefault(); // Prevent any unintended default behavior
      fileInput.click();
  });

    // Handle drag and drop
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
      uploadArea.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
      e.preventDefault();
      e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
      uploadArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
      uploadArea.addEventListener(eventName, unhighlight, false);
    });

    function highlight() {
      uploadArea.classList.add('drag-active');
      uploadHeading.textContent = 'Drop files here';
    }

    function unhighlight() {
      uploadArea.classList.remove('drag-active');
      uploadHeading.textContent = 'Upload question papers';
    }

    uploadArea.addEventListener('drop', handleDrop, false);

    function handleDrop(e) {
      const dt = e.dataTransfer;
      const files = dt.files;
      handleFiles(files);
    }

    fileInput.addEventListener('change', function() {
      handleFiles(this.files);
    });

    function handleFiles(files) {
      if (files.length === 0) return;
      
      const validFiles = Array.from(files).filter(file => {
        const fileType = file.type;
        return fileType === 'image/png' || fileType === 'image/jpeg' || fileType === 'application/pdf';
      });
      
      if (validFiles.length === 0) {
        alert('No valid files selected. Please upload PNG, JPEG, or PDF files.');
        return;
      }
      
      // Show progress
      progressContainer.style.display = 'block';
      
      // Simulate upload progress
      let progress = 0;
      const interval = setInterval(() => {
        progress += 20;
        if (progress >= 100) {
          clearInterval(interval);
          setTimeout(() => {
            progressContainer.style.display = 'none';
            displayFiles(validFiles);
          }, 500);
        }
        progressValue.style.width = `${progress}%`;
        progressPercentage.textContent = `${progress}%`;
      }, 150);
    }


    function displayFiles(files) {
      filesContainer.style.display = 'block';
      
      for (const file of files) {
        const fileItem = document.createElement('div');
        fileItem.className = 'file-item';
        
        const fileIcon = file.type.startsWith('image/') ? 
          '<i data-lucide="image" size="20"></i>' : 
          '<i data-lucide="file-text" size="20"></i>';
        
        const fileSize = formatFileSize(file.size);
        
        fileItem.innerHTML = `
          <div class="file-info">
            <div class="file-icon">${fileIcon}</div>
            <div class="file-name">
              ${file.name}
              <span class="file-size">(${fileSize})</span>
            </div>
          </div>
          <div class="file-actions">
            <button class="btn-icon btn-danger remove-file" aria-label="Remove file">
              <i data-lucide="x" size="16"></i>
            </button>
          </div>
        `;
        
        filesList.appendChild(fileItem);
      }
      
      // Update file count
      const currentCount = filesList.querySelectorAll('.file-item').length;
      fileCount.textContent = currentCount;
      
      // Initialize remove buttons
      lucide.createIcons();
      
      const removeButtons = document.querySelectorAll('.remove-file');
      removeButtons.forEach(button => {
        button.addEventListener('click', function() {
          const fileItem = this.closest('.file-item');
          fileItem.remove();
          
          const newCount = filesList.querySelectorAll('.file-item').length;
          fileCount.textContent = newCount;
          
          if (newCount === 0) {
            filesContainer.style.display = 'none';
          }
        });
      });
    }

    // Clear all files
    clearBtn.addEventListener('click', () => {
      filesList.innerHTML = '';
      fileCount.textContent = '0';
      filesContainer.style.display = 'none';
    });

    // Analyze files (simulate)
    analyzeBtn.addEventListener('click', (event) => {
      const count = filesList.querySelectorAll('.file-item').length;
      if (count === 0) {
        alert('No files to analyze. Please upload at least one file.');
        
        return;
      }
      
      event.preventDefault(); // Stop form submission
    
      // Change button to loading state
      analyzeBtn.disabled = true;
      analyzeBtn.innerHTML = `
        <i data-lucide="loader-2" size="16" class="animate-spin"></i>
        Analyzing...
      `;
      lucide.createIcons();
      
      // Simulate analysis
      setTimeout(() => {
        showToast('please wait...', 'info');
        analyzeBtn.disabled = false;
        analyzeBtn.innerHTML = `
          <i data-lucide="scan-search" size="16"></i>
          Analyze
        `;
        lucide.createIcons();
        
       
       
      }, 2000);
    });

    // Helper function for file size formatting
    function formatFileSize(bytes) {
      if (bytes === 0) return '0 Bytes';
      
      const k = 1024;
      const sizes = ['Bytes', 'KB', 'MB', 'GB'];
      const i = Math.floor(Math.log(bytes) / Math.log(k));
      
      return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }

   

  // Toast Notifications
  function showToast(message, type = 'info') {
    const toastContainer = document.getElementById('toast-container');
    if (!toastContainer) return;
    
    const toast = document.createElement('div');
    toast.classList.add('toast', type);
    
    let iconSvg;
    let title;
    
    switch (type) {
      case 'success':
        iconSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>';
        title = 'Success';
        break;
      case 'error':
        iconSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>';
        title = 'Error';
        break;
      case 'warning':
        iconSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"></path><path d="M12 9v4"></path><path d="M12 17h.01"></path></svg>';
        title = 'Warning';
        break;
      default:
        iconSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>';
        title = 'Info';
    }
    
    toast.innerHTML = `
      <div class="toast-icon">${iconSvg}</div>
      <div class="toast-content">
        <div class="toast-title">${title}</div>
        <div class="toast-message">${message}</div>
      </div>
      <button class="toast-close">
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </button>
    `;
    
    toastContainer.appendChild(toast);
    
    // Add event listener to close button
    const closeBtn = toast.querySelector('.toast-close');
    if (closeBtn) {
      closeBtn.addEventListener('click', function() {
        toast.style.animation = 'slide-out 0.3s ease-out forwards';
        setTimeout(() => {
          toastContainer.removeChild(toast);
        }, 300);
      });
    }
    
    // Auto remove toast after 5 seconds
    setTimeout(() => {
      if (toastContainer.contains(toast)) {
        toast.style.animation = 'slide-out 0.3s ease-out forwards';
        setTimeout(() => {
          if (toastContainer.contains(toast)) {
            toastContainer.removeChild(toast);
          }
        }, 300);
      }
    }, 900);
  }
    

});


  

