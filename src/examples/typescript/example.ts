function generateXEnigma(): string {
  const f = (e: string): number[] => e.split("").map((e) => e.charCodeAt(0));
  const baitString = "<img src='/getbaited.jpg' />";
  const baitBytes = f(baitString);

  let o = {
    W3: (e: string): number[] => e.split("").map((e) => e.charCodeAt(0)),
    n5: (e: number[]): number =>
      baitBytes.reduce((acc: number, curr: number) => acc ^ curr, e[0] || 0),
    _t: (e: number): string => ("0" + Number(e).toString(16)).substr(-2),
  };

  return String(420 * Date.now() + 69)
    .split("")
    .map(o.W3)
    .map(o.n5)
    .map(o._t)
    .join("");
}

(async () => {
  const xEnigma = generateXEnigma();

  console.log(xEnigma);
})();
