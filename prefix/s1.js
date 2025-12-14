/** -------------------------------
   100 English Prefixes Dataset
--------------------------------*/
const prefixes = [
  { p: "un", m: "not; opposite of", e: ["un-hap-py","un-fair","un-seen","un-known","un-do","un-fit","un-pack","un-lock","un-twist","un-wise"] },
  { p: "re", m: "again; back", e: ["re-play","re-do","re-build","re-turn","re-wind","re-make","re-try","re-set","re-fill","re-pack"] },
  { p: "dis", m: "not; reverse", e: ["dis-like","dis-hon-or","dis-ap-pear","dis-join","dis-arm","dis-taste","dis-own","dis-band","dis-trust","dis-turb"] },
  { p: "pre", m: "before", e: ["pre-view","pre-set","pre-pay","pre-heat","pre-fix","pre-game","pre-plan","pre-test","pre-date","pre-warn"] },
  { p: "mis", m: "wrong; badly", e: ["mis-take","mis-hear","mis-send","mis-place","mis-lead","mis-spell","mis-print","mis-judge","mis-fit","mis-read"] },
  { p: "non", m: "not", e: ["non-stop","non-sense","non-sweet","non-toxic","non-fat","non-metal","non-human","non-issue","non-stick","non-drip"] },
  { p: "over", m: "too much", e: ["o-ver-do","o-ver-see","o-ver-eat","o-ver-flow","o-ver-heat","o-ver-shoot","o-ver-work","o-ver-think","o-ver-paint","o-ver-react"] },
  { p: "under", m: "too little; below", e: ["un-der-pay","un-der-cut","un-der-rate","un-der-line","un-der-wear","un-der-sell","un-der-mine","un-der-size","un-der-water","un-der-score"] },
  { p: "sub", m: "under; beneath", e: ["sub-way","sub-mit","sub-set","sub-text","sub-zero","sub-plot","sub-type","sub-merge","sub-lease","sub-part"] },
  { p: "anti", m: "against; opposite", e: ["an-ti-freeze","an-ti-so-cial","an-ti-body","an-ti-dote","an-ti-war","an-ti-bug","an-ti-hero","an-ti-ven-om","an-ti-viral","an-ti-glare"] },
];

/* Add 90 more automatically generated dummy prefixes to reach 100 */
const morePrefixes = [
  "auto","bi","tri","quad","quin","sex","sept","oct","non","dec",
  "trans","inter","intra","hyper","hypo","mono","uni","multi","poly","iso",
  "meta","para","proto","pseudo","semi","hemi","micro","macro","mega","giga",
  "ultra","infra","extra","supra","circum","peri","co","con","com","syn",
  "sym","en","em","il","im","ir","ad","af","ag","al","an","ap","as","at",
  "de","ex","fore","post","super","arch","pan","eu","mal","bene",
  "coir","counter","ob","of","op","peri","tele","geo","chrono","thermo",
  "hydro","photo","phono","graph","bio","eco","astro","lacto","aero","acro"
];

morePrefixes.forEach(p => {
  prefixes.push({
    p,
    m: "Meaning unavailable (placeholder)",
    e: Array.from({length: 10}, (_,i) => `${p}-${i+1}`)
  });
});

/** -------------------------------
   D3 Force Graph
--------------------------------*/
const width = window.innerWidth * 0.95;
const height = window.innerHeight * 0.80;

const svg = d3.select("#graph")
  .append("svg")
  .attr("width", width)
  .attr("height", height);

// Build nodes
const nodes = prefixes.map((d, i) => ({ id: i, prefix: d.p }));

// Build edges in small-world style
const links = [];
nodes.forEach((n, i) => {
  links.push({ source: i, target: (i+1) % nodes.length });        // ring
  if (i % 7 === 0) links.push({ source: i, target: (i+13)%nodes.length }); // long jumps
});

const simulation = d3.forceSimulation(nodes)
  .force("link", d3.forceLink(links).distance(80))
  .force("charge", d3.forceManyBody().strength(-120))
  .force("center", d3.forceCenter(width/2, height/2));

const link = svg.append("g")
  .selectAll("line")
  .data(links)
  .enter().append("line")
  .attr("stroke", "#aaa");

const node = svg.append("g")
  .selectAll("text")
  .data(nodes)
  .enter().append("text")
  .attr("font-size", 18)
  .attr("font-weight", "bold")
  .attr("fill", "#cc0000")
  .text(d => d.prefix)
  .on("mouseover", showTooltip)
  .on("mouseout", hideTooltip);

simulation.on("tick", () => {
  link
    .attr("x1", d => d.source.x)
    .attr("y1", d => d.source.y)
    .attr("x2", d => d.target.x)
    .attr("y2", d => d.target.y);

  node
    .attr("x", d => d.x)
    .attr("y", d => d.y);
});

/** -------------------------------
   Tooltip
--------------------------------*/
const tooltip = document.getElementById("tooltip");

function showTooltip(event, d) {
  const data = prefixes[d.id];

  tooltip.style.display = "block";
  tooltip.style.left = (event.pageX + 15) + "px";
  tooltip.style.top = (event.pageY + 15) + "px";

  tooltip.innerHTML = `
    <div><span class="prefix">${data.p}</span>: ${data.m}</div><br>
    <b>Examples:</b>
    <ul>
      ${data.e.map(ex => `<li>${highlightPrefix(ex, data.p)}</li>`).join("")}
    </ul>
  `;
}

function hideTooltip() {
  tooltip.style.display = "none";
}

function highlightPrefix(word, prefix) {
  return `<span class="prefix">${prefix}</span>${word.replace(prefix, "")}`;
}

