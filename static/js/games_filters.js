// Define and run immediatly
(function () {
    // set variable to entire documen, search elements with IDs "xxx"
  const exact = document.getElementById("players_exact");
  const min = document.getElementById("players_min");
  const max = document.getElementById("players_max");
  const exactOnly = document.querySelector('input[name="players_exact_only"]');
// if any of these are missing from doc (webpage)
  if (!exact || !min || !max) return;

// Helper: true if an input has some value typed in it
  function hasValue(el) {
    return el && el.value.trim() !== "";
  }  

// When user types into EXACT:
// - if exact has value, clear values in range (min/max)
  function onExactInput() {
    if (hasValue(exact)) {
      min.value = "";
      max.value = "";
      // do NOT auto-tick exactOnly
    } else {
      // if exact becomes empty, "fixed only" doesnt make sense
      if (exactOnly) exactOnly.checked = false;
    }
  }

// When user types into RANGE (min or max):
// - if range has value, clear value in "exact" + untick checkbox
  function onRangeInput() {
    const rangeHasValue = hasValue(min) || hasValue(max);
    if (rangeHasValue) {
      exact.value = "";
      if (exactOnly) exactOnly.checked = false;
    }
  }

// When user clicks the checkbox:
// - if ticking it ON, clear range
// -if exact is empty, don't allow it to stay checked
  function onExactOnlyChange() {
    if (!exactOnly) return;

    if (exactOnly.checked) {
      // cant be "fixed only" without an exact value
      if (!hasValue(exact)) {
        exactOnly.checked = false;
        return;
      }
      // fixed-only mode uses exact; clear range
      min.value = "";
      max.value = "";
    }
  }

// Wire up events
  exact.addEventListener("input", function () {
    onExactInput();
  });

  min.addEventListener("input", function () {
    onRangeInput();
  });

  max.addEventListener("input", function () {
    onRangeInput();
  });

  if (exactOnly) {
    exactOnly.addEventListener("change", function () {
      onExactOnlyChange();
    });
  }
})();

(function () {
  const age = document.getElementById("age_min");
  const ageUnknown = document.getElementById("age_include_unknown");

  if (!age || !ageUnknown) return;

  function syncAgeUnknownCheckbox() {
    const hasAge = age.value.trim() !== "";

    ageUnknown.disabled = !hasAge;

    // If age is cleared, also untick the checkbox (so it can't submit "on" with no age)
    if (!hasAge) ageUnknown.checked = false;
  }

  // Enable/disable immediately while typing
  age.addEventListener("input", syncAgeUnknownCheckbox);

  // Run once on page load (covers refresh / back button)
  syncAgeUnknownCheckbox();
})()

/* I cannot deal with this nonses anymore JS script sucks big time
//declare funxtion
  function syncPlayersInputs() {
    // whatever is typed but remove blank space and cannot be empty string
    const hasExact = exact.value.trim() !== "";
    const hasRange = min.value.trim() !== "" || max.value.trim() !== "";

    // If exact is used, disable range
    min.disabled = hasExact;
    max.disabled = hasExact;
    
    // If range is used, disable exact
    exact.disabled = hasRange;

    // Checkbox rule
    // - only usable when exact has value
    // -if range becomes active, force untick
    if (exactOnly) {
      exactOnly.disabled = !hasExact || hasRange;
      if (!hasExact || hasRange) exactOnly.checked = false;
    }
  }

  exact.addEventListener("input", function () {
    // if user types range, untick "exact only"
  if (exact.value.trim() !== "") {
    min.value = "";
    max.value = "";
    }
    syncPlayersInputs();
  });

  // Typing range clears exact + unticks checkbox
  function onRangeInput() {
    const hasRange = min.value.trim() !== "" || max.value.trim() !== "";
    if (hasRange) {
      exact.value = "";
      if (exactOnly) exactOnly.checked = false;
    }
    syncPlayersInputs();
  }

  min.addEventListener("input", onRangeInput);
  max.addEventListener("input", onRangeInput);

  syncPlayersInputs();
})();
*/
