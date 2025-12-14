// script.js
const prefixes = [
  {
    prefix: "un",
    meaning: "A prefix meaning 'not' or 'opposite of'.",
    examples: ["unhappy", "unfair", "unpredictable", "undo", "unseen", "unheard", "unfortunate", "unnecessary", "unfamiliar", "untouchable"]
  },
  {
    prefix: "re",
    meaning: "A prefix meaning 'again' or 'back'.",
    examples: ["replay", "rebuild", "revisit", "react", "recharge", "reboot", "reaffirm", "revise", "recreate", "reconsider"]
  },
  {
    prefix: "dis",
    meaning: "A prefix meaning 'not' or 'opposite of'.",
    examples: ["disagree", "dishonor", "disappear", "disconnect", "dislike", "displace", "disprove", "disrupt", "discontent", "disorder"]
  },
  // Add more prefixes as needed
];

// Function to create the prefix graph
function createPrefixGraph() {
  const graphContainer = document.getElementById("prefix-graph");

  prefixes.forEach(prefix => {
    const li = document.createElement("li");
    li.classList.add("prefix-item");
    li.textContent = prefix.prefix;
    li.addEventListener("mouseover", () => showTooltip(prefix));
    graphContainer.appendChild(li);
  });
}

// Function to show the tooltip with the prefix meaning and examples
function showTooltip(prefix) {
  const tooltip = document.getElementById("tooltip");
  const prefixMeaning = document.getElementById("prefix-meaning");
  const prefixExamples = document.getElementById("prefix-examples");

  // Set the prefix meaning
  prefixMeaning.textContent = prefix.meaning;

  // Clear any previous examples
  prefixExamples.innerHTML = '';

  // Add the example words separated by syllables
  prefix.examples.forEach(example => {
    const li = document.createElement("li");
    li.innerHTML = separateSyllables(example);
    prefixExamples.appendChild(li);
  });

  // Position the tooltip near the hovered prefix
  tooltip.style.display = "block";
  tooltip.style.left = `${event.pageX + 10}px`;
  tooltip.style.top = `${event.pageY + 10}px`;
}

// Function to separate syllables in a word (basic example)
function separateSyllables(word) {
  // This is a very basic syllable separator using hyphens as an example.
  // A more sophisticated syllable separation would require NLP techniques or APIs.
  return word.replace(/([aeiouy]{1,2})(?=[^aeiouy])/g, "$1-");
}

// Hide the tooltip when mouse leaves the prefix
document.addEventListener("mousemove", (event) => {
  const tooltip = document.getElementById("tooltip");
  tooltip.style.display = "none";
});

// Initialize the graph when the page loads
window.onload = createPrefixGraph;

