
var cs = require("./caesarCipher");

test("Boy! What a string!", () => {
  expect(cs.caesarCipher("Boy! What a string!", -5)).toBe("Wjt! Rcvo v nomdib!")
})

test("Hello zach168! Yes here.", () => {
  expect(cs.caesarCipher("Hello zach168! Yes here.", 5)).toBe("Mjqqt efhm168! Djx mjwj.")
})

test("Hello Zach168! Yes here.", () => {
  expect(cs.caesarCipher("Hello Zach168! Yes here.", -5)).toBe("Czggj Uvxc168! Tzn czmz.")
})
