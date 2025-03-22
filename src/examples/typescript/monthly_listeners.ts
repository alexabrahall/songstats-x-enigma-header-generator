import axios from "axios";

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

async function getSongStatsListeners(
  artistName: string,
  city: string,
  country?: string
) {
  const headers = {
    accept: "application/json",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "fe-build-timestamp": Date.now().toString(), //this will fetch the newest data
    "fe-platform": "web",
    "fe-version": "143",
    origin: "https://songstats.com/",
    pragma: "no-cache",
    priority: "u=1, i",
    referer: "https://songstats.com/",
    "sec-ch-ua":
      '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent":
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "x-enigma": generateXEnigma(), //generate a new x-enigma for each request as it expires very quickly
  };

  let searchReq = await axios.get(
    `https://data.songstats.com/api/v1/search/search_all?q=${encodeURIComponent(
      artistName
    )}&excludedModels=RadioStation`,
    { headers }
  );

  let resp = searchReq.data;
  let artistId = resp.results[0].idUnique;
  const params = {
    idUnique: artistId,
    source: "spotify",
  };

  try {
    const response = await axios.get(
      "https://data.songstats.com/api/v1/audience/map_stats",
      {
        params,
        headers,
      }
    );
    let resp = response.data;

    //get the number of listeners for city
    let cityListeners = resp.mapStats[0].data.rows
      .find((row) => row.countryCode === country || row.countryCode === "GB")
      ?.rowGroup.find((row) => row.cityName === city)?.cells[1].displayText;

    return cityListeners;
  } catch (error) {
    console.error("Error fetching SongStats listeners:", error);
    return null;
  }
}

(async () => {
  const listeners = await getSongStatsListeners("The Weeknd", "London");
  console.log(`The Weeknd has ${listeners} listeners in London`);
})();
