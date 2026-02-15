// Define and run immediatly
(function () {
    // set variable to entire documen, search elements with IDs "xxx"
  const exact = document.getElementById("players_exact");
  const min = document.getElementById("players_min");
  const max = document.getElementById("players_max");
  const exactOnly = document.querySelector('input[name="players_exact_only"]');
// if any of these are missing from doc (webpage)
  if (!exact || !min || !max) return;
//declare funxtion
  function syncPlayersInputs() {
    // whatever is typed but remove blank space and cannot be empty string
    const hasExact = exact.value.trim() !== "";

    min.disabled = hasExact;
    max.disabled = hasExact;
// only if checkbox is present (RECONSIDER change it!)
    if (exactOnly) {
      exactOnly.disabled = !hasExact;
      // check if checbox is ticked
      if (!hasExact) exactOnly.checked = false;
    }
  }
// even listener
  exact.addEventListener("input", syncPlayersInputs);
  // calls as soon as page loads
  syncPlayersInputs();
})();
