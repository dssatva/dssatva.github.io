/* ==========================================================
   DS SATVA — site behaviour
   1. product grid (drops in a real photo the moment one exists)
   2. hero slider: push transition + parallax band + Ken Burns
   3. scroll reveal, mobile nav, year
   ========================================================== */
(function () {
  "use strict";

  var WA = "https://wa.me/917709932222?text=";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------------------------------------------------
     1. THE RANGE
     English is the product's name; Hindi sits under it as a
     secondary line. `cat` is the fine-grained shelf, while GROUPS
     decides which tabs exist — so the two can differ, and ground
     and whole spices share a single tab.
     `img` is tried first. If the file is not there yet, the card
     keeps its designed tile — so to add a real photo later, just
     save it at that exact path and reload. Nothing else to edit.
     --------------------------------------------------------- */
  var PRODUCTS = [
    /* ---- ground spices ---- */
    { acc:"#e8a713", ink:"#94660a", en:"Turmeric", hi:"हल्दी", cat:"ground", form:"Ground", glyph:"हल",
      d:"The everyday base — dal, sabzi and every tadka starts here.",
      img:"assets/p-haldi.jpg", tint:"linear-gradient(150deg,#e3ae3c,#c1860f)" },
    { acc:"#c3341a", ink:"#a52a13", en:"Chilli Powder", hi:"लाल मिर्च", cat:"ground", form:"Ground", glyph:"मि",
      d:"Colour and heat, ground from whole dried chillies.",
      img:"assets/p-mirchi.jpg", tint:"linear-gradient(150deg,#cf5238,#a8321b)" },
    { acc:"#93a04b", ink:"#5f6a26", en:"Coriander Powder", hi:"धनिया", cat:"ground", form:"Ground", glyph:"ध",
      d:"Warm and nutty — the quiet base under a good curry.",
      img:"assets/p-dhane.jpg", tint:"linear-gradient(150deg,#bcae63,#948537)" },

    /* ---- whole spices, for tadka ---- */
    { acc:"#a3763f", ink:"#6b5029", en:"Cumin Seeds", hi:"जीरा", cat:"whole", form:"Whole", glyph:"जी",
      d:"Whole, for the first crackle in hot oil.",
      img:"assets/p-jeera.jpg", tint:"linear-gradient(150deg,#b98d55,#8a6a3a)" },
    { acc:"#c9962a", ink:"#8a6510", en:"Mustard Seeds", hi:"राई", cat:"whole", form:"Whole", glyph:"रा",
      d:"Small, sharp and made for tadka.",
      img:"assets/p-rai.jpg", tint:"linear-gradient(150deg,#d3a844,#a87d16)" },
    { acc:"#b08b2e", ink:"#7d6118", en:"Fenugreek Seeds", hi:"मेथी दाना", cat:"whole", form:"Whole", glyph:"मे",
      d:"A bitter edge for pickles, dal and tadka.",
      img:"assets/p-methi.jpg", tint:"linear-gradient(150deg,#bf9c48,#94781f)" },

    /* ---- masala blends ---- */
    { acc:"#a8462a", ink:"#8a3720", en:"Kanda Lasun Masala", hi:"प्याज़ लहसुन मसाला", cat:"blend", glyph:"प्या",
      d:"Onion, garlic and chilli — the Marathwada blend, ground fresh.",
      img:"assets/p-kandalasun.jpg", tint:"linear-gradient(150deg,#c9603f,#9e3d22)" },
    { acc:"#7d5630", ink:"#634324", en:"Garam Masala", hi:"गरम मसाला", cat:"blend", glyph:"गर",
      d:"The finishing spoon — stirred in at the end, not boiled away.",
      img:"assets/p-garam.jpg", tint:"linear-gradient(150deg,#a38055,#74562f)" },
    { acc:"#8f2e28", ink:"#7a2620", en:"Meat Masala", hi:"मीट मसाला", cat:"blend", glyph:"मी",
      d:"Built for slow-cooked mutton and chicken curry.",
      img:"assets/p-meat.jpg", tint:"linear-gradient(150deg,#a7473f,#7c2721)" },
    { acc:"#e2912b", ink:"#94590c", en:"Biryani Masala", hi:"बिरयानी मसाला", cat:"blend", glyph:"बि",
      d:"For layered rice — whole spices ground for aroma, not just heat.",
      img:"assets/p-biryani.jpg", tint:"linear-gradient(150deg,#e8a750,#c07a17)" },
    { acc:"#7f6a4e", ink:"#5f5039", en:"Chaat Masala", hi:"चाट मसाला", cat:"blend", glyph:"चा",
      d:"The tangy finish for chaat, fruit and a glass of buttermilk.",
      img:"assets/p-chaat.jpg", tint:"linear-gradient(150deg,#9b8768,#6d5a41)" },
    { acc:"#b8453c", ink:"#96332b", en:"Chatpat Masala", hi:"चटपट मसाला", cat:"blend", glyph:"चट",
      d:"Sharp and tangy — for chivda, raw mango, anything that needs a lift.",
      img:"assets/p-chatpat.jpg", tint:"linear-gradient(150deg,#c9605a,#a3352c)" },

    /* ---- seeds ---- */
    { acc:"#a08256", ink:"#6a4a33", en:"Flax Seeds", hi:"अलसी", cat:"seeds", glyph:"अल",
      d:"Roast and grind for chutney, or stir into roti dough.",
      img:"assets/p-flax.jpg", tint:"linear-gradient(150deg,#b39468,#8a6244)" },
    { acc:"#68737e", ink:"#3f4952", en:"Chia Seeds", hi:"चिया बीज", cat:"seeds", glyph:"चि",
      d:"Stir into water, curd or a smoothie.",
      img:"assets/p-chia.jpg", tint:"linear-gradient(150deg,#7c8794,#55606b)" },
    { acc:"#c2a878", ink:"#7d6a42", en:"Quinoa", hi:"क्विनोआ", cat:"seeds", glyph:"क्वि",
      d:"Cooks like rice, in about fifteen minutes.",
      img:"assets/p-quinoa.jpg", tint:"linear-gradient(150deg,#d0ba92,#a88d5c)" },

    /* ---- pantry staples ---- */
    { acc:"#d98a8a", ink:"#a04a55", en:"Himalayan Pink Salt", hi:"गुलाबी नमक", cat:"pantry", glyph:"नम",
      d:"Unrefined rock salt, ground coarse or fine.",
      img:"assets/p-pinksalt.jpg", tint:"linear-gradient(150deg,#e3a3a3,#c07474)" },
    /* TO CONFIRM: khandsari / desi khand, or jaggery? If jaggery, this cannot
       be labelled sugar — rename to Jaggery / गुड़ before any label is printed. */
    { acc:"#b5813f", ink:"#855c26", en:"Unprocessed Sugar", hi:"खांडसरी", cat:"pantry", glyph:"खां",
      d:"Unrefined and unbleached, with the molasses left in.",
      img:"assets/p-khandsari.jpg", tint:"linear-gradient(150deg,#c4954f,#96692a)" },

    /* ---- cold-pressed oils ---- */
    { acc:"#d98f2f", ink:"#8f6a13", en:"Groundnut Oil", hi:"मूंगफली तेल", cat:"oils", glyph:"मू",
      d:"Cold-pressed, for everyday cooking.",
      img:"assets/p-groundnutoil.jpg", tint:"linear-gradient(150deg,#e0a54a,#b57b1c)" },
    { acc:"#c9a86a", ink:"#7f6733", en:"Sesame Oil", hi:"तिल तेल", cat:"oils", glyph:"ति",
      d:"Cold-pressed til oil, for tadka and for pickles.",
      img:"assets/p-sesameoil.jpg", tint:"linear-gradient(150deg,#d4b880,#a88b4c)" },
    { acc:"#cfa81f", ink:"#866c08", en:"Mustard Oil", hi:"सरसों तेल", cat:"oils", glyph:"सर",
      d:"Sharp and pungent, cold-pressed.",
      img:"assets/p-mustardoil.jpg", tint:"linear-gradient(150deg,#dcb93a,#a8880e)" },
    { acc:"#8a9a84", ink:"#566250", en:"Coconut Oil", hi:"नारियल तेल", cat:"oils", glyph:"ना",
      d:"Cold-pressed, mild and clean.",
      img:"assets/p-coconutoil.jpg", tint:"linear-gradient(150deg,#a3b09d,#6f7d69)" }
  ];

  /* Tabs. `cats:null` means everything.
     The owner walked through jainproducts-style shelving on 4 Sep 2026 and asked
     for the spices split the way that site splits them - "whole spices, blend and
     seeds and all in that way we can have" - so "Spices" was broken into its two
     real shelves. Ground and Whole are now separate tabs and separate category
     cards; nothing else about the filtering changed. */
  var GROUPS = [
    { id:"all",    label:"Everything",    cats:null },
    { id:"ground", label:"Ground spices", cats:["ground"] },
    { id:"whole",  label:"Whole spices",  cats:["whole"] },
    { id:"blend",  label:"Blends",        cats:["blend"] },
    { id:"seeds",  label:"Seeds",         cats:["seeds"] },
    { id:"pantry", label:"Pantry",        cats:["pantry"] },
    { id:"oils",   label:"Oils",          cats:["oils"] }
  ];

  var MORTAR = '<svg class="mortar" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 11h14a7 7 0 0 1-7 7 7 7 0 0 1-7-7Z"/><path d="M12 18v3M8 21h8"/><path d="M16 8.5 19 4"/></svg>';
  var CHAT = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.2-1.8-.9-2.1-1-.3-.1-.5-.2-.7.1s-.8 1-1 1.2c-.2.2-.4.3-.7.1a8.2 8.2 0 0 1-2.4-1.5 9.1 9.1 0 0 1-1.7-2.1c-.2-.3 0-.5.1-.7l.6-.7c.1-.2.2-.4.1-.6l-.9-2.1c-.2-.5-.4-.5-.6-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.1 1.1-1.1 2.6s1.1 3 1.3 3.2c.1.2 2 3.2 4.9 4.4 2.4 1 2.9.8 3.4.8.5-.1 1.7-.7 1.9-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.2-.6-.4zM12 21.5c-1.7 0-3.4-.5-4.9-1.3l-3.4.9.9-3.3A9.4 9.4 0 0 1 2.6 12 9.4 9.4 0 0 1 12 2.6 9.4 9.4 0 0 1 21.4 12 9.4 9.4 0 0 1 12 21.5z"/></svg>';
  var VEG = '<span class="veg" title="Vegetarian"><i></i></span>';

  // the spice-spectrum rules are drawn from the product list, so the range can
  // grow to any length and the rule (and the grid) simply follow
  document.querySelectorAll(".spectrum").forEach(function (bar) {
    bar.innerHTML = PRODUCTS.map(function (p) {
      return '<i style="background:' + p.acc + '" title="' + p.en + '"></i>';
    }).join("");
  });

  /* Category tabs, counted off the list itself so they stay correct as it grows.
     MENU-FIRST (5 Sep 2026, the owner's instruction): nothing is listed until a
     shelf is chosen. The tabs are the menu; #rangepick holds the space until the
     first choice, then never returns. Before this, all 21 products were listed
     on load under a selected "Everything" tab, which put the whole catalogue on
     the page before anyone had asked for any of it. */
  var tabsEl = document.getElementById("tabs");
  var pickEl = document.getElementById("rangepick");
  var inGroup = function (g, cat) { return !g.cats || g.cats.indexOf(cat) > -1; };

  function showGroup(g, tabBtn) {
    if (tabsEl) {
      [].forEach.call(tabsEl.children, function (o) { o.setAttribute("aria-selected", "false"); });
      if (tabBtn) tabBtn.setAttribute("aria-selected", "true");
    }
    [].forEach.call(document.querySelectorAll(".pcard"), function (card) {
      var out = !inGroup(g, card.dataset.cat);
      card.classList.toggle("hide", out);
      // a card that was display:none never met the reveal observer, so it would
      // come back at opacity 0 - the same trap as the recipe tabs
      if (!out) card.classList.add("in");
    });
    if (pickEl) pickEl.hidden = true;
    var grid = document.getElementById("grid");
    if (grid) grid.classList.add("is-listed");
  }

  if (tabsEl) {
    GROUPS.forEach(function (g) {
      var count = PRODUCTS.filter(function (p) { return inGroup(g, p.cat); }).length;
      if (!count) return;                       // never render an empty tab
      var b = document.createElement("button");
      b.className = "tab";
      b.type = "button";
      b.setAttribute("role", "tab");
      b.setAttribute("aria-selected", "false");   // nothing chosen yet
      b.dataset.cat = g.id;
      b.innerHTML = g.label + '<span class="n">' + count + "</span>";
      b.addEventListener("click", function () { showGroup(g, b); });
      tabsEl.appendChild(b);
    });
  }

  /* ---------------------------------------------------------
     1b. SHOP BY CATEGORY
     Arch-topped cards, one per GROUPS entry (minus "all"). Counts
     and labels come off GROUPS and PRODUCTS, so adding a product
     or a group updates this block with no edit here. Clicking a
     card selects the matching tab and scrolls to the grid.
     --------------------------------------------------------- */
  var CAT_ART = {
    ground: { tint:"linear-gradient(150deg,#f7e2ad,#deac3f)",
              blurb:"Stone-ground, in their own colour and smell.",
              icon:'<path d="M3.5 12.5h17a8.5 8.5 0 0 1-17 0Z"/><path d="M6.5 12.5c1.5-4 3.2-6 5.5-6s4 2 5.5 6"/>' },
    whole:  { tint:"linear-gradient(150deg,#e8dcb6,#a98f46)",
              blurb:"Left whole, to grind when you cook.",
              icon:'<path d="M7 4.5c3.4 0 5 2.2 5 7.5s-1.6 7.5-5 7.5"/><path d="M17 4.5c-3.4 0-5 2.2-5 7.5s1.6 7.5 5 7.5"/><path d="M12 4.5v15"/>' },
    blend:  { tint:"linear-gradient(150deg,#e6b795,#b9714a)",
              blurb:"The everyday masalas, built from whole spices.",
              icon:'<path d="M5 11h14a7 7 0 0 1-7 7 7 7 0 0 1-7-7Z"/><path d="M12 18v3M8 21h8"/><path d="M16 8.5 19 4"/>' },
    seeds:  { tint:"linear-gradient(150deg,#d8e2b4,#93a04b)",
              blurb:"Whole and unrefined, nothing polished off.",
              icon:'<ellipse cx="8" cy="9" rx="3.2" ry="2.2" transform="rotate(-25 8 9)"/><ellipse cx="15.5" cy="11" rx="3.2" ry="2.2" transform="rotate(15 15.5 11)"/><ellipse cx="11" cy="15.5" rx="3.2" ry="2.2" transform="rotate(-8 11 15.5)"/>' },
    pantry: { tint:"linear-gradient(150deg,#f2d3d3,#d98a8a)",
              blurb:"Salt and sugar as they come, not as they are bleached.",
              icon:'<rect x="6" y="8" width="12" height="13" rx="2.5"/><path d="M9 8V5h6v3M8 5h8"/>' },
    oils:   { tint:"linear-gradient(150deg,#f6e7ae,#cfa72a)",
              blurb:"Pressed, not refined, so the smell survives.",
              icon:'<path d="M10.5 3h3v3l2.8 3.5A4 4 0 0 1 17 12v7a2 2 0 0 1-2 2H9a2 2 0 0 1-2-2v-7a4 4 0 0 1 .7-2.5L10.5 6Z"/><path d="M12 13.5c1.2 1.4 2 2.4 2 3.2a2 2 0 1 1-4 0c0-.8.8-1.8 2-3.2Z"/>' }
  };

  var catWrap = document.getElementById("cats");
  if (catWrap) {
    GROUPS.forEach(function (g) {
      if (g.id === "all") return;                       // not a category
      var a = CAT_ART[g.id];
      if (!a) return;                                   // no art, no card
      var count = PRODUCTS.filter(function (p) {
        return !g.cats || g.cats.indexOf(p.cat) > -1;
      }).length;
      if (!count) return;                               // never an empty card

      var card = document.createElement("button");
      card.type = "button";
      card.className = "catcard reveal";
      card.dataset.cat = g.id;
      card.innerHTML =
        '<span class="cshot" style="--tint:' + a.tint + '">' +
          '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" ' +
            'stroke-linecap="round" stroke-linejoin="round">' + a.icon + '</svg>' +
          '<span class="cscrim"></span>' +
          '<span class="cname">' + g.label + '</span>' +
          '<span class="carrow" aria-hidden="true">' +
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" ' +
              'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13M12 5l7 7-7 7"/></svg>' +
          '</span>' +
        '</span>' +
        '<span class="cmeta">' +
          '<span class="cblurb">' + a.blurb + '</span>' +
          '<span class="ccount">' + count + (count === 1 ? " item" : " items") + '</span>' +
        '</span>';

      // the photograph replaces the icon tile, same probe pattern as everywhere else
      (function (c) {
        var probe = new Image();
        probe.onload = function () {
          var shot = c.querySelector(".cshot");
          if (!shot) return;
          probe.alt = "";
          probe.loading = "lazy";
          shot.insertBefore(probe, shot.firstChild);
          shot.querySelector("svg").remove();
          shot.classList.add("has-photo");
        };
        probe.src = "assets/cat-" + g.id + ".jpg";
      })(card);

      card.addEventListener("click", function () {
        // drive the existing tabs rather than duplicate their filtering
        var tab = document.querySelector('.tab[data-cat="' + g.id + '"]');
        if (tab) tab.click();
        var range = document.getElementById("range");
        if (range) range.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
      });

      catWrap.appendChild(card);
    });
  }

  /* ---------------------------------------------------------
     1c. THE SHELF SLIDER
     Five editorial openings, one per shelf, after the page the
     owner sent on 6 Sep 2026 (jainfarmfresh.com/products/spices).

     Deliberately NOT autoplaying. The hero already advances on
     its own, and two carousels moving at once on one page read
     as noise; this one is browsed, not watched. The named tab
     strip is the real navigation - arrows and swipe are there
     for anyone who would rather flick through.

     Counts and tab labels come off the slides and PRODUCTS, so
     adding a sixth slide needs no edit here, and a count can
     never drift from what the range below will actually list.
     --------------------------------------------------------- */
  var shStage = document.getElementById("shstage");
  var shTabs  = document.getElementById("shtabs");

  if (shStage) {
    var shelves = [].slice.call(shStage.querySelectorAll(".shelf"));
    var shCur = 0, shBusy = false;

    // count line, off the same PRODUCTS/GROUPS pair the tabs use
    shelves.forEach(function (s) {
      var el = s.querySelector(".sh-count");
      if (!el) return;
      var g = GROUPS.filter(function (o) { return o.id === s.dataset.shelf; })[0];
      if (!g) return;
      var n = PRODUCTS.filter(function (p) { return inGroup(g, p.cat); }).length;
      if (n) el.textContent = n + (n === 1 ? " item packed" : " items packed");
    });

    function shGo(to) {
      var n = shelves.length;
      to = ((to % n) + n) % n;
      if (to === shCur || shBusy) return;
      shBusy = true;
      shelves[shCur].classList.remove("is-on");
      shelves[to].classList.add("is-on");
      if (shTabs) {
        [].forEach.call(shTabs.children, function (b, i) {
          b.setAttribute("aria-selected", i === to ? "true" : "false");
          b.tabIndex = i === to ? 0 : -1;
        });
      }
      shCur = to;
      setTimeout(function () { shBusy = false; }, reduce ? 20 : 620);
    }

    if (shTabs) {
      shelves.forEach(function (s, i) {
        var b = document.createElement("button");
        b.className = "etab";
        b.type = "button";
        b.setAttribute("role", "tab");
        b.setAttribute("aria-selected", i === 0 ? "true" : "false");
        b.tabIndex = i === 0 ? 0 : -1;
        b.textContent = s.dataset.label || ("Shelf " + (i + 1));
        b.addEventListener("click", function () { shGo(i); });
        // left/right walk the strip, the usual tablist behaviour
        b.addEventListener("keydown", function (e) {
          var d = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0;
          if (!d) return;
          e.preventDefault();
          var nx = ((shCur + d) % shelves.length + shelves.length) % shelves.length;
          shGo(nx);
          shTabs.children[nx].focus();
        });
        shTabs.appendChild(b);
      });
    }

    var shPrev = document.getElementById("shprev");
    var shNext = document.getElementById("shnext");
    if (shPrev) shPrev.addEventListener("click", function () { shGo(shCur - 1); });
    if (shNext) shNext.addEventListener("click", function () { shGo(shCur + 1); });

    // swipe, same threshold as the hero
    var sx0 = null;
    shStage.addEventListener("pointerdown", function (e) { sx0 = e.clientX; });
    shStage.addEventListener("pointerup", function (e) {
      if (sx0 === null) return;
      var dx = e.clientX - sx0; sx0 = null;
      if (Math.abs(dx) > 55) shGo(shCur + (dx < 0 ? 1 : -1));
    });
    shStage.addEventListener("pointercancel", function () { sx0 = null; });

    /* Each pill drives the existing range tabs rather than filtering on its own
       - exactly what a category card does when clicked, so a visitor arriving
       from either lands on the same listed shelf. */
    shStage.addEventListener("click", function (e) {
      var pill = e.target.closest ? e.target.closest(".pill[data-go]") : null;
      if (!pill) return;
      e.preventDefault();
      var tab = document.querySelector('.tab[data-cat="' + pill.dataset.go + '"]');
      if (tab) tab.click();
      var range = document.getElementById("range");
      if (range) range.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
    });
  }

  /* one product card, used by both the full grid and the essentials row below,
     so the two can never drift apart */
  function buildCard(p, cls) {
    var card = document.createElement("article");
    card.className = "pcard frame" + (cls ? " " + cls : "");
    card.style.setProperty("--r", "20px");
    card.style.setProperty("--acc", p.acc);
    card.style.setProperty("--acc-ink", p.ink);
    card.dataset.cat = p.cat;
    card.innerHTML =
      '<div class="pthumb tile" style="--tint:' + p.tint + '">' +
        '<span class="glyph">' + p.glyph + '</span>' + MORTAR + VEG +
      '</div>' +
      '<div class="pbody">' +
        '<h3>' + p.en + '</h3>' +
        '<p class="dv">' + p.hi + '</p>' +
        (p.form ? '<span class="pform">' + p.form + '</span>' : '') +
        '<p>' + p.d + '</p>' +
        '<a class="ask" href="' + WA + encodeURIComponent("Namaste! Please send me the pack sizes and price for SATVA " + p.en + ".") + '">' +
          CHAT + "Ask price on WhatsApp</a>" +
      "</div>";

    // swap the tile for a real photo if one exists at p.img
    var probe = new Image();
    probe.onload = function () {
      var thumb = card.querySelector(".pthumb");
      thumb.classList.remove("tile");
      thumb.removeAttribute("style");
      thumb.innerHTML = "";
      probe.alt = p.en;
      thumb.appendChild(probe);
      thumb.insertAdjacentHTML("beforeend", VEG);
    };
    probe.src = p.img;

    return card;
  }

  var grid = document.getElementById("grid");
  if (grid) {
    PRODUCTS.forEach(function (p, i) {
      var card = buildCard(p, "reveal d" + (i % 4));
      card.classList.add("hide");               // nothing listed until a shelf is picked
      grid.appendChild(card);
    });
  }

  /* 1d. EVERYDAY ESSENTIALS - REMOVED 5 Sep 2026.
     It was a curated row of 13 products, every one of which is also in the
     full range below, so the same spices were introduced twice on one page
     (and Cumin Seeds appeared twice inside the row itself, being in both the
     "Kitchen staples" and "Whole spices" lists). The way into the range is
     now SHOP BY CATEGORY above, which filters rather than repeats.
     If a curated row is ever wanted again, it must show something the range
     does not - a seasonal set, or the pack sizes the range omits. */

  /* ---------------------------------------------------------
     1e. HEADER: range dropdown + rotating announcement
     Both after curiospice.com. The dropdown is filled from
     GROUPS so it lists exactly what the grid can show, and each
     item drives the existing tabs - one filtering mechanism for
     the whole site.
     --------------------------------------------------------- */
  var rangeMenu = document.getElementById("rangemenu");
  if (rangeMenu) {
    var jumpTo = function (id) {
      var tab = document.querySelector('.tab[data-cat="' + id + '"]');
      if (tab) tab.click();
      var range = document.getElementById("range");
      if (range) range.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
      // let go of hover-open so the menu does not hang around after the jump
      if (document.activeElement && document.activeElement.blur) document.activeElement.blur();
    };

    GROUPS.forEach(function (g) {
      var count = PRODUCTS.filter(function (p) {
        return !g.cats || g.cats.indexOf(p.cat) > -1;
      }).length;
      if (!count) return;

      var li = document.createElement("li");
      var a  = document.createElement("a");
      a.href = "#range";
      a.innerHTML = (g.id === "all" ? "Everything" : g.label) +
                    '<span class="mn">' + count + "</span>";
      if (g.id === "all") li.className = "all";
      a.addEventListener("click", function (e) {
        e.preventDefault();
        jumpTo(g.id);
      });
      li.appendChild(a);
      rangeMenu.appendChild(li);
    });

    // Escape closes the menu wherever focus is inside it
    var hasmenu = rangeMenu.closest(".hasmenu");
    if (hasmenu) {
      hasmenu.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && document.activeElement && document.activeElement.blur) {
          document.activeElement.blur();
        }
      });
    }
  }

  /* the announcement line. The count message is written here rather than in the
     HTML so it can never disagree with PRODUCTS. */
  var tick = document.getElementById("tickline");
  if (tick) {
    var countMsg = document.getElementById("tickcount");
    if (countMsg) {
      countMsg.textContent = PRODUCTS.length + " daily kitchen staples, and counting";
      countMsg.hidden = false;
    }

    var msgs = [].slice.call(tick.querySelectorAll(".tmsg"));
    if (msgs.length > 1 && !reduce) {
      var at = 0, hold = null;
      var turn = function () {
        msgs[at].classList.remove("is-on");
        at = (at + 1) % msgs.length;
        msgs[at].classList.add("is-on");
      };
      var run   = function () { hold = setInterval(turn, 4200); };
      var pause = function () { clearInterval(hold); };
      run();
      tick.addEventListener("mouseenter", pause);
      tick.addEventListener("mouseleave", run);
      document.addEventListener("visibilitychange", function () {
        if (document.hidden) pause(); else run();
      });
    }
  }

  /* ---------------------------------------------------------
     2. HERO SLIDER
     --------------------------------------------------------- */
  var hero   = document.querySelector(".hero");
  var slides = [].slice.call(document.querySelectorAll(".slide"));
  var dots   = document.getElementById("dots");
  var bar    = document.getElementById("bar");
  var nextup = document.getElementById("nextup");
  var nImg   = document.getElementById("nextupImg");
  var nTitle = document.getElementById("nextupTitle");
  var DUR = 1000, DELAY = 5600;
  var cur = 0, busy = false, timer = null;

  if (hero && slides.length) {
    slides.forEach(function (s, i) {
      var b = document.createElement("button");
      b.setAttribute("role", "tab");
      b.setAttribute("aria-label", "Slide " + (i + 1));
      b.setAttribute("aria-current", i === 0 ? "true" : "false");
      b.addEventListener("click", function () { go(i); });
      dots.appendChild(b);
    });

    function paintNextUp() {
      var n = slides[(cur + 1) % slides.length];
      nImg.src = n.getAttribute("data-thumb") || "";
      nTitle.textContent = n.getAttribute("data-title") || "";
    }

    function restartBar() {
      if (!bar || reduce) return;
      bar.style.transition = "none";
      bar.style.width = "0%";
      void bar.offsetWidth;
      bar.style.transition = "width " + DELAY + "ms linear";
      bar.style.width = "100%";
    }

    function schedule() {
      clearTimeout(timer);
      if (reduce) return;
      restartBar();
      timer = setTimeout(function () { go(cur + 1); }, DELAY);
    }

    function go(to) {
      var n = slides.length;
      to = ((to % n) + n) % n;
      if (to === cur || busy) return;
      var dir = to > cur ? 1 : -1;
      if (cur === 0 && to === n - 1) dir = -1;
      if (cur === n - 1 && to === 0) dir = 1;

      var out = slides[cur], inc = slides[to];
      busy = true;

      hero.classList.remove("anim");
      inc.style.transform = "translate3d(" + (dir > 0 ? 100 : -100) + "%,0,0)";
      inc.classList.add("is-active");
      out.classList.add("is-leaving");
      void inc.offsetWidth;

      hero.classList.add("anim");
      inc.style.transform = "translate3d(0,0,0)";
      out.style.transform = "translate3d(" + (dir > 0 ? -38 : 38) + "%,0,0)";

      dots.children[cur].setAttribute("aria-current", "false");
      dots.children[to].setAttribute("aria-current", "true");
      cur = to;
      paintNextUp();

      setTimeout(function () {
        out.classList.remove("is-active", "is-leaving");
        out.style.transform = "";
        inc.style.transform = "";
        busy = false;
      }, reduce ? 20 : DUR);

      schedule();
    }

    document.getElementById("prev").addEventListener("click", function () { go(cur - 1); });
    document.getElementById("next").addEventListener("click", function () { go(cur + 1); });
    nextup.addEventListener("click", function () { go(cur + 1); });

    hero.addEventListener("mouseenter", function () { clearTimeout(timer); if (bar) bar.style.transition = "none"; });
    hero.addEventListener("mouseleave", schedule);
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) clearTimeout(timer); else schedule();
    });

    // swipe
    var x0 = null;
    hero.addEventListener("pointerdown", function (e) { x0 = e.clientX; });
    hero.addEventListener("pointerup", function (e) {
      if (x0 === null) return;
      var dx = e.clientX - x0; x0 = null;
      if (Math.abs(dx) > 55) go(cur + (dx < 0 ? 1 : -1));
    });
    hero.addEventListener("pointercancel", function () { x0 = null; });

    // keyboard, only while the hero is on screen
    var heroVisible = true;
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (es) { heroVisible = es[0].isIntersecting; },
        { threshold: 0.25 }).observe(hero);
    }
    document.addEventListener("keydown", function (e) {
      if (!heroVisible) return;
      if (e.key === "ArrowRight") go(cur + 1);
      if (e.key === "ArrowLeft") go(cur - 1);
    });

    paintNextUp();
    schedule();
  }

  /* The floating WhatsApp button appears once the opening section has scrolled
     away - it would otherwise sit on top of that section's own controls.
     It used to live inside the hero block and observe .hero; when the shelf
     slider replaced the hero on 6 Sep 2026 that block stopped running, and the
     button would never have shown again. It now observes whichever section
     opens the page, so it survives the next reshuffle too. */
  (function () {
    var fab = document.querySelector(".wafab");
    if (!fab) return;
    var first = document.querySelector("main > section, body > section");
    if (!first || !("IntersectionObserver" in window)) { fab.classList.add("show"); return; }
    new IntersectionObserver(function (es) {
      fab.classList.toggle("show", !es[0].isIntersecting);
    }, { threshold: 0.12 }).observe(first);
  })();

  /* ---------------------------------------------------------
     2b. ORIGIN — where it comes from
     Modelled on the three place cards on onyxcoffeelab.com
     (PERU / ECUADOR / COLOMBIA): a name, one paragraph of
     terroir, one link, over full-bleed media.

     What is deliberately different: Onyx runs a looping video
     behind each card. The owner said "we'll not have a video as
     of now", so each card renders a tinted ground with line art
     and probes for media - drop `assets/origin-<id>.jpg` (or
     .mp4) in and that card switches over with no code edit.

     IMPORTANT: a region only appears here once the owner has
     confirmed it. `todo:true` renders the card visibly
     unfinished rather than inventing a sourcing story - see
     "Copy on this page is the owner's, or it does not ship" in
     the README. Only the grinding location is stated as fact,
     because it is the one already on the page.
     --------------------------------------------------------- */
  var LEAF = '<path d="M12 21c0-7 3-12 9-15-1 8-4 13-9 15Z"/><path d="M12 21C12 14 9 9 3 6c1 8 4 13 9 15Z"/><path d="M12 21v-6"/>';
  var HILL = '<path d="M2 18h20"/><path d="M2 18 9 7l4.5 7"/><path d="M11 18l4-6 7 6"/><circle cx="17.5" cy="5.5" r="2"/>';
  var MILL = '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="2.4"/><path d="M12 4v2.6M12 17.4V20M4 12h2.6M17.4 12H20"/>';

  var ORIGINS = [
    { id:"grind", place:"Chhatrapati Sambhajinagar", hi:"छत्रपती संभाजीनगर",
      icon:MILL, tint:"linear-gradient(150deg,#c9a24a,#7d5630)",
      tag:"Where it is ground",
      blurb:"Marathwada. Every pouch is ground in small batches and packed here — the address on the back of the packet is the address the spice was last touched at.",
      link:{ label:"What is on our pouch", href:"#freshness" } },

    { id:"region-1", place:"Region to be named", icon:HILL, todo:true,
      tint:"linear-gradient(150deg,#b7c48a,#6f8168)",
      tag:"To confirm",
      blurb:"The owner is collecting photographs and the growers’ own account from the farms this range is sourced from. Nothing is written here until that arrives." },

    { id:"region-2", place:"Region to be named", icon:LEAF, todo:true,
      tint:"linear-gradient(150deg,#e2c98f,#b08b3a)",
      tag:"To confirm",
      blurb:"The second sourcing region, on the same terms. A named place, one honest paragraph, and a photograph we actually own." }
  ];

  var oWrap = document.getElementById("origins");
  if (oWrap) {
    ORIGINS.forEach(function (o, i) {
      var card = document.createElement("article");
      card.className = "ocard reveal d" + (i % 4) + (o.todo ? " todo" : "");
      card.innerHTML =
        (o.tag ? '<span class="otag">' + o.tag + "</span>" : "") +
        '<span class="ofield" style="--tint:' + o.tint + '">' +
          '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" ' +
            'stroke-linecap="round" stroke-linejoin="round">' + o.icon + "</svg>" +
        "</span>" +
        '<h3 class="oplace">' + o.place +
          (o.hi ? '<span class="ohi dv">' + o.hi + "</span>" : "") +
        "</h3>" +
        '<p class="oblurb">' + o.blurb + "</p>" +
        (o.link ? '<a class="olink" href="' + o.link.href + '">' + o.link.label + "</a>" : "");

      /* swap the tinted ground for real media the moment a file exists.
         Same probe-then-swap idea as buildCard, so adding a photo is a
         file drop. A video is preferred only if the owner supplies one. */
      var probe = new Image();
      probe.onload = function () {
        var f = card.querySelector(".ofield");
        if (!f) return;
        probe.alt = "";
        probe.className = "omedia";
        f.replaceWith(probe);
      };
      probe.src = "assets/origin-" + o.id + ".jpg";

      oWrap.appendChild(card);
    });
  }

  /* ---------------------------------------------------------
     2c. RECIPES
     After the recipe row on dandelionchocolate.com. The one
     thing taken from it is the cook time sitting on the card
     ("Just Chocolate Cake · 2½ Hours") - it is what turns a
     photograph into something a cook can decide about.

     Not taken: their MORE RECIPES link, because there is no
     recipe library to link to yet. Each card names the SATVA
     product it uses instead, which is the point of the block.

     These are ordinary household recipes in our own voice, not
     claims about the business. `uses` must match a name in
     PRODUCTS or the accent falls back to gold.
     --------------------------------------------------------- */
  var POT  = '<path d="M4 9h16v6a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4V9Z"/><path d="M2 9h20"/><path d="M20 11h2v3h-2M4 11H2v3h2"/><path d="M9 6c0-1.5 1.3-2 1.3-3.5M14 6c0-1.5 1.3-2 1.3-3.5"/>';
  var RICE = '<path d="M2.5 19.5h19"/><path d="M4.5 19.5c0-4.8 3.4-8.2 7.5-8.2s7.5 3.4 7.5 8.2"/><path d="M8.8 15.6c1.1-.9 2-1.3 3.2-1.3s2.1.4 3.2 1.3"/><path d="M12 11V7.4"/><path d="M10.2 8.6 12 6.2l1.8 2.4"/>';
  var PAN  = '<circle cx="10" cy="12" r="7.2"/><path d="M17.4 12H22"/><circle cx="10" cy="12" r="3.2"/>';

  /* Two groups, because the range is no longer masala alone:
     what the blends are for, and what the seeds and grains are for.
     `id` keys the photo (assets/recipe-<id>.jpg) - keyed on the recipe
     and NOT on `uses`, so two recipes may share a product.
     `uses` must still match an `en` name in PRODUCTS or the accent
     falls back to gold. A card with no photo file keeps its tile. */
  var RECIPES = [
    /* ---- with the masalas ---- */
    { id:"varan-bhaat", group:"masala", name:"Everyday Varan Bhaat", hi:"वरण भात", time:"40 min",
      icon:POT, tint:"linear-gradient(150deg,#f7e2ad,#deac3f)",
      desc:"Toor dal, turmeric, a spoon of ghee and a tadka of cumin and mustard. The plainest thing in the kitchen, and the fastest way to tell whether your turmeric is real.",
      uses:"Turmeric" },

    { id:"biryani", group:"masala", name:"Sunday Biryani", hi:"बिर्याणी", time:"1 hr 30 min",
      icon:RICE, tint:"linear-gradient(150deg,#d8c69a,#8a6210)",
      desc:"Whole spices bloomed in ghee first, the blend layered in with the rice, then sealed and left alone. The long one — worth starting before lunch.",
      uses:"Biryani Masala" },

    { id:"rassa", group:"masala", name:"Aitwarcha Rassa", hi:"आयतवारचा रस्सा", time:"1 hr 15 min",
      icon:POT, tint:"linear-gradient(150deg,#c98a63,#8c3a1c)",
      desc:"Onion and dry coconut browned properly before anything else goes in — that browning is the whole gravy. Mutton on the bone, and the thinnest rassa you can still call thick.",
      uses:"Meat Masala" },

    { id:"chole", group:"masala", name:"Chole", hi:"छोले", time:"45 min",
      icon:POT, tint:"linear-gradient(150deg,#e3c98d,#a4761f)",
      desc:"Chana soaked overnight, cooked soft, then garam masala stirred in at the end rather than the start so it stays fragrant instead of turning bitter.",
      uses:"Garam Masala" },

    { id:"bhel", group:"masala", name:"Bhel", hi:"भेळ", time:"10 min",
      icon:PAN, tint:"linear-gradient(150deg,#f0d7a8,#c98b2c)",
      desc:"Mix it at the table, eat it in five minutes, and never before — bhel waits for nobody. Chaat masala goes on last, over everything.",
      uses:"Chaat Masala" },

    { id:"shengdana", group:"masala", name:"Masala Shengdana", hi:"मसाला शेंगदाणे", time:"15 min",
      icon:PAN, tint:"linear-gradient(150deg,#e9c98f,#b06a22)",
      desc:"Peanuts roasted dry, tossed hot with chatpat masala and a squeeze of lime. The thing that disappears off the counter before dinner is served.",
      uses:"Chatpat Masala" },

    { id:"misal", group:"masala", name:"Misal", hi:"मिसळ", time:"1 hr",
      icon:POT, tint:"linear-gradient(150deg,#e0a07f,#a32d10)",
      desc:"The kat is where the chilli has to be honest — colour without a burnt edge. Sprouted matki under it, farsan on top, pav on the side.",
      uses:"Chilli Powder" },

    { id:"bharli-vangi", group:"masala", name:"Bharli Vangi", hi:"भरली वांगी", time:"40 min",
      icon:PAN, tint:"linear-gradient(150deg,#c9a9c4,#6b3f66)",
      desc:"Small brinjals slit and stuffed with coriander, groundnut and coconut, then left to cook slowly until the skins give. Dhane powder does most of the work.",
      uses:"Coriander Powder" },

    { id:"zunka", group:"masala", name:"Kanda Lasun Zunka", hi:"कांदा लसूण झुणका", time:"25 min",
      icon:PAN, tint:"linear-gradient(150deg,#e6b795,#b9714a)",
      desc:"Besan roasted down with onion and garlic until it goes nutty, then the masala off the heat so the garlic stays sharp. Bhakri, and nothing else.",
      uses:"Kanda Lasun Masala" },

    /* ---- with the seeds and grains ---- */
    { id:"jeera-bhaat", group:"seed", name:"Jeera Bhaat", hi:"जिरा भात", time:"20 min",
      icon:RICE, tint:"linear-gradient(150deg,#efe0bd,#c19a4e)",
      desc:"Cumin in hot ghee until it darkens a shade and smells like a kitchen — no further. Rice on top, lid on, no stirring. What you make when the curry is doing the talking.",
      uses:"Cumin Seeds" },

    { id:"fodni-poha", group:"seed", name:"Fodnicha Poha", hi:"फोडणीचे पोहे", time:"20 min",
      icon:PAN, tint:"linear-gradient(150deg,#f6e7a8,#d8a72b)",
      desc:"Wait for the mustard to actually pop before the onion goes in; everything after that is timing. Peanuts for the crunch, lime at the end, coconut if you have it.",
      uses:"Mustard Seeds" },

    { id:"methi-dal", group:"seed", name:"Methi Dal Tadka", hi:"मेथी डाळ", time:"35 min",
      icon:POT, tint:"linear-gradient(150deg,#f4dda1,#c68f1e)",
      desc:"Four or five methi seeds in the tadka — no more. They turn the dal faintly bitter in the way that makes you want the next spoon, and too many ruin it outright.",
      uses:"Fenugreek Seeds" },

    { id:"javas-chutney", group:"seed", name:"Javas Chutney", hi:"जवस चटणी", time:"15 min",
      icon:PAN, tint:"linear-gradient(150deg,#dcc39a,#8e6435)",
      desc:"Flax roasted till it crackles, cooled completely, then ground coarse with garlic, chilli and salt. Keeps a fortnight in a steel dabba. Bhakri, bhaat, or a spoon straight off the plate.",
      uses:"Flax Seeds" },

    { id:"chia", group:"seed", name:"Overnight Chia", hi:"चिया", time:"5 min + a night",
      icon:POT, tint:"linear-gradient(150deg,#e4e6ef,#9aa3bd)",
      desc:"Three spoons of chia to a cup of milk, sweetened however you take it, left in the fridge overnight. Fruit in the morning. Nothing is cooked and nothing can go wrong.",
      uses:"Chia Seeds" },

    { id:"quinoa", group:"seed", name:"Quinoa Bowl", hi:"क्विनोआ", time:"25 min",
      icon:RICE, tint:"linear-gradient(150deg,#dfe3c9,#8a9457)",
      desc:"Rinse it properly first — that bitter coating is why most people decide they dislike quinoa. Then treat it as bhaat: a fodni, whatever vegetable is in the house, lime.",
      uses:"Quinoa" }
  ];

  var RGROUPS = [
    { id:"masala", label:"With our masalas" },
    { id:"seed",   label:"With our seeds & grains" }
  ];

  function buildRecipeCard(r, i) {
    var prod = PRODUCTS.filter(function (p) { return p.en === r.uses; })[0];
    var card = document.createElement("article");
    card.className = "reccard reveal d" + (i % 4);
    if (prod) card.style.setProperty("--acc", prod.acc);
    card.innerHTML =
      '<div class="rfield" style="--tint:' + r.tint + '">' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" ' +
          'stroke-linecap="round" stroke-linejoin="round">' + r.icon + "</svg>" +
        '<span class="rtime">' + r.time + "</span>" +
      "</div>" +
      '<div class="rbody">' +
        "<h3>" + r.name + '<span class="rhi dv">' + r.hi + "</span></h3>" +
        '<p class="rdesc">' + r.desc + "</p>" +
        '<p class="ruses"><i></i>Made with ' + r.uses + "</p>" +
      "</div>";

    // a real photo replaces the tile, same as everywhere else on the page
    var probe = new Image();
    probe.onload = function () {
      var f = card.querySelector(".rfield");
      if (!f) return;
      probe.alt = r.name;
      probe.loading = "lazy";
      f.insertBefore(probe, f.firstChild);
      f.querySelector("svg").remove();
      f.classList.add("has-photo");
    };
    probe.src = "assets/recipe-" + r.id + ".jpg";

    return card;
  }

  /* The strip, after the "See what else we're cooking up" marquee on graza.co.
     Measured off their live page 5 Sep 2026: a fixed card width with VARYING
     heights, top-aligned, 20px corners, and the whole set duplicated exactly
     twice inside a track that translates -50% on a linear loop - which is what
     makes the loop seamless without any JS running per frame.

     Taken differently in one place, on purpose: theirs does not pause on hover,
     because their slides are photographs and nothing else. Ours carry a name, a
     cook time and the masala it needs, so the strip pauses on hover and on
     keyboard focus - a moving target you cannot finish reading is worse than no
     movement. Reduced motion stops it altogether and hands back a normal
     scrollbar. */
  /* 2/3 was the tallest of these and it alone decided the strip height, since
     every card is top-aligned in one row. Capped at 3/4 so the stagger stays
     but the tallest card is ~11% shorter. */
  var RH = ["4/5", "1/1", "3/4", "5/6", "4/5", "1/1", "5/6", "3/4"];

  var recStage = document.getElementById("recipes-stage");
  var recTabs  = document.getElementById("rtabs");
  if (recStage) {
    var rTracks = [];

    RGROUPS.forEach(function (g, gi) {
      var list = RECIPES.filter(function (r) { return r.group === g.id; });
      if (!list.length) return;                       // never an empty tab

      var mq = document.createElement("div");
      mq.className = "recmq";
      mq.id = "rtrack-" + g.id;
      mq.setAttribute("role", "tabpanel");
      mq.setAttribute("aria-label", g.label);
      if (gi) mq.hidden = true;

      var inner = document.createElement("div");
      inner.className = "recmq-inner";

      // set one, then the same set again: the loop is a -50% translate, so the
      // second copy is what is on screen as the first scrolls away
      for (var pass = 0; pass < 2; pass++) {
        list.forEach(function (r, i) {
          var card = buildRecipeCard(r, i);
          card.style.setProperty("--rar", RH[i % RH.length]);
          if (pass === 1) {
            card.setAttribute("aria-hidden", "true");   // a duplicate, not a second recipe
            card.classList.add("is-clone");
          }
          inner.appendChild(card);
        });
      }

      mq.appendChild(inner);
      recStage.appendChild(mq);
      rTracks.push(mq);

      // The loop shift is the pitch from a card to its own duplicate - measured,
      // not computed from scrollWidth, which is half a gap short. Speed is held
      // at ~62px a second whatever the group's length.
      (function (box, setLen) {
        function measure() {
          var kids = box.children;
          if (kids.length <= setLen) return;
          var pitch = kids[setLen].offsetLeft - kids[0].offsetLeft;
          if (pitch <= 0) return;
          box.style.setProperty("--shift", pitch + "px");
          box.style.animationDuration = Math.round(pitch / 62) + "s";
        }
        requestAnimationFrame(measure);
        window.addEventListener("resize", function () {
          clearTimeout(box._mqT);
          box._mqT = setTimeout(measure, 180);
        });
        box._mqMeasure = measure;
      })(inner, list.length);

      if (!recTabs) return;
      var tab = document.createElement("button");
      tab.type = "button";
      tab.className = "etab";
      tab.setAttribute("role", "tab");
      tab.setAttribute("aria-selected", gi === 0 ? "true" : "false");
      tab.setAttribute("aria-controls", mq.id);
      tab.innerHTML = g.label + ' <span class="ecount">' + list.length + "</span>";
      tab.addEventListener("click", function () {
        [].forEach.call(recTabs.children, function (o) { o.setAttribute("aria-selected", "false"); });
        tab.setAttribute("aria-selected", "true");
        rTracks.forEach(function (tr) { tr.hidden = tr !== mq; });
        // a track that was hidden never met the reveal observer, and its width
        // could not be measured either - do both now that it is on screen
        mq.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("in"); });
        var box = mq.querySelector(".recmq-inner");
        if (box && box._mqMeasure) box._mqMeasure();
      });
      recTabs.appendChild(tab);
    });
  }

  /* ---------------------------------------------------------
     2d. THE MISSION COLOUR-SHIFT
     The owner noticed a reference site whose ground changes
     colour only for its mission section - "when we come here to
     our mission, the site color is changing. It's like that only
     for our mission." The domain was never named in the
     recording, so only the idea is borrowed.

     --mx runs 0 -> 1 as the section's centre approaches the
     centre of the viewport, and the CSS mixes cream toward gold
     across that range. Nothing else on the page reads --mx, so
     the effect cannot leak into a neighbouring section.
     --------------------------------------------------------- */
  var mission = document.querySelector(".mission");
  if (mission && !reduce) {
    var mTick = false;
    var mShift = function () {
      mTick = false;
      var r = mission.getBoundingClientRect();
      var vh = window.innerHeight || 1;
      if (r.bottom < 0 || r.top > vh) return;           // off screen, leave it
      // 0 when the section's centre is a full viewport away, 1 when centred
      var dist = Math.abs((r.top + r.height / 2) - vh / 2);
      var mx = 1 - Math.min(dist / (vh * 0.75), 1);
      mission.style.setProperty("--mx", mx.toFixed(3));
    };
    var onMScroll = function () {
      if (mTick) return;
      mTick = true;
      requestAnimationFrame(mShift);
    };
    addEventListener("scroll", onMScroll, { passive: true });
    addEventListener("resize", onMScroll);
    mShift();
  }

  /* ---------------------------------------------------------
     3. reveal on scroll
     --------------------------------------------------------- */
  function reveal() {
    var els = [].slice.call(document.querySelectorAll(".reveal"));
    if (reduce || !("IntersectionObserver" in window)) {
      els.forEach(function (el) { el.classList.add("in"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
  }
  reveal();
  // cards are injected after first paint
  setTimeout(reveal, 60);

  /* ---------------------------------------------------------
     4. mobile nav + year
     --------------------------------------------------------- */
  var burger = document.getElementById("burger"), nav = document.getElementById("nav");
  if (burger) {
    burger.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A" && nav.classList.contains("open")) {
        nav.classList.remove("open");
        burger.setAttribute("aria-expanded", "false");
      }
    });
  }
  var yr = document.getElementById("yr");
  if (yr) yr.textContent = new Date().getFullYear();
})();
