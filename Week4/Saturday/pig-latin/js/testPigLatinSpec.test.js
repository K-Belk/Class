
var pig = require("./pigLatin");

test("translates a word beginning with a vowel:", () => {
  expect(pig.translate("apple")).toBe("appleay")
});
test("translates a word beginning with a consonant:", () => {
  expect(pig.translate("banana")).toBe("ananabay")
});
test("translates a word beginning with two consonants:", () => {
  expect(pig.translate("cherry")).toBe("errychay")
});
test("translates two words:", () => {
  expect(pig.translate("eat pie")).toBe("eatay iepay")
});
test("translates a word beginning with three consonants:", () => {
  expect(pig.translate("three")).toBe("eethray")
});
test("counts 'sch' as a single phoneme:", () => {
  expect(pig.translate("school")).toBe("oolschay")
});
test("counts 'qu' as a single phoneme:", () => {
  expect(pig.translate("quiet")).toBe("ietquay")
});
test("counts 'qu' as a consonant even when it's preceded by a consonant:", () => {
expect(pig.translate("square")).toBe("aresquay")
});
test("translates many words:", () => {
  expect(pig.translate("the quick brown fox")).toBe("ethay ickquay ownbray oxfay")
});

// write a test asserting that capitalized words are still capitalized
// (but with a different initial capital letter, of course) retain the
// punctuation from the original phrase
