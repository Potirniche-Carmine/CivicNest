import { Map } from '@/components/zipcodemap'; 

type ZipcodePageProps = {
  params: { zip: string }; 
};

export default async function ZipcodePage({ params }: ZipcodePageProps) {
  const awaitedParams = await params;
  const id = awaitedParams.zip;

  return (
    <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-4"> 
      <h1 className="text-2xl font-semibold mb-4">Houses in Zipcode {id}</h1> 
      <Map zipcode={id} />
    </div>
  );
}