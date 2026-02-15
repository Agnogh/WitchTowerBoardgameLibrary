// Define and run immediatly
(function () {
    // set variable to entire documen, search elements with IDs "xxx"
  const exact = document.getElementById("players_exact");
  const min = document.getElementById("players_min");
  const max = document.getElementById("players_max");
  const exactOnly = document.querySelector('input[name="players_exact_only"]');
// if any of these are missing from doc (webpage)
  if (!exact || !min || !max) return;

  function hasValue(el) {
    return el && el.value.trim() !== "";
  }

//declare funxtion
  function syncPlayersInputs() {
    // whatever is typed but remove blank space and cannot be empty string
    // const hasExact = exact.value.trim() !== "";
    const hasExact = hasValue(exact);
    const hasRange = hasValue(min) || hasValue(max);
    // if exact is used, then range is dispbled 
    min.disabled = hasExact;
    max.disabled = hasExact;

    // If range is used, then exact is disabled
    exact.disabled = hasRange;

// only if checkbox is present (RECONSIDER change it!)
    if (exactOnly) {
      exactOnly.disabled = !hasExact || hasRange;
      if (!hasExact || hasRange) exactOnly.checked = false;
    }
  }
// typing in range clears the exact (and vice verse)
  exact.addEventListener("input", function () {
    // if any of these are have values clear them
    if (hasValue(exact)) {
      min.value = "";
      max.value = "";
    }
    // call so fileds/checkbox get disable or enabled
    syncPlayersInputs();
  });
  //define funxtion that runs
  function onRangeInput() {
    // if min or max  is typed
    if (hasValue(min) || hasValue(max)) {
      // clear exact field 
      exact.value = "";
      // untick/unmark checkbox (exact only doesn't apply anymore)
      if (exactOnly) exactOnly.checked = false;
    }
    syncPlayersInputs();
  }
  // run if either min or max is typed
  min.addEventListener("input", onRangeInput);
  max.addEventListener("input", onRangeInput);

  // Run on page load
  syncPlayersInputs();
})();