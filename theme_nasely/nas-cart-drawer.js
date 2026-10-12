(function() {
  var overlay = document.getElementById('nas-cart-overlay');
  var drawer = document.getElementById('nas-cart-drawer');
  var closeBtn = document.getElementById('nas-cart-close');
  var itemsEl = document.getElementById('nas-cart-items');
  var emptyEl = document.getElementById('nas-cart-empty');
  var footerEl = document.getElementById('nas-cart-footer');
  var totalEl = document.getElementById('nas-cart-total');
  var drawerCountEl = document.getElementById('nas-cart-count');
  var headerCountEl = document.getElementById('nas-header-cart-count');
  var cartTrigger = document.getElementById('nas-cart-trigger');

  if (!overlay || !drawer) return;

  /* ===== Offres Nasely : flacons achetés / offerts + guides ===== */
  var NAS_GIFT_BUNDLE_ID = 62714974732675;
  var NAS_BUNDLES = {
    62714822394243: { paid: 1, free: 1 },
    62714974732675: { paid: 2, free: 2 }
  };
  /* Prix barrés connus : évite de recharger la fiche produit à chaque ouverture du panier */
  var NAS_KNOWN_COMPARE = {
    62714822394243: 6980,
    62714974732675: 13960
  };
  /* Prix connus : permet d'afficher le panier rempli instantanément, avant la réponse du serveur */
  var NAS_KNOWN_PRICE = {
    62714822394243: 3490,
    62714974732675: 4990
  };
  var NAS_BOTTLE_IMG = 'https://cdn.shopify.com/s/files/1/1013/1783/7187/files/nasely-bottle-single.webp?v=1790709670&width=200';
  /* Guides = vrais produits (9,99 € / 12,99 €), offerts à -100 % par une réduction automatique quand l'offre 2 est dans le panier. */
  var NAS_GUIDE_ORDER = [62807604035971, 62807604429187];
  var NAS_GUIDES = {
    62807604035971: { title: 'Guide « Mieux dormir en 14 jours »', price: 999, img: 'https://cdn.shopify.com/s/files/1/1013/1783/7187/files/nasely-couverture-mieux-dormir-14-jours.png?v=1791820448&width=160', sub: 'Programme guidé · PDF' },
    62807604429187: { title: 'Guide « Recettes du soir pour mieux dormir »', price: 1299, img: 'https://cdn.shopify.com/s/files/1/1013/1783/7187/files/nasely-couverture-recettes-du-soir.png?v=1791820448&width=160', sub: '15 recettes · PDF' }
  };
  (function injectStyles() {
    if (document.getElementById('nas-cart-gift-style')) return;
    var st = document.createElement('style');
    st.id = 'nas-cart-gift-style';
    st.textContent =
      '.nas-cart-item-free{background:#FDF2F0;border-radius:12px;padding:10px;margin:-2px 0 12px}' +
      '.nas-cart-free-badge{display:inline-block;font-size:10.5px;font-weight:800;color:#fff;background:#2e7d32;border-radius:20px;padding:3px 9px}' +
      '.nas-cart-free-note{margin:6px 0 0;font-size:11.5px;color:#6E100F;font-weight:700}' +
      '.nas-cart-gifts{margin:-4px 0 12px;padding:12px;border:1.5px dashed #6E100F;border-radius:12px;background:#FDF2F0;display:flex;flex-direction:column;gap:8px}' +
      '.nas-cart-gifts-title{margin:0;font-size:12px;font-weight:800;color:#6E100F;letter-spacing:.3px}' +
      '.nas-cart-gift{display:flex;align-items:center;gap:10px;background:#fff;border-radius:10px;padding:8px 10px;border:1px solid #f0dcd7}' +
      'img.nas-cart-gift-cover{flex:0 0 34px;width:34px;height:48px;object-fit:cover;border-radius:2px 4px 4px 2px;box-shadow:0 2px 6px rgba(0,0,0,.18);display:block;background:#F5F0ED}' +
      '.nas-cart-gift-main{flex:1;min-width:0}' +
      '.nas-cart-gift-name{margin:0;font-size:12.5px;font-weight:700;color:#1a1a1a;line-height:1.25}' +
      '.nas-cart-gift-sub{margin:2px 0 0;font-size:11px;color:#8a7f7c}' +
      '.nas-cart-gift-price{display:flex;flex-direction:column;align-items:flex-end;flex-shrink:0;gap:2px}' +
      '.nas-cart-gift-price s{font-size:11px;color:#999}' +
      '.nas-cart-gift-price b{font-size:10.5px;font-weight:800;color:#fff;background:#2e7d32;border-radius:20px;padding:2px 8px}' +
      'img.nas-cart-guide-cover{flex:0 0 58px;width:58px;height:82px;object-fit:cover;border-radius:3px 6px 6px 3px;box-shadow:0 2px 8px rgba(0,0,0,.18);display:block;background:#F5F0ED}' +
      '.nas-cart-guide-note{margin:4px 0 6px;font-size:11px;color:#6E100F;font-weight:600}' +
      '.nas-cart-total-compare{font-size:14px;color:#999;text-decoration:line-through;margin-right:8px;font-weight:600}' +
      '.nas-cart-savings{margin:6px 0 0;text-align:right;font-size:13px;font-weight:800;color:#2e7d32}' +
      '#nas-cart-items{transition:opacity .15s}' +
      '#nas-cart-items.nas-cart-loading{opacity:.55;pointer-events:none}' +
      '#nas-cart-items.nas-cart-pending{pointer-events:none}' +
      '.nas-cart-wait{display:flex;justify-content:center;padding:48px 0}' +
      '.nas-cart-wait span{width:26px;height:26px;border:3px solid #f0dcd7;border-top-color:#6E100F;border-radius:50%;animation:nasSpin .7s linear infinite}' +
      '@keyframes nasSpin{to{transform:rotate(360deg)}}';
    document.head.appendChild(st);
  })();

  /* Précharge les couvertures pour un affichage instantané dans le panier */
  NAS_GUIDE_ORDER.forEach(function(id) { var i = new Image(); i.src = NAS_GUIDES[id].img; });

  function bundleOf(item) { return NAS_BUNDLES[item.variant_id] || null; }
  function guideOf(item) { return NAS_GUIDES[item.variant_id] || null; }
  function finalLine(item) { return item.final_line_price != null ? item.final_line_price : item.line_price; }
  function originalLine(item) { return item.original_line_price != null ? item.original_line_price : item.line_price; }

  function bottleCount(cart) {
    var n = 0;
    cart.items.forEach(function(item) {
      if (guideOf(item)) return;
      var b = bundleOf(item);
      n += b ? (b.paid + b.free) * item.quantity : item.quantity;
    });
    return n;
  }

  function renderTotalCompare(cart, compareTotal) {
    if (!totalEl) return;
    var cmp = document.getElementById('nas-cart-total-compare');
    if (!cmp) {
      cmp = document.createElement('span');
      cmp.id = 'nas-cart-total-compare';
      cmp.className = 'nas-cart-total-compare';
      totalEl.parentNode.insertBefore(cmp, totalEl);
    }
    var sav = document.getElementById('nas-cart-savings');
    if (!sav) {
      sav = document.createElement('p');
      sav.id = 'nas-cart-savings';
      sav.className = 'nas-cart-savings';
      var row = totalEl.parentNode;
      row.parentNode.insertBefore(sav, row.nextSibling);
    }
    var saved = compareTotal - cart.total_price;
    if (saved > 0) {
      cmp.textContent = formatMoney(compareTotal);
      cmp.style.display = '';
      sav.textContent = 'Vous économisez ' + formatMoney(saved) + ' 🎉';
      sav.style.display = '';
    } else {
      cmp.style.display = 'none';
      sav.style.display = 'none';
    }
  }

  function formatMoney(cents) {
    return (cents / 100).toFixed(2).replace('.', ',') + ' €';
  }

  var productCache = {};
  function loadProductsForCart(cart) {
    var handles = [];
    cart.items.forEach(function(item) {
      if (NAS_KNOWN_COMPARE[item.variant_id] || guideOf(item)) return;
      if (item.handle && handles.indexOf(item.handle) === -1 && !productCache[item.handle]) {
        handles.push(item.handle);
      }
    });
    if (!handles.length) return Promise.resolve();
    return Promise.all(handles.map(function(handle) {
      return fetch('/products/' + handle + '.js').then(function(r) { return r.json(); }).then(function(product) {
        productCache[handle] = product;
      }).catch(function() {});
    }));
  }

  function getVariantCompareAt(item) {
    var known = NAS_KNOWN_COMPARE[item.variant_id];
    if (known) return known > item.price ? known : null;
    var product = productCache[item.handle];
    if (!product) return null;
    var variant = product.variants.filter(function(v) { return v.id === item.variant_id; })[0];
    if (!variant || !variant.compare_at_price) return null;
    return variant.compare_at_price > item.price ? variant.compare_at_price : null;
  }

  function openDrawer() {
    overlay.classList.add('nas-cart-open');
    drawer.classList.add('nas-cart-open');
    drawer.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    overlay.classList.remove('nas-cart-open');
    drawer.classList.remove('nas-cart-open');
    drawer.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  function setLoading(on) {
    itemsEl.classList.toggle('nas-cart-loading', !!on);
    if (!on) itemsEl.classList.remove('nas-cart-pending');
  }

  /* Petit indicateur de chargement (jamais « panier vide » pendant un ajout) */
  function showWaiting() {
    emptyEl.hidden = true;
    itemsEl.classList.remove('nas-cart-loading');
    itemsEl.innerHTML = '<div class="nas-cart-wait"><span></span></div>';
  }

  /* Panier « prévu » affiché immédiatement : panier actuel + ce qui vient d'être ajouté */
  function optimisticCart(base, addedId, qty) {
    var price = NAS_KNOWN_PRICE[addedId];
    if (!price) return null;
    var items = (base ? base.items : []).map(function(it) {
      var c = {};
      for (var k in it) c[k] = it[k];
      return c;
    });
    var title = 'Extrait de Cerise Griotte';
    var image = NAS_BOTTLE_IMG;
    items.forEach(function(it) { if (bundleOf(it)) { title = it.product_title; image = it.image || image; } });
    var existing = items.filter(function(it) { return it.variant_id === addedId; })[0];
    if (existing) {
      existing.quantity += qty;
      existing.line_price = existing.price * existing.quantity;
      existing.final_line_price = existing.line_price;
      existing.original_line_price = existing.line_price;
    } else {
      items.unshift({ key: 'nas-pending', variant_id: addedId, quantity: qty, price: price, line_price: price * qty, final_line_price: price * qty, original_line_price: price * qty, product_title: title, image: image });
    }
    var hasGiftBundle = items.some(function(it) { return it.variant_id === NAS_GIFT_BUNDLE_ID; });
    if (hasGiftBundle) {
      items.forEach(function(it) {
        var g = guideOf(it);
        if (g) { it.final_line_price = 0; it.original_line_price = g.price * it.quantity; }
      });
    }
    var total = 0;
    items.forEach(function(it) { total += it.final_line_price != null ? it.final_line_price : it.line_price; });
    return { items: items, total_price: total, pending: true };
  }

  function qtyControls(item) {
    return '<div class="nas-cart-item-qty">' +
        '<button type="button" data-action="decrease" data-key="' + item.key + '" data-qty="' + item.quantity + '" aria-label="Diminuer la quantité">−</button>' +
        '<span>' + item.quantity + '</span>' +
        '<button type="button" data-action="increase" data-key="' + item.key + '" data-qty="' + item.quantity + '" aria-label="Augmenter la quantité">+</button>' +
      '</div>' + removeBtn(item);
  }
  function removeBtn(item) {
    return '<button type="button" class="nas-cart-item-remove" data-action="remove" data-key="' + item.key + '">Supprimer</button>';
  }

  /* Encadré « Vos guides offerts » (affiché tant que l'offre 2 est dans le panier) */
  function renderGiftBox(guideItems, bundleQty) {
    var box = document.createElement('div');
    box.className = 'nas-cart-gifts';
    var html = '<p class="nas-cart-gifts-title">🎁 Vos guides offerts avec cette offre</p>';
    var compare = 0;
    NAS_GUIDE_ORDER.forEach(function(id) {
      var g = NAS_GUIDES[id];
      var it = guideItems[id];
      var orig = it ? originalLine(it) : g.price * bundleQty;
      var fin = it ? finalLine(it) : 0;
      compare += orig;
      var free = fin < orig;
      html +=
        '<div class="nas-cart-gift">' +
          '<img class="nas-cart-gift-cover" src="' + g.img + '" alt="" width="34" height="48">' +
          '<div class="nas-cart-gift-main"><p class="nas-cart-gift-name">' + g.title + '</p><p class="nas-cart-gift-sub">' + g.sub + ' · Envoyé par e-mail</p></div>' +
          '<div class="nas-cart-gift-price">' + (free ? '<s>' + formatMoney(orig) + '</s><b>OFFERT</b>' : '<span style="font-weight:800">' + formatMoney(fin) + '</span>') + '</div>' +
        '</div>';
    });
    box.innerHTML = html;
    return { el: box, compare: compare };
  }

  /* Guide affiché comme un vrai produit payant (quand l'offre 2 n'est plus dans le panier) */
  function renderPaidGuide(item) {
    var g = guideOf(item);
    var el = document.createElement('div');
    el.className = 'nas-cart-item';
    el.innerHTML =
      '<img class="nas-cart-guide-cover" src="' + g.img + '" alt="" width="58" height="82">' +
      '<div class="nas-cart-item-main">' +
        '<p class="nas-cart-item-title">' + g.title + '</p>' +
        '<p class="nas-cart-item-variant">' + g.sub + ' · Envoyé par e-mail</p>' +
        '<p class="nas-cart-guide-note">🎁 Offert avec l\'offre 2 achetés + 2 offerts</p>' +
        removeBtn(item) +
      '</div>' +
      '<div class="nas-cart-item-price">' +
        '<span class="nas-cart-item-price-sale">' + formatMoney(finalLine(item)) + '</span>' +
      '</div>';
    return el;
  }

  var lastCart = null;

  function renderCart(cart) {
    if (!cart.pending) lastCart = cart;
    setLoading(false);
    if (cart.pending) itemsEl.classList.add('nas-cart-pending');
    itemsEl.innerHTML = '';
    var compareTotal = 0;
    if (!cart.items.length) {
      emptyEl.hidden = false;
      footerEl.hidden = true;
    } else {
      emptyEl.hidden = true;
      footerEl.hidden = false;
      var guideItems = {};
      var bundleQty = 0;
      cart.items.forEach(function(item) {
        if (guideOf(item)) guideItems[item.variant_id] = item;
        if (item.variant_id === NAS_GIFT_BUNDLE_ID) bundleQty += item.quantity;
      });
      cart.items.forEach(function(item) {
        if (guideOf(item)) return;
        var compareAt = getVariantCompareAt(item);
        var compareLineTotal = compareAt ? compareAt * item.quantity : null;
        var hasDiscount = compareLineTotal && compareLineTotal > item.line_price;
        compareTotal += hasDiscount ? compareLineTotal : originalLine(item);
        var b = bundleOf(item);
        var el = document.createElement('div');
        el.className = 'nas-cart-item';
        if (b) {
          var total = b.paid + b.free;
          var unitCompare = compareLineTotal ? Math.round(compareLineTotal / total) : 0;
          var paidCompare = unitCompare * b.paid;
          var freeCompare = unitCompare * b.free;
          var paidN = b.paid * item.quantity;
          var freeN = b.free * item.quantity;
          el.innerHTML =
            '<img class="nas-cart-item-img" src="' + (item.image || '') + '" alt="">' +
            '<div class="nas-cart-item-main">' +
              '<p class="nas-cart-item-title">' + item.product_title + '</p>' +
              '<p class="nas-cart-item-variant">' + paidN + ' flacon' + (paidN > 1 ? 's' : '') + ' acheté' + (paidN > 1 ? 's' : '') + '</p>' +
              qtyControls(item) +
            '</div>' +
            '<div class="nas-cart-item-price">' +
              '<span class="nas-cart-item-price-sale">' + formatMoney(item.line_price) + '</span>' +
              (paidCompare > item.line_price ? '<span class="nas-cart-item-price-compare" style="text-decoration:line-through">' + formatMoney(paidCompare) + '</span>' : '') +
            '</div>';
          itemsEl.appendChild(el);
          var free = document.createElement('div');
          free.className = 'nas-cart-item nas-cart-item-free';
          free.innerHTML =
            '<img class="nas-cart-item-img" src="' + (item.image || '') + '" alt="">' +
            '<div class="nas-cart-item-main">' +
              '<p class="nas-cart-item-title">' + item.product_title + '</p>' +
              '<p class="nas-cart-item-variant">🎁 ' + freeN + ' flacon' + (freeN > 1 ? 's' : '') + ' offert' + (freeN > 1 ? 's' : '') + '</p>' +
              '<p class="nas-cart-free-note">Inclus avec votre offre</p>' +
            '</div>' +
            '<div class="nas-cart-item-price">' +
              '<span class="nas-cart-free-badge">OFFERT</span>' +
              (freeCompare ? '<span class="nas-cart-item-price-compare" style="text-decoration:line-through">' + formatMoney(freeCompare) + '</span>' : '') +
            '</div>';
          itemsEl.appendChild(free);
          if (item.variant_id === NAS_GIFT_BUNDLE_ID) {
            var box = renderGiftBox(guideItems, item.quantity);
            itemsEl.appendChild(box.el);
            compareTotal += box.compare;
          }
        } else {
          el.innerHTML =
            '<img class="nas-cart-item-img" src="' + (item.image || '') + '" alt="">' +
            '<div class="nas-cart-item-main">' +
              '<p class="nas-cart-item-title">' + item.product_title + '</p>' +
              (item.variant_title && item.variant_title !== 'Default Title' ? '<p class="nas-cart-item-variant">' + item.variant_title + '</p>' : '') +
              qtyControls(item) +
            '</div>' +
            '<div class="nas-cart-item-price">' +
              '<span class="nas-cart-item-price-sale">' + formatMoney(item.line_price) + '</span>' +
              (hasDiscount ? '<span class="nas-cart-item-price-compare" style="text-decoration:line-through">' + formatMoney(compareLineTotal) + '</span>' : '') +
            '</div>';
          itemsEl.appendChild(el);
        }
      });
      if (!bundleQty) {
        NAS_GUIDE_ORDER.forEach(function(id) {
          var it = guideItems[id];
          if (!it) return;
          compareTotal += originalLine(it);
          itemsEl.appendChild(renderPaidGuide(it));
        });
      }
      totalEl.textContent = formatMoney(cart.total_price);
      renderTotalCompare(cart, compareTotal);
    }
    var count = bottleCount(cart);
    if (drawerCountEl) drawerCountEl.textContent = count;
    if (headerCountEl) {
      headerCountEl.textContent = count;
      headerCountEl.style.display = count > 0 ? 'flex' : 'none';
    }
  }

  /* Pendant un ajout, une ancienne réponse ne doit jamais remplacer l'affichage prévu */
  var adding = 0;
  function showCart(cart, force) {
    return loadProductsForCart(cart).then(function() {
      if (adding && !force) { lastCart = cart; return cart; }
      renderCart(cart);
      return cart;
    });
  }

  function fetchCart(force) {
    return fetch('/cart.js').then(function(r) { return r.json(); }).then(function(cart) { return showCart(cart, force); });
  }

  function changeItem(key, quantity) {
    setLoading(true);
    fetch('/cart/change.js', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: key, quantity: quantity })
    }).then(function(r) { return r.json(); }).then(showCart).catch(function() { setLoading(false); });
  }

  itemsEl.addEventListener('click', function(e) {
    var btn = e.target.closest('button[data-action]');
    if (!btn) return;
    var key = btn.getAttribute('data-key');
    var action = btn.getAttribute('data-action');
    if (action === 'remove') {
      changeItem(key, 0);
    } else {
      var qty = parseInt(btn.getAttribute('data-qty'), 10);
      changeItem(key, action === 'increase' ? qty + 1 : Math.max(0, qty - 1));
    }
  });

  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  overlay.addEventListener('click', closeDrawer);
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeDrawer();
  });

  function openNow() {
    if (lastCart) { renderCart(lastCart); setLoading(true); } else { showWaiting(); }
    openDrawer();
    return fetchCart().catch(function() { setLoading(false); });
  }

  if (cartTrigger) {
    cartTrigger.addEventListener('click', function(e) {
      e.preventDefault();
      openNow();
    });
  }

  /* Offre 2 : flacons + guides manquants ajoutés en une seule requête */
  function bundleItemsFromForm(formData, addedId) {
    var qty = parseInt(formData.get('quantity'), 10) || 1;
    var main = { id: addedId, quantity: qty };
    var props = {};
    var hasProps = false;
    formData.forEach(function(value, name) {
      var m = /^properties\[(.+)\]$/.exec(name);
      if (m && typeof value === 'string') { props[m[1]] = value; hasProps = true; }
    });
    if (hasProps) main.properties = props;
    var sellingPlan = formData.get('selling_plan');
    if (sellingPlan) main.selling_plan = sellingPlan;
    var present = {};
    lastCart.items.forEach(function(it) { present[it.variant_id] = true; });
    var items = [main];
    NAS_GUIDE_ORDER.forEach(function(id) { if (!present[id]) items.push({ id: id, quantity: 1 }); });
    return items;
  }

  function interceptForm(form) {
    if (form.dataset.nasCartBound) return;
    form.dataset.nasCartBound = 'true';
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      var formData = new FormData(form);
      var addedId = parseInt(formData.get('id'), 10);
      /* Ouverture immédiate du panier déjà rempli, confirmé dès la réponse du serveur */
      var qty = parseInt(formData.get('quantity'), 10) || 1;
      var guess = optimisticCart(lastCart, addedId, qty);
      if (guess) renderCart(guess);
      else if (lastCart && lastCart.items.length) { renderCart(lastCart); setLoading(true); }
      else showWaiting();
      openDrawer();
      adding++;
      var oneRequest = addedId === NAS_GIFT_BUNDLE_ID && !!lastCart;
      var req;
      if (oneRequest) {
        req = fetch('/cart/add.js', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify({ items: bundleItemsFromForm(formData, addedId) })
        });
      } else {
        req = fetch('/cart/add.js', {
          method: 'POST',
          headers: { 'Accept': 'application/json' },
          body: formData
        });
      }
      req.then(function(r) {
        if (!r.ok) return r.json().then(function(err) { throw err; });
        return r.json();
      }).then(function() {
        if (addedId === NAS_GIFT_BUNDLE_ID && !oneRequest) return addGuidesIfMissing();
      }).then(function() {
        adding--;
        return fetchCart(true);
      }).catch(function(err) {
        adding = Math.max(0, adding - 1);
        console.error('Nasely cart: add to cart failed', err);
        fetchCart(true).catch(function() { setLoading(false); });
      });
    });
  }

  /* Secours si le panier n'était pas encore chargé au moment du clic */
  function addGuidesIfMissing() {
    return fetch('/cart.js').then(function(r) { return r.json(); }).then(function(cart) {
      var present = {};
      cart.items.forEach(function(it) { present[it.variant_id] = true; });
      var toAdd = NAS_GUIDE_ORDER.filter(function(id) { return !present[id]; }).map(function(id) { return { id: id, quantity: 1 }; });
      if (!toAdd.length) return;
      return fetch('/cart/add.js', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({ items: toAdd })
      }).catch(function() {});
    });
  }

  document.querySelectorAll('form[action*="/cart/add"]').forEach(interceptForm);

  window.nasCart = { open: openNow, refresh: function() { return fetchCart(); } };

  fetchCart();
})();
