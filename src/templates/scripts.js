// ConnectHear Operations Portal - JavaScript

// Global state
// Note: OPERATIONS_DATA is embedded inline by the generator
let currentWorkstream = null;
let searchDebounceTimer = null;

// Utility Functions
function debounce(func, delay) {
  return function(...args) {
    clearTimeout(searchDebounceTimer);
    searchDebounceTimer = setTimeout(() => func.apply(this, args), delay);
  };
}

function generateId(text) {
  return text.toLowerCase()
    .replace(/[🔷📍✅]/g, '')
    .replace(/[^\w\s-]/g, '')
    .replace(/[-\s]+/g, '-')
    .trim()
    .replace(/^-+|-+$/g, '');
}

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Navigation Functions
function toggleDepartment(deptId) {
  const deptElement = document.querySelector(`[data-dept-id="${deptId}"]`);
  if (!deptElement) return;

  const areasContainer = deptElement.querySelector('.nav-areas');
  const toggleIcon = deptElement.querySelector('.toggle-icon');

  if (areasContainer.classList.contains('expanded')) {
    areasContainer.classList.remove('expanded');
    toggleIcon.classList.remove('expanded');
  } else {
    areasContainer.classList.add('expanded');
    toggleIcon.classList.add('expanded');
  }
}

function toggleArea(areaId) {
  const areaElement = document.querySelector(`[data-area-id="${areaId}"]`);
  if (!areaElement) return;

  const workstreamsContainer = areaElement.querySelector('.nav-workstreams');
  const toggleIcon = areaElement.querySelector('.toggle-icon');

  if (workstreamsContainer.classList.contains('expanded')) {
    workstreamsContainer.classList.remove('expanded');
    toggleIcon.classList.remove('expanded');
  } else {
    workstreamsContainer.classList.add('expanded');
    toggleIcon.classList.add('expanded');
  }
}

function showWorkstream(deptId, areaId, wsId) {
  // Hide all workstream sections
  document.querySelectorAll('.workstream-section').forEach(section => {
    section.classList.remove('active');
  });

  // Hide home section
  const homeSection = document.getElementById('home-section');
  if (homeSection) {
    homeSection.classList.add('hidden');
  }

  // Show selected workstream
  const workstreamSection = document.getElementById(`ws-${deptId}-${areaId}-${wsId}`);
  if (workstreamSection) {
    workstreamSection.classList.add('active');
  }

  // Update active state in navigation
  document.querySelectorAll('.nav-workstream-link').forEach(link => {
    link.classList.remove('active');
  });
  const activeLink = document.querySelector(`[data-workstream-id="${deptId}-${areaId}-${wsId}"]`);
  if (activeLink) {
    activeLink.classList.add('active');

    // Ensure parent area and department are expanded
    const areaElement = activeLink.closest('[data-area-id]');
    const deptElement = activeLink.closest('[data-dept-id]');

    if (areaElement) {
      const areasContainer = areaElement.querySelector('.nav-workstreams');
      const toggleIcon = areaElement.querySelector('.toggle-icon');
      if (areasContainer) areasContainer.classList.add('expanded');
      if (toggleIcon) toggleIcon.classList.add('expanded');
    }

    if (deptElement) {
      const areasContainer = deptElement.querySelector('.nav-areas');
      const toggleIcon = deptElement.querySelector('.toggle-icon');
      if (areasContainer) areasContainer.classList.add('expanded');
      if (toggleIcon) toggleIcon.classList.add('expanded');
    }

    // Scroll link into view in sidebar
    activeLink.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  // Update breadcrumbs
  updateBreadcrumbs(deptId, areaId, wsId);

  // Scroll content to top
  scrollToTop();

  // Update current workstream
  currentWorkstream = { deptId, areaId, wsId };
}

function showHome() {
  // Hide all workstream sections
  document.querySelectorAll('.workstream-section').forEach(section => {
    section.classList.remove('active');
  });

  // Show home section
  const homeSection = document.getElementById('home-section');
  if (homeSection) {
    homeSection.classList.remove('hidden');
  }

  // Clear active navigation
  document.querySelectorAll('.nav-workstream-link').forEach(link => {
    link.classList.remove('active');
  });

  // Clear breadcrumbs
  const breadcrumbs = document.getElementById('breadcrumbs');
  if (breadcrumbs) {
    breadcrumbs.innerHTML = '<div class="breadcrumb-item">Home</div>';
  }

  scrollToTop();
  currentWorkstream = null;
}

function updateBreadcrumbs(deptId, areaId, wsId) {
  const breadcrumbs = document.getElementById('breadcrumbs');
  if (!breadcrumbs || !OPERATIONS_DATA) return;

  // Find the department, area, and workstream
  const dept = OPERATIONS_DATA.departments.find(d => d.id === deptId);
  if (!dept) return;

  const area = dept.areas.find(a => a.id === areaId);
  if (!area) return;

  const ws = area.workstreams.find(w => w.id === wsId);
  if (!ws) return;

  // Build breadcrumb HTML
  const breadcrumbHTML = `
    <div class="breadcrumb-item">
      <a href="#" onclick="showHome(); return false;">Home</a>
    </div>
    <span class="breadcrumb-separator">›</span>
    <div class="breadcrumb-item">
      ${dept.emoji} ${dept.name}
    </div>
    <span class="breadcrumb-separator">›</span>
    <div class="breadcrumb-item">
      ${area.emoji} ${area.name}
    </div>
    <span class="breadcrumb-separator">›</span>
    <div class="breadcrumb-item">
      <strong>${ws.name}</strong>
    </div>
  `;

  breadcrumbs.innerHTML = breadcrumbHTML;
}

// Search Functions
function initSearch() {
  const searchInput = document.getElementById('search-input');
  const searchClear = document.getElementById('search-clear');

  if (searchInput) {
    searchInput.addEventListener('input', debounce(performSearch, 300));
  }

  if (searchClear) {
    searchClear.addEventListener('click', clearSearch);
  }
}

function performSearch(event) {
  const query = event.target.value.trim().toLowerCase();

  if (!query) {
    clearSearch();
    return;
  }

  // Search across all content
  const results = [];

  OPERATIONS_DATA.departments.forEach(dept => {
    dept.areas.forEach(area => {
      area.workstreams.forEach(ws => {
        let score = 0;
        let matchedIn = [];

        // Search in workstream name (highest priority)
        if (ws.name.toLowerCase().includes(query)) {
          score += 10;
          matchedIn.push('name');
        }

        // Search in description
        if (ws.description && ws.description.toLowerCase().includes(query)) {
          score += 5;
          matchedIn.push('description');
        }

        // Search in frequency
        if (ws.frequency && ws.frequency.toLowerCase().includes(query)) {
          score += 3;
          matchedIn.push('frequency');
        }

        // Search in RACI roles
        if (ws.raci) {
          ws.raci.forEach(role => {
            if (role.role.toLowerCase().includes(query)) {
              score += 7;
              matchedIn.push('raci');
            }
          });
        }

        // Search in dependencies
        if (ws.dependencies) {
          ws.dependencies.forEach(dep => {
            if (dep.team.toLowerCase().includes(query)) {
              score += 4;
              matchedIn.push('dependencies');
            }
          });
        }

        // Search in output
        if (ws.output) {
          ws.output.forEach(out => {
            if (out.toLowerCase().includes(query)) {
              score += 2;
              matchedIn.push('output');
            }
          });
        }

        if (score > 0) {
          results.push({
            dept,
            area,
            ws,
            score,
            matchedIn: [...new Set(matchedIn)]
          });
        }
      });
    });
  });

  // Sort by score (highest first)
  results.sort((a, b) => b.score - a.score);

  // Display results
  displaySearchResults(results, query);
}

function displaySearchResults(results, query) {
  // Show/hide navigation items based on results
  document.querySelectorAll('.nav-department').forEach(dept => {
    dept.style.display = 'none';
  });

  if (results.length === 0) {
    // Show "no results" message
    showSearchInfo(`No results found for "${query}"`);
    return;
  }

  // Build matched items map with proper structure
  const matchedItems = new Map();

  results.forEach(result => {
    const deptId = result.dept.id;
    const areaId = result.area.id;
    const wsId = result.ws.id;

    if (!matchedItems.has(deptId)) {
      matchedItems.set(deptId, new Map());
    }
    if (!matchedItems.get(deptId).has(areaId)) {
      matchedItems.get(deptId).set(areaId, new Set());
    }
    matchedItems.get(deptId).get(areaId).add(wsId);
  });

  // Show only matching items
  matchedItems.forEach((areas, deptId) => {
    const deptElement = document.querySelector(`[data-dept-id="${deptId}"]`);
    if (!deptElement) return;

    // Show department
    deptElement.style.display = '';

    // Expand department
    const areasContainer = deptElement.querySelector('.nav-areas');
    const toggleIcon = deptElement.querySelector('.toggle-icon');
    if (areasContainer) areasContainer.classList.add('expanded');
    if (toggleIcon) toggleIcon.classList.add('expanded');

    // Hide all areas first
    const allAreas = deptElement.querySelectorAll('.nav-area');
    allAreas.forEach(area => {
      area.style.display = 'none';
    });

    // Show only matching areas
    areas.forEach((workstreams, areaId) => {
      const areaElement = deptElement.querySelector(`[data-area-id="${areaId}"]`);
      if (!areaElement) return;

      // Show area
      areaElement.style.display = '';

      // Expand area
      const workstreamsContainer = areaElement.querySelector('.nav-workstreams');
      const areaToggleIcon = areaElement.querySelector('.toggle-icon');
      if (workstreamsContainer) workstreamsContainer.classList.add('expanded');
      if (areaToggleIcon) areaToggleIcon.classList.add('expanded');

      // Hide all workstreams first
      const allWorkstreamLinks = areaElement.querySelectorAll('.nav-workstream-link');
      allWorkstreamLinks.forEach(link => {
        link.style.display = 'none';
      });

      // Show only matching workstreams
      workstreams.forEach(wsId => {
        const fullWsId = `${deptId}-${areaId}-${wsId}`;
        const wsLink = areaElement.querySelector(`[data-workstream-id="${fullWsId}"]`);
        if (wsLink) {
          wsLink.style.display = '';
        }
      });
    });
  });

  // Show results info
  showSearchInfo(`Showing ${results.length} result${results.length !== 1 ? 's' : ''} for "${query}"`);
}

function showSearchInfo(message) {
  let infoElement = document.getElementById('search-results-info');

  if (!infoElement) {
    infoElement = document.createElement('div');
    infoElement.id = 'search-results-info';
    infoElement.className = 'search-results-info';

    const content = document.querySelector('.content');
    if (content && content.firstChild) {
      content.insertBefore(infoElement, content.firstChild);
    }
  }

  infoElement.textContent = message;
  infoElement.style.display = 'block';
}

function clearSearch() {
  const searchInput = document.getElementById('search-input');
  if (searchInput) {
    searchInput.value = '';
  }

  // Show all navigation items
  document.querySelectorAll('.nav-department').forEach(item => {
    item.style.display = '';
  });

  document.querySelectorAll('.nav-area').forEach(item => {
    item.style.display = '';
  });

  document.querySelectorAll('.nav-workstream').forEach(item => {
    item.style.display = '';
  });

  document.querySelectorAll('.nav-workstream-link').forEach(item => {
    item.style.display = '';
  });

  // Collapse all
  document.querySelectorAll('.nav-areas, .nav-workstreams').forEach(container => {
    container.classList.remove('expanded');
  });

  document.querySelectorAll('.toggle-icon').forEach(icon => {
    icon.classList.remove('expanded');
  });

  // Hide search info
  const infoElement = document.getElementById('search-results-info');
  if (infoElement) {
    infoElement.style.display = 'none';
  }

  // Re-expand current workstream's parents if any
  if (currentWorkstream) {
    showWorkstream(currentWorkstream.deptId, currentWorkstream.areaId, currentWorkstream.wsId);
  }
}

// URL Routing Functions
function initRouting() {
  // Handle initial hash
  handleHashChange();

  // Listen for hash changes
  window.addEventListener('hashchange', handleHashChange);
}

function handleHashChange() {
  const hash = window.location.hash.slice(1); // Remove #

  if (!hash) {
    showHome();
    return;
  }

  // Parse hash format: dept-id-area-id-ws-id
  const parts = hash.split('-');

  // Try to find the workstream by reconstructing possible IDs
  // This is tricky because IDs can have hyphens in them
  // We'll try different split points

  if (!OPERATIONS_DATA) return;

  let found = false;

  OPERATIONS_DATA.departments.forEach(dept => {
    dept.areas.forEach(area => {
      area.workstreams.forEach(ws => {
        const fullId = `${dept.id}-${area.id}-${ws.id}`;
        if (fullId === hash) {
          showWorkstream(dept.id, area.id, ws.id);
          found = true;
        }
      });
    });
  });

  if (!found) {
    showHome();
  }
}

function navigateToWorkstream(deptId, areaId, wsId) {
  const hash = `#${deptId}-${areaId}-${wsId}`;
  window.location.hash = hash;
}

// Mobile Menu Functions
function toggleMobileMenu() {
  const sidebar = document.querySelector('.sidebar');
  if (sidebar) {
    sidebar.classList.toggle('mobile-open');
  }
}

function initMobileMenu() {
  const menuBtn = document.getElementById('mobile-menu-btn');
  if (menuBtn) {
    menuBtn.addEventListener('click', toggleMobileMenu);
  }

  // Close mobile menu when clicking a workstream link
  document.querySelectorAll('.nav-workstream-link').forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth <= 768) {
        const sidebar = document.querySelector('.sidebar');
        if (sidebar) {
          sidebar.classList.remove('mobile-open');
        }
      }
    });
  });
}

// Initialization
function initializeApp() {
  console.log('Initializing ConnectHear Operations Portal...');
  console.log('Data loaded:', OPERATIONS_DATA ? 'Yes' : 'No');

  if (!OPERATIONS_DATA) {
    console.error('Operations data not loaded!');
    return;
  }

  console.log(`Loaded ${OPERATIONS_DATA.departments.length} departments`);

  // Initialize all features
  initSearch();
  initRouting();
  initMobileMenu();
  initNavigationListeners();
  initBadgeCounts();
  initBackToTop();

  console.log('Portal initialized successfully!');
}

// Add badge counts to navigation
function initBadgeCounts() {
  // Add workstream counts to areas
  document.querySelectorAll('.nav-area').forEach(areaElement => {
    const workstreams = areaElement.querySelectorAll('.nav-workstream');
    if (workstreams.length > 0) {
      const areaHeader = areaElement.querySelector('.nav-area-header');
      if (areaHeader) {
        const badge = document.createElement('span');
        badge.className = 'badge-count';
        badge.textContent = workstreams.length;
        areaHeader.appendChild(badge);
      }
    }
  });

  console.log('Badge counts initialized');
}

// Back to top button
function initBackToTop() {
  // Create button
  const backToTopBtn = document.createElement('button');
  backToTopBtn.className = 'back-to-top';
  backToTopBtn.innerHTML = '↑';
  backToTopBtn.setAttribute('aria-label', 'Back to top');
  backToTopBtn.title = 'Back to top';
  document.body.appendChild(backToTopBtn);

  // Show/hide based on scroll
  const content = document.querySelector('.content');
  if (content) {
    content.addEventListener('scroll', () => {
      if (content.scrollTop > 300) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });
  }

  // Also check window scroll
  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      backToTopBtn.classList.add('visible');
    } else {
      backToTopBtn.classList.remove('visible');
    }
  });

  // Click handler
  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
    if (content) {
      content.scrollTo({ top: 0, behavior: 'smooth' });
    }
  });

  console.log('Back to top button initialized');
}

// Initialize navigation event listeners (alternative to inline onclick)
function initNavigationListeners() {
  // Add event listeners to all department headers
  document.querySelectorAll('.nav-department-header').forEach(header => {
    header.addEventListener('click', function() {
      const deptId = this.parentElement.getAttribute('data-dept-id');
      if (deptId) {
        toggleDepartment(deptId);
      }
    });
  });

  // Add event listeners to all area headers
  document.querySelectorAll('.nav-area-header').forEach(header => {
    header.addEventListener('click', function() {
      const areaId = this.parentElement.getAttribute('data-area-id');
      if (areaId) {
        toggleArea(areaId);
      }
    });
  });

  // Add event listeners to all workstream links
  document.querySelectorAll('.nav-workstream-link').forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const wsId = this.getAttribute('data-workstream-id');
      if (wsId) {
        const parts = wsId.split('-');
        // Parse the workstream ID to extract dept, area, and ws IDs
        // This is complex because IDs can contain hyphens
        // Use the data attribute structure
        const deptElement = this.closest('[data-dept-id]');
        const areaElement = this.closest('[data-area-id]');

        if (deptElement && areaElement) {
          const deptId = deptElement.getAttribute('data-dept-id');
          const areaId = areaElement.getAttribute('data-area-id');

          // Find the workstream ID by removing dept-area prefix
          const wsIdPart = wsId.replace(`${deptId}-${areaId}-`, '');

          navigateToWorkstream(deptId, areaId, wsIdPart);
        }
      }
    });
  });

  console.log('Navigation event listeners initialized');
}

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeApp);
} else {
  initializeApp();
}
