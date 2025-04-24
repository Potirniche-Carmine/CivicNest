export interface houses {
    zpid: number;
    address: string;
    lat: number;
    long: number;
    price: number;
    bedrooms: number;
    bathrooms: number;
    zipcode: string;
    cluster_id?: number | null;
}

export interface EmploymentPrediction {
    zipcode: string;
    percent_change: string;
    houses: Array<{
        zpid: string;
    }>;
}

export interface ZipInsightData {
    zipcode: number;
    pct_cluster_1: string;
    pct_cluster_2: string;
    pct_cluster_3: string;
    pct_cluster_4: string;
    assigned_cluster: number;
    median_price: number;
    affordability_ratio: number;
    employment_growth: string; 
  }

  export interface ClusterInsightData {
    cluster_id: number;
    avg_payroll: string;
    median_price: string;
    affordability_ratio: number;
    employment_growth: string; 
}

export interface GeneratedInsight {
    title: string;
    explanation: string;
}

export interface GeneratedZipInsight {
    title: string;
    explanation: string;
}

export interface ZipcodeSpecificData {
  col_index: number | null;
  demographics: {
    median_age: number | null;
    school_enrollment_total: number | null;
  };
  schoolRatings: {
    poorly_rated_elementary: number | null;
    poorly_rated_middle: number | null;
    poorly_rated_high: number | null;
  };
}