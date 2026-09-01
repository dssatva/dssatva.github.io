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
     `img` is tried first. If the file is not there yet, the card
     keeps its designed tile — so to add a real photo later, just
     save it at that exact path and reload. Nothing else to edit.
     --------------------------------------------------------- */
  var PRODUCTS = [
    { acc:"#e8a713", ink:"#94660a", mr:"हळद", en:"Turmeric", cat:"single", glyph:"हळ",
      d:"The everyday base of every Maharashtrian kitchen — bhaji, varan, amti.",
      img:"assets/p-haldi.jpg", tint:"linear-gradient(150deg,#e3ae3c,#c1860f)" },
    { acc:"#c3341a", ink:"#a52a13", mr:"लाल तिखट", en:"Chilli Powder", cat:"single", glyph:"ति",
      d:"Colour and heat, ground from whole dried chillies.",
      img:"assets/p-mirchi.jpg", tint:"linear-gradient(150deg,#cf5238,#a8321b)" },
    { acc:"#93a04b", ink:"#5f6a26", mr:"धणे पूड", en:"Coriander Powder", cat:"single", glyph:"धणे",
      d:"Warm and nutty — the quiet base under a good rassa.",
      img:"assets/p-dhane.jpg", tint:"linear-gradient(150deg,#bcae63,#948537)" },
    { acc:"#a8462a", ink:"#8a3720", mr:"कांदा लसूण मसाला", en:"Kanda Lasun Masala", cat:"blend", glyph:"कां",
      d:"Onion, garlic and chilli — what a misal or usal cannot do without.",
      img:"assets/p-kandalasun.jpg", tint:"linear-gradient(150deg,#c9603f,#9e3d22)" },
    { acc:"#7d5630", ink:"#634324", mr:"गरम मसाला", en:"Garam Masala", cat:"blend", glyph:"गरम",
      d:"The finishing spoon — stirred in at the end, not boiled away.",
      img:"assets/p-garam.jpg", tint:"linear-gradient(150deg,#a38055,#74562f)" },
    { acc:"#8f2e28", ink:"#7a2620", mr:"मीट मसाला", en:"Meat Masala", cat:"blend", glyph:"मीट",
      d:"Built for slow-cooked mutton and chicken rassa.",
      img:"assets/p-meat.jpg", tint:"linear-gradient(150deg,#a7473f,#7c2721)" },
    { acc:"#e2912b", ink:"#94590c", mr:"बिर्याणी मसाला", en:"Biryani Masala", cat:"blend", glyph:"बि",
      d:"For layered rice — whole spices ground for aroma, not just heat.",
      img:"assets/p-biryani.jpg", tint:"linear-gradient(150deg,#e8a750,#c07a17)" },
    { acc:"#d1521f", ink:"#a53d13", mr:"पाव भाजी मसाला", en:"Pav Bhaji Masala", cat:"blend", glyph:"पाव",
      d:"The tawa blend. Butter, bhaji, pav, done.",
      img:"assets/p-pavbhaji.jpg", tint:"linear-gradient(150deg,#dd6c3a,#b3410f)" },
    { acc:"#7f6a4e", ink:"#5f5039", mr:"चाट मसाला", en:"Chaat Masala", cat:"blend", glyph:"चाट",
      d:"The tangy finish for bhel, sev puri, fruit and a glass of buttermilk.",
      img:"assets/p-chaat.jpg", tint:"linear-gradient(150deg,#9b8768,#6d5a41)" },
    { acc:"#b8453c", ink:"#96332b", mr:"चटपट मसाला", en:"Chatpat Masala", cat:"blend", glyph:"चट",
      d:"Sharp and tangy — for chivda, kairi, and anything that needs a lift.",
      img:"assets/p-chatpat.jpg", tint:"linear-gradient(150deg,#c9605a,#a3352c)" }
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

  // category tabs, counted off the list itself so they stay correct as it grows
  var tabsEl = document.getElementById("tabs");
  if (tabsEl) {
    var n = function (c) { return PRODUCTS.filter(function (p) { return c === "all" || p.cat === c; }).length; };
    [["all","Everything"],["single","Single spices"],["blend","Blends"]].forEach(function (t, i) {
      var b = document.createElement("button");
      b.className = "tab";
      b.type = "button";
      b.setAttribute("role", "tab");
      b.setAttribute("aria-selected", i === 0 ? "true" : "false");
      b.dataset.cat = t[0];
      b.innerHTML = t[1] + '<span class="n">' + n(t[0]) + "</span>";
      b.addEventListener("click", function () {
        [].forEach.call(tabsEl.children, function (o) { o.setAttribute("aria-selected", "false"); });
        b.setAttribute("aria-selected", "true");
        [].forEach.call(document.querySelectorAll(".pcard"), function (card) {
          card.classList.toggle("hide", t[0] !== "all" && card.dataset.cat !== t[0]);
        });
      });
      tabsEl.appendChild(b);
    });
  }

  var grid = document.getElementById("grid");
  if (grid) {
    PRODUCTS.forEach(function (p, i) {
      var card = document.createElement("article");
      card.className = "pcard frame reveal d" + (i % 4);
      card.style.setProperty("--r", "20px");
      card.style.setProperty("--acc", p.acc);
      card.style.setProperty("--acc-ink", p.ink);
      card.dataset.cat = p.cat;
      card.innerHTML =
        '<div class="pthumb tile" style="--tint:' + p.tint + '">' +
          '<span class="glyph">' + p.glyph + '</span>' + MORTAR + VEG +
          '<span class="soon">Photo coming</span>' +
        '</div>' +
        '<div class="pbody">' +
          '<p class="mr">' + p.mr + '</p>' +
          '<h3>' + p.en + '</h3>' +
          '<p>' + p.d + '</p>' +
          '<a class="ask" href="' + WA + encodeURIComponent("Namaskar! Please send me the pack sizes and price for SATVA " + p.en + ".") + '">' +
            CHAT + "Ask price on WhatsApp</a>" +
        "</div>";
      grid.appendChild(card);

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
    });
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

    // the floating WhatsApp button would sit on top of the "next up" card,
    // so it only appears once the hero has scrolled away
    var fab = document.querySelector(".wafab");
    if (fab) {
      if ("IntersectionObserver" in window) {
        new IntersectionObserver(function (es) {
          fab.classList.toggle("show", !es[0].isIntersecting);
        }, { threshold: 0.12 }).observe(hero);
      } else {
        fab.classList.add("show");
      }
    }

    paintNextUp();
    schedule();
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
