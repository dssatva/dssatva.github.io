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
    { mr:"हळद", en:"Haldi", glyph:"हळ",
      d:"The everyday base of every Maharashtrian kitchen — bhaji, varan, amti.",
      img:"assets/p-haldi.jpg", tint:"linear-gradient(150deg,#e3ae3c,#c1860f)" },
    { mr:"लाल तिखट", en:"Mirchi Powder", glyph:"ति",
      d:"Colour and heat, ground from whole dried chillies.",
      img:"assets/p-mirchi.jpg", tint:"linear-gradient(150deg,#cf5238,#a8321b)" },
    { mr:"धणे पूड", en:"Coriander Powder", glyph:"धणे",
      d:"Warm and nutty — the quiet base under a good rassa.",
      img:"assets/p-dhane.jpg", tint:"linear-gradient(150deg,#bcae63,#948537)" },
    { mr:"काळा मसाला", en:"Premium Kala Masala", glyph:"काळा",
      d:"The dark roasted Marathwada blend that makes a rassa taste like home.",
      img:"assets/p-kala.jpg", tint:"linear-gradient(150deg,#8d7a55,#635232)" },
    { mr:"कांदा लसूण मसाला", en:"Kanda Lasun Masala", glyph:"कां",
      d:"Onion, garlic and chilli — what a misal or usal cannot do without.",
      img:"assets/p-kandalasun.jpg", tint:"linear-gradient(150deg,#d1674a,#b03f24)" },
    { mr:"शेंगदाणा चटणी", en:"Groundnut Chutney", glyph:"शें",
      d:"Dry groundnut chutney for bhakri, thalipeeth and a bowl of dahi.",
      img:"assets/p-shengdana.jpg", tint:"linear-gradient(150deg,#dd9a4e,#bf7420)" },
    { mr:"जवस चटणी", en:"Javas Chutney", glyph:"ज",
      d:"Roasted flaxseed chutney — earthy, nutty, and gone before you expect.",
      img:"assets/p-javas.jpg", tint:"linear-gradient(150deg,#b3a05c,#8d7a32)" },
    { mr:"कारळे चटणी", en:"Karala Chutney", glyph:"का",
      d:"Niger-seed chutney, the Marathwada favourite alongside bhakri.",
      img:"assets/p-karala.jpg", tint:"linear-gradient(150deg,#9aa07a,#727950)" }
  ];

  var MORTAR = '<svg class="mortar" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 11h14a7 7 0 0 1-7 7 7 7 0 0 1-7-7Z"/><path d="M12 18v3M8 21h8"/><path d="M16 8.5 19 4"/></svg>';
  var CHAT = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.2-1.8-.9-2.1-1-.3-.1-.5-.2-.7.1s-.8 1-1 1.2c-.2.2-.4.3-.7.1a8.2 8.2 0 0 1-2.4-1.5 9.1 9.1 0 0 1-1.7-2.1c-.2-.3 0-.5.1-.7l.6-.7c.1-.2.2-.4.1-.6l-.9-2.1c-.2-.5-.4-.5-.6-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.1 1.1-1.1 2.6s1.1 3 1.3 3.2c.1.2 2 3.2 4.9 4.4 2.4 1 2.9.8 3.4.8.5-.1 1.7-.7 1.9-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.2-.6-.4zM12 21.5c-1.7 0-3.4-.5-4.9-1.3l-3.4.9.9-3.3A9.4 9.4 0 0 1 2.6 12 9.4 9.4 0 0 1 12 2.6 9.4 9.4 0 0 1 21.4 12 9.4 9.4 0 0 1 12 21.5z"/></svg>';
  var VEG = '<span class="veg" title="Vegetarian"><i></i></span>';

  var grid = document.getElementById("grid");
  if (grid) {
    PRODUCTS.forEach(function (p, i) {
      var card = document.createElement("article");
      card.className = "pcard frame reveal d" + (i % 4);
      card.style.setProperty("--r", "20px");
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
