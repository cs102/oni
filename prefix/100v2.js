// Define Prefixes, Categories, Definitions, and Examples
const prefixData = [
    { "name": "un-", "category": "Negation", "definition": "Not or opposite of", "examples": ["unhappy", "unseen"] },
    { "name": "in-", "category": "Negation", "definition": "Not, without", "examples": ["invisible", "insecure"] },
    { "name": "im-", "category": "Negation", "definition": "Not or opposite of", "examples": ["impossible", "impatient"] },
    { "name": "dis-", "category": "Negation", "definition": "Reverse, opposite of", "examples": ["disagree", "disconnect"] },
    { "name": "non-", "category": "Negation", "definition": "Not", "examples": ["nonprofit", "nonexistent"] },
    { "name": "bi-", "category": "Quantity", "definition": "Two", "examples": ["bicycle", "biannual"] },
    { "name": "mono-", "category": "Quantity", "definition": "One", "examples": ["monologue", "monarch"] },
    { "name": "poly-", "category": "Quantity", "definition": "Many", "examples": ["polygon", "polyglot"] },
    { "name": "multi-", "category": "Quantity", "definition": "Many, multiple", "examples": ["multimedia", "multipurpose"] },
    { "name": "duo-", "category": "Quantity", "definition": "Two", "examples": ["duo", "duet"] },
    { "name": "micro-", "category": "Size/degree", "definition": "Small", "examples": ["microscope", "microphone"] },
    { "name": "mega-", "category": "Size/degree", "definition": "Large", "examples": ["megabyte", "megaton"] },
    { "name": "giga-", "category": "Size/degree", "definition": "Billion", "examples": ["gigabyte", "gigawatt"] },
    { "name": "centi-", "category": "Size/degree", "definition": "Hundredth", "examples": ["centimeter", "centiliter"] },
    { "name": "milli-", "category": "Size/degree", "definition": "Thousandth", "examples": ["millisecond", "milligram"] },
    { "name": "pre-", "category": "Time", "definition": "Before", "examples": ["preorder", "precondition"] },
    { "name": "post-", "category": "Time", "definition": "After", "examples": ["postmortem", "postpone"] },
    { "name": "sub-", "category": "Time", "definition": "Under, below", "examples": ["submarine", "subordinate"] },
    { "name": "inter-", "category": "Time", "definition": "Between", "examples": ["internet", "international"] },
    { "name": "ante-", "category": "Time", "definition": "Before", "examples": ["antecedent", "antebellum"] },
    { "name": "re-", "category": "Direction", "definition": "Again", "examples": ["revisit", "rewrite"] },
    { "name": "anti-", "category": "Direction", "definition": "Against", "examples": ["antibiotic", "antagonist"] },
    { "name": "auto-", "category": "Direction", "definition": "Self", "examples": ["autonomous", "autograph"] },
    { "name": "counter-", "category": "Direction", "definition": "Opposite", "examples": ["counteract", "counterclockwise"] },
    { "name": "co-", "category": "Direction", "definition": "Together, with", "examples": ["coexist", "cooperate"] },
    { "name": "ex-", "category": "Direction", "definition": "Out of", "examples": ["extract", "exclude"] },
    { "name": "trans-", "category": "Direction", "definition": "Across", "examples": ["transport", "transform"] },
    { "name": "super-", "category": "Size/degree", "definition": "Above, beyond", "examples": ["superhuman", "supernatural"] },
    { "name": "ultra-", "category": "Size/degree", "definition": "Beyond, extreme", "examples": ["ultra-modern", "ultrasonic"] },
    { "name": "hyper-", "category": "Size/degree", "definition": "Excessive", "examples": ["hyperactive", "hyperbole"] },
    // Add more prefixes up to 100 as needed
];

// Force-Directed Graph Layout
const width = window.innerWidth;
const height = window.innerHeight;

const svg = d3.select("#tree-container")
              .append("svg")
              .attr("width", width)
              .attr("height", height);

// Tooltip for displaying prefix definitions
const tooltip = d3.select("#tooltip");

// Create a simulation for the force-directed graph
const simulation = d3.forceSimulation(prefixData)
                     .force("charge", d3.forceManyBody().strength(-200)) // Repels nodes from each other
                     .force("center", d3.forceCenter(width / 2, height / 2)); // Centers the graph

// Create nodes
const node = svg.append("g")
                .selectAll(".node")
                .data(prefixData)
                .enter().append("g")
                .attr("class", "node")
                .call(d3.drag()
                    .on("start", dragstarted)
                    .on("drag", dragged)
                    .on("end", dragended));

node.append("circle")
    .attr("r", 15)
    .on("mouseover", function(event, d) {
        tooltip.style("display", "inline")
               .html(`<strong>${d.name}</strong><br>Definition: ${d.definition}<br>Examples: ${d.examples.join(", ")}`);
    })
    .on("mousemove", function(event) {
        tooltip.style("top", (event.pageY + 5) + "px")
               .style("left", (event.pageX + 5) + "px");
    })
    .on("mouseout", function() {
        tooltip.style("display", "none");
    });

node.append("text")
    .attr("dy", -20)
    .attr("text-anchor", "middle")
    .text(d => d.name);

// Start the simulation
simulation.nodes(prefixData).on("tick", ticked);

// Update the positions of the nodes during the simulation
function ticked() {
    node.attr("transform", d => `translate(${d.x},${d.y})`);
}

// Drag functions
function dragstarted(event, d) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged(event, d) {
    d.fx = event.x;
    d.fy = event.y;
}

function dragended(event, d) {
    if (!event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}

</script>

</body>
</html>

