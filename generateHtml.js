const fs = require("fs");

let data = require("./images/results.json");

const html = Object.entries(data).map(([img, duplicits]) => {
  const duplicitsHtml = duplicits
    .sort((a, b) => b[1] - a[1])
    .map(([duplicitImg, threshold]) => {
      return `<td><img src="images/${duplicitImg}" /><br />${threshold}</td>`;
    });
  return `<tr><th><img src="images/${img}" /></th>${duplicitsHtml}</tr>`;
});

const styles = `<style>img { max-width: 300px; max-height: 300px } th { background-color: gray; padding: 1rem } </style>`;

fs.writeFileSync("index.html", `${styles}<table>${html}</table>`);
