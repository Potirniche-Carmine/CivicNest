import fetch from 'node-fetch';

// Define a type for house data (based on Zillow's API response structure)
interface House {
  id: string
  address: string;
  price: number;
  latitude: number;
  longitude: number;
  // Include additional fields as needed based on the Zillow API response
}

interface ZillowListing{
  results: House[];
}

interface ZestimateAPIResponse{
  zestimate: number;
}

export const fetchZillowListings = async (): Promise<House[] | null>  => {
    const url = 'https://zillow-com1.p.rapidapi.com/search?polygon=34.03959576441558%20-118.50636536779786%2C34.0418716916327%20-118.50276047888184%2C34.042440663894304%20-118.49846894445801%2C34.04201393505594%20-118.49417741003418%2C34.04087598099002%20-118.4897142142334%2C34.03945351693672%20-118.48525101843262%2C34.03788877892429%20-118.48095948400879%2C34.03618175908096%20-118.47683961096192%2C34.034190192514366%20-118.47271973791504%2C34.031629538228394%20-118.46962983312989%2C34.02835747861639%20-118.4677415579834%2C34.02465847668084%20-118.46671158972168%2C34.02081703478521%20-118.46636826696778%2C34.01697541902413%20-118.46636826696778%2C34.01341821237762%20-118.4673982352295%2C34.011283816847104%20-118.47100312414551%2C34.01057233974687%20-118.47563798132325%2C34.01043004361143%20-118.47992951574707%2C34.01071463564384%20-118.48439271154786%2C34.01156840601794%20-118.48868424597168%2C34.01270675316253%20-118.49297578039551%2C34.01398737545716%20-118.49709565344239%2C34.01555255425154%20-118.50104386511231%2C34.01754455825562%20-118.50464875402832%2C34.02039019717532%20-118.50756699743653%2C34.02352028980117%20-118.50962693395996%2C34.02707707311613%20-118.51065690222168%2C34.03063370735633%20-118.50997025671387%2C34.034190192514366%20-118.5091119498291%2C34.03774652858273%20-118.50825364294434%2C34.03959576441558%20-118.50636536779786&output=json&status=forSale&sortSelection=priorityscore&listing_type=by_agent&doz=any';
    const options = {
      method: 'GET',
      headers: {
        'x-rapidapi-key': 'eb433fb3e6msh6f40dfa8c7810a1p1587fbjsn9ddafafaa1a5',
        'x-rapidapi-host': 'zillow-com1.p.rapidapi.com'
      }
    };
    
    try {
        const response = await fetch(url, options);
        const data = await response.json() as ZillowListing;
        const house = data.results;
        console.log(data);

        const housesWithZestimate = await Promise.all(
          house.map(async (house) =>{
            const zestimate = await fetchZestimate(house.id);
            return{...house,zestimate};
          })
        );
        return housesWithZestimate;
    } catch (error) {
        console.error(error)
        return null;
    }
}

export const fetchZestimate = async (houseId: string): Promise<number | null> => {
  const url = `https://zillow-com1.p.rapidapi.com/zestimate?zpid=${houseId}`;
  const options = {
    method: 'GET',
    headers: {
      'x-rapidapi-key': process.env.RAPIDAPI_KEY || '',
      'x-rapidapi-host': 'zillow-com1.p.rapidapi.com'
    }
  };

  try {
    const response = await fetch(url, options);
    const data = await response.json() as ZestimateAPIResponse;
    return data.zestimate;
  } catch (error) {
    console.error(`Error fetching Zestimate for house ID ${houseId}`, error);
    return null;
  }
};

