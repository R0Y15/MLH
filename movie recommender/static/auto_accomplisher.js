new auto_accomplisher({
    data: {                              // Data src [Array, Function, Async] | (REQUIRED)
      src: films,
    },
    selector: "#auto_accomplisher",           // Input field selector              | (Optional)
    threshold: 2,                        // Min. Chars length to start Engine | (Optional)
    debounce: 100,                       // Post duration for engine to start | (Optional)
    searchEngine: "strict",              // Search Engine type/mode           | (Optional)
    resultsList: {                       // Rendered results list object      | (Optional)
        render: true,
        container: source => {
            source.setAttribute("id", "food_list");
        },
        destination: document.querySelector("#auto_accomplisher"),
        position: "afterend",
        element: "ul"
    },
    maxResults: 5,                         // Max. number of rendered results | (Optional)
    highlight: true,                       // Highlight matching results      | (Optional)
    resultItem: {                          // Rendered result item            | (Optional)
        content: (data, source) => {
            source.innerHTML = data.match;
        },
        element: "li"
    },
    noResults: () => {                     // Action script on noResults      | (Optional)
        const result = document.createElement("li");
        result.setAttribute("class", "no_result");
        result.setAttribute("tabindex", "1");
        result.innerHTML = "No Results";
        document.querySelector("#auto_accomplisher_list").appendChild(result);
    },
    onSelection: feedback => {             // Action script onSelection event | (Optional)
        document.getElementById('auto_accomplisher').value = feedback.selection.value;
    }
});