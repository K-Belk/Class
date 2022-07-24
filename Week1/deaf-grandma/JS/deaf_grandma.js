function deafGrandma() {

  const prompt = require("prompt-sync")({ sigint: true });
  let gbCounter = 0;
while (gbCounter < 2) {


const inputText = prompt("Kid: ");


if (inputText === ""){
   console.log("WHAT!");
} else if (inputText != inputText.toUpperCase()){
   console.log("SPEAK UP, KID!"); 
}   else if (inputText != "GOODBYE!" && inputText === inputText.toUpperCase()){
   console.log("NO, NOT SINCE 1946!");
}

else if ( inputText === "GOODBYE!") {
    gbCounter += 1
      if (gbCounter < 2) {
          console.log("LEAVING SO SOON?")
      } else if (gbCounter > 1) {
        gbCounter += 1
           return console.log("LATER SKATER!")   
      }
}
} //end while
console.log("all done")
}
deafGrandma();

module.exports = deafGrandma