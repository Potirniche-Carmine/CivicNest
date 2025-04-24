import '@testing-library/jest-dom';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import HouseSelect from '@/components/house_select';
import * as themes from 'next-themes';
import { houses } from '@/lib/types';

// Mock fetch
global.fetch = jest.fn();

// Mock next-themes
jest.mock('next-themes');
const mockedUseTheme = jest.mocked(themes.useTheme);

describe('HouseSelect Component', () => {
  const mockHouses: houses[] = [
    { address: '123 Main St', lat: 40.7128, long: -74.0060, price: 500000, zpid: 1 },
    { address: '456 Elm St', lat: 34.0522, long: -118.2437, price: 750000, zpid: 2 },
    { address: '789 Oak Ave', lat: 41.8781, long: -87.6298, price: 600000, zpid: 3 },
    { address: 'House 4 St', lat: 35.0400, long: -119.9600, price: 404000, zpid: 4 },
    { address: 'House 5 St', lat: 35.0500, long: -119.9500, price: 405000, zpid: 5 },
    { address: 'House 6 St', lat: 35.0600, long: -119.9400, price: 406000, zpid: 6 },
    { address: 'House 7 St', lat: 35.0700, long: -119.9300, price: 407000, zpid: 7 },
    { address: 'House 8 St', lat: 35.0800, long: -119.9200, price: 408000, zpid: 8 },
    { address: 'House 9 St', lat: 35.0900, long: -119.9100, price: 409000, zpid: 9 },
    { address: 'House 10 St', lat: 35.1000, long: -119.9000, price: 410000, zpid: 10 },
    { address: 'House 11 St', lat: 35.1100, long: -119.8900, price: 411000, zpid: 11 },
    { address: 'House 12 St', lat: 35.1200, long: -119.8800, price: 412000, zpid: 12 },
    { address: 'House 13 St', lat: 35.1300, long: -119.8700, price: 413000, zpid: 13 },
    { address: 'House 14 St', lat: 35.1400, long: -119.8600, price: 414000, zpid: 14 },
    { address: 'House 15 St', lat: 35.1500, long: -119.8500, price: 415000, zpid: 15 },
    { address: 'House 16 St', lat: 35.1600, long: -119.8400, price: 416000, zpid: 16 },
    { address: 'House 17 St', lat: 35.1700, long: -119.8300, price: 417000, zpid: 17 },
    { address: 'House 18 St', lat: 35.1800, long: -119.8200, price: 418000, zpid: 18 },
    { address: 'House 19 St', lat: 35.1900, long: -119.8100, price: 419000, zpid: 19 },
    { address: 'House 20 St', lat: 35.2000, long: -119.8000, price: 420000, zpid: 20 },
    { address: 'House 21 St', lat: 35.2100, long: -119.7900, price: 421000, zpid: 21 },
    { address: 'House 22 St', lat: 35.2200, long: -119.7800, price: 422000, zpid: 22 },
    { address: 'House 23 St', lat: 35.2300, long: -119.7700, price: 423000, zpid: 23 },
    { address: 'House 24 St', lat: 35.2400, long: -119.7600, price: 424000, zpid: 24 },
    { address: 'House 25 St', lat: 35.2500, long: -119.7500, price: 425000, zpid: 25 },
    { address: 'House 26 St', lat: 35.2600, long: -119.7400, price: 426000, zpid: 26 },
    { address: 'House 27 St', lat: 35.2700, long: -119.7300, price: 427000, zpid: 27 },
    { address: 'House 28 St', lat: 35.2800, long: -119.7200, price: 428000, zpid: 28 },
    { address: 'House 29 St', lat: 35.2900, long: -119.7100, price: 429000, zpid: 29 },
    { address: 'House 30 St', lat: 35.3000, long: -119.7000, price: 430000, zpid: 30 },
    { address: 'House 31 St', lat: 35.3100, long: -119.6900, price: 431000, zpid: 31 },
    { address: 'House 32 St', lat: 35.3200, long: -119.6800, price: 432000, zpid: 32 },
    { address: 'House 33 St', lat: 35.3300, long: -119.6700, price: 433000, zpid: 33 },
    { address: 'House 34 St', lat: 35.3400, long: -119.6600, price: 434000, zpid: 34 },
    { address: 'House 35 St', lat: 35.3500, long: -119.6500, price: 435000, zpid: 35 },
    { address: 'House 36 St', lat: 35.3600, long: -119.6400, price: 436000, zpid: 36 },
    { address: 'House 37 St', lat: 35.3700, long: -119.6300, price: 437000, zpid: 37 },
    { address: 'House 38 St', lat: 35.3800, long: -119.6200, price: 438000, zpid: 38 },
    { address: 'House 39 St', lat: 35.3900, long: -119.6100, price: 439000, zpid: 39 },
    { address: 'House 40 St', lat: 35.4000, long: -119.6000, price: 440000, zpid: 40 },
    { address: 'House 41 St', lat: 35.4100, long: -119.5900, price: 441000, zpid: 41 },
    { address: 'House 42 St', lat: 35.4200, long: -119.5800, price: 442000, zpid: 42 },
    { address: 'House 43 St', lat: 35.4300, long: -119.5700, price: 443000, zpid: 43 },
    { address: 'House 44 St', lat: 35.4400, long: -119.5600, price: 444000, zpid: 44 },
    { address: 'House 45 St', lat: 35.4500, long: -119.5500, price: 445000, zpid: 45 },
    { address: 'House 46 St', lat: 35.4600, long: -119.5400, price: 446000, zpid: 46 },
    { address: 'House 47 St', lat: 35.4700, long: -119.5300, price: 447000, zpid: 47 },
    { address: 'House 48 St', lat: 35.4800, long: -119.5200, price: 448000, zpid: 48 },
    { address: 'House 49 St', lat: 35.4900, long: -119.5100, price: 449000, zpid: 49 },
    { address: 'House 50 St', lat: 35.5000, long: -119.5000, price: 450000, zpid: 50 },
    { address: 'House 51 St', lat: 35.5100, long: -119.4900, price: 451000, zpid: 51 },
    { address: 'House 52 St', lat: 35.5200, long: -119.4800, price: 452000, zpid: 52 },
    { address: 'House 53 St', lat: 35.5300, long: -119.4700, price: 453000, zpid: 53 },
    { address: 'House 54 St', lat: 35.5400, long: -119.4600, price: 454000, zpid: 54 },
    { address: 'House 55 St', lat: 35.5500, long: -119.4500, price: 455000, zpid: 55 },
    { address: 'House 56 St', lat: 35.5600, long: -119.4400, price: 456000, zpid: 56 },
    { address: 'House 57 St', lat: 35.5700, long: -119.4300, price: 457000, zpid: 57 },
    { address: 'House 58 St', lat: 35.5800, long: -119.4200, price: 458000, zpid: 58 },
    { address: 'House 59 St', lat: 35.5900, long: -119.4100, price: 459000, zpid: 59 },
    { address: 'House 60 St', lat: 35.6000, long: -119.4000, price: 460000, zpid: 60 },
    { address: 'House 61 St', lat: 35.6100, long: -119.3900, price: 461000, zpid: 61 },
    { address: 'House 62 St', lat: 35.6200, long: -119.3800, price: 462000, zpid: 62 },
    { address: 'House 63 St', lat: 35.6300, long: -119.3700, price: 463000, zpid: 63 },
    { address: 'House 64 St', lat: 35.6400, long: -119.3600, price: 464000, zpid: 64 },
    { address: 'House 65 St', lat: 35.6500, long: -119.3500, price: 465000, zpid: 65 },
    { address: 'House 66 St', lat: 35.6600, long: -119.3400, price: 466000, zpid: 66 },
    { address: 'House 67 St', lat: 35.6700, long: -119.3300, price: 467000, zpid: 67 },
    { address: 'House 68 St', lat: 35.6800, long: -119.3200, price: 468000, zpid: 68 },
    { address: 'House 69 St', lat: 35.6900, long: -119.3100, price: 469000, zpid: 69 },
    { address: 'House 70 St', lat: 35.7000, long: -119.3000, price: 470000, zpid: 70 },
    { address: 'House 71 St', lat: 35.7100, long: -119.2900, price: 471000, zpid: 71 },
    { address: 'House 72 St', lat: 35.7200, long: -119.2800, price: 472000, zpid: 72 },
    { address: 'House 73 St', lat: 35.7300, long: -119.2700, price: 473000, zpid: 73 },
    { address: 'House 74 St', lat: 35.7400, long: -119.2600, price: 474000, zpid: 74 },
    { address: 'House 75 St', lat: 35.7500, long: -119.2500, price: 475000, zpid: 75 },
    { address: 'House 76 St', lat: 35.7600, long: -119.2400, price: 476000, zpid: 76 },
    { address: 'House 77 St', lat: 35.7700, long: -119.2300, price: 477000, zpid: 77 },
    { address: 'House 78 St', lat: 35.7800, long: -119.2200, price: 478000, zpid: 78 },
    { address: 'House 79 St', lat: 35.7900, long: -119.2100, price: 479000, zpid: 79 },
    { address: 'House 80 St', lat: 35.8000, long: -119.2000, price: 480000, zpid: 80 },
    { address: 'House 81 St', lat: 35.8100, long: -119.1900, price: 481000, zpid: 81 },
    { address: 'House 82 St', lat: 35.8200, long: -119.1800, price: 482000, zpid: 82 },
    { address: 'House 83 St', lat: 35.8300, long: -119.1700, price: 483000, zpid: 83 },
    { address: 'House 84 St', lat: 35.8400, long: -119.1600, price: 484000, zpid: 84 },
    { address: 'House 85 St', lat: 35.8500, long: -119.1500, price: 485000, zpid: 85 },
    { address: 'House 86 St', lat: 35.8600, long: -119.1400, price: 486000, zpid: 86 },
    { address: 'House 87 St', lat: 35.8700, long: -119.1300, price: 487000, zpid: 87 },
    { address: 'House 88 St', lat: 35.8800, long: -119.1200, price: 488000, zpid: 88 },
    { address: 'House 89 St', lat: 35.8900, long: -119.1100, price: 489000, zpid: 89 },
    { address: 'House 90 St', lat: 35.9000, long: -119.1000, price: 490000, zpid: 90 },
    { address: 'House 91 St', lat: 35.9100, long: -119.0900, price: 491000, zpid: 91 },
    { address: 'House 92 St', lat: 35.9200, long: -119.0800, price: 492000, zpid: 92 },
    { address: 'House 93 St', lat: 35.9300, long: -119.0700, price: 493000, zpid: 93 },
    { address: 'House 94 St', lat: 35.9400, long: -119.0600, price: 494000, zpid: 94 },
    { address: 'House 95 St', lat: 35.9500, long: -119.0500, price: 495000, zpid: 95 },
    { address: 'House 96 St', lat: 35.9600, long: -119.0400, price: 496000, zpid: 96 },
    { address: 'House 97 St', lat: 35.9700, long: -119.0300, price: 497000, zpid: 97 },
    { address: 'House 98 St', lat: 35.9800, long: -119.0200, price: 498000, zpid: 98 },
    { address: 'House 99 St', lat: 35.9900, long: -119.0100, price: 499000, zpid: 99 },
    { address: 'House 100 St', lat: 36.0000, long: -119.0000, price: 500000, zpid: 100 },
    { address: 'House 101 St', lat: 36.0100, long: -118.9900, price: 501000, zpid: 101 },
    { address: 'House 102 St', lat: 36.0200, long: -118.9800, price: 502000, zpid: 102 },
    { address: 'House 103 St', lat: 36.0300, long: -118.9700, price: 503000, zpid: 103 },
    { address: 'House 104 St', lat: 36.0400, long: -118.9600, price: 504000, zpid: 104 },
    { address: 'House 105 St', lat: 36.0500, long: -118.9500, price: 505000, zpid: 105 },
    { address: 'House 106 St', lat: 36.0600, long: -118.9400, price: 506000, zpid: 106 },
    { address: 'House 107 St', lat: 36.0700, long: -118.9300, price: 507000, zpid: 107 },
    { address: 'House 108 St', lat: 36.0800, long: -118.9200, price: 508000, zpid: 108 },
    { address: 'House 109 St', lat: 36.0900, long: -118.9100, price: 509000, zpid: 109 },
    { address: 'House 110 St', lat: 36.1000, long: -118.9000, price: 510000, zpid: 110 },
    { address: 'House 111 St', lat: 36.1100, long: -118.8900, price: 511000, zpid: 111 },
    { address: 'House 112 St', lat: 36.1200, long: -118.8800, price: 512000, zpid: 112 },
    { address: 'House 113 St', lat: 36.1300, long: -118.8700, price: 513000, zpid: 113 },
    { address: 'House 114 St', lat: 36.1400, long: -118.8600, price: 514000, zpid: 114 },
    { address: 'House 115 St', lat: 36.1500, long: -118.8500, price: 515000, zpid: 115 },
    { address: 'House 116 St', lat: 36.1600, long: -118.8400, price: 516000, zpid: 116 },
    { address: 'House 117 St', lat: 36.1700, long: -118.8300, price: 517000, zpid: 117 },
    { address: 'House 118 St', lat: 36.1800, long: -118.8200, price: 518000, zpid: 118 },
    { address: 'House 119 St', lat: 36.1900, long: -118.8100, price: 519000, zpid: 119 },
    { address: 'House 120 St', lat: 36.2000, long: -118.8000, price: 520000, zpid: 120 },
    { address: 'House 121 St', lat: 36.2100, long: -118.7900, price: 521000, zpid: 121 },
    { address: 'House 122 St', lat: 36.2200, long: -118.7800, price: 522000, zpid: 122 },
    { address: 'House 123 St', lat: 36.2300, long: -118.7700, price: 523000, zpid: 123 },
    { address: 'House 124 St', lat: 36.2400, long: -118.7600, price: 524000, zpid: 124 },
    { address: 'House 125 St', lat: 36.2500, long: -118.7500, price: 525000, zpid: 125 },
    { address: 'House 126 St', lat: 36.2600, long: -118.7400, price: 526000, zpid: 126 },
    { address: 'House 127 St', lat: 36.2700, long: -118.7300, price: 527000, zpid: 127 },
    { address: 'House 128 St', lat: 36.2800, long: -118.7200, price: 528000, zpid: 128 },
    { address: 'House 129 St', lat: 36.2900, long: -118.7100, price: 529000, zpid: 129 },
    { address: 'House 130 St', lat: 36.3000, long: -118.7000, price: 530000, zpid: 130 },
    { address: 'House 131 St', lat: 36.3100, long: -118.6900, price: 531000, zpid: 131 },
    { address: 'House 132 St', lat: 36.3200, long: -118.6800, price: 532000, zpid: 132 },
    { address: 'House 133 St', lat: 36.3300, long: -118.6700, price: 533000, zpid: 133 },
    { address: 'House 134 St', lat: 36.3400, long: -118.6600, price: 534000, zpid: 134 },
    { address: 'House 135 St', lat: 36.3500, long: -118.6500, price: 535000, zpid: 135 },
    { address: 'House 136 St', lat: 36.3600, long: -118.6400, price: 536000, zpid: 136 },
    { address: 'House 137 St', lat: 36.3700, long: -118.6300, price: 537000, zpid: 137 },
    { address: 'House 138 St', lat: 36.3800, long: -118.6200, price: 538000, zpid: 138 },
    { address: 'House 139 St', lat: 36.3900, long: -118.6100, price: 539000, zpid: 139 },
    { address: 'House 140 St', lat: 36.4000, long: -118.6000, price: 540000, zpid: 140 },
    { address: 'House 141 St', lat: 36.4100, long: -118.5900, price: 541000, zpid: 141 },
    { address: 'House 142 St', lat: 36.4200, long: -118.5800, price: 542000, zpid: 142 },
    { address: 'House 143 St', lat: 36.4300, long: -118.5700, price: 543000, zpid: 143 },
    { address: 'House 144 St', lat: 36.4400, long: -118.5600, price: 544000, zpid: 144 },
    { address: 'House 145 St', lat: 36.4500, long: -118.5500, price: 545000, zpid: 145 },
    { address: 'House 146 St', lat: 36.4600, long: -118.5400, price: 546000, zpid: 146 },
    { address: 'House 147 St', lat: 36.4700, long: -118.5300, price: 547000, zpid: 147 },
    { address: 'House 148 St', lat: 36.4800, long: -118.5200, price: 548000, zpid: 148 },
    { address: 'House 149 St', lat: 36.4900, long: -118.5100, price: 549000, zpid: 149 },
    { address: 'House 150 St', lat: 36.5000, long: -118.5000, price: 550000, zpid: 150 },
    { address: 'House 151 St', lat: 36.5100, long: -118.4900, price: 551000, zpid: 151 },
    { address: 'House 152 St', lat: 36.5200, long: -118.4800, price: 552000, zpid: 152 },
    { address: 'House 153 St', lat: 36.5300, long: -118.4700, price: 553000, zpid: 153 },
    { address: 'House 154 St', lat: 36.5400, long: -118.4600, price: 554000, zpid: 154 },
    { address: 'House 155 St', lat: 36.5500, long: -118.4500, price: 555000, zpid: 155 },
    { address: 'House 156 St', lat: 36.5600, long: -118.4400, price: 556000, zpid: 156 },
    { address: 'House 157 St', lat: 36.5700, long: -118.4300, price: 557000, zpid: 157 },
    { address: 'House 158 St', lat: 36.5800, long: -118.4200, price: 558000, zpid: 158 },
    { address: 'House 159 St', lat: 36.5900, long: -118.4100, price: 559000, zpid: 159 },
    { address: 'House 160 St', lat: 36.6000, long: -118.4000, price: 560000, zpid: 160 },
    { address: 'House 161 St', lat: 36.6100, long: -118.3900, price: 561000, zpid: 161 },
    { address: 'House 162 St', lat: 36.6200, long: -118.3800, price: 562000, zpid: 162 },
    { address: 'House 163 St', lat: 36.6300, long: -118.3700, price: 563000, zpid: 163 },
    { address: 'House 164 St', lat: 36.6400, long: -118.3600, price: 564000, zpid: 164 },
    { address: 'House 165 St', lat: 36.6500, long: -118.3500, price: 565000, zpid: 165 },
    { address: 'House 166 St', lat: 36.6600, long: -118.3400, price: 566000, zpid: 166 },
    { address: 'House 167 St', lat: 36.6700, long: -118.3300, price: 567000, zpid: 167 },
    { address: 'House 168 St', lat: 36.6800, long: -118.3200, price: 568000, zpid: 168 },
    { address: 'House 169 St', lat: 36.6900, long: -118.3100, price: 569000, zpid: 169 },
    { address: 'House 170 St', lat: 36.7000, long: -118.3000, price: 570000, zpid: 170 },
    { address: 'House 171 St', lat: 36.7100, long: -118.2900, price: 571000, zpid: 171 },
    { address: 'House 172 St', lat: 36.7200, long: -118.2800, price: 572000, zpid: 172 },
    { address: 'House 173 St', lat: 36.7300, long: -118.2700, price: 573000, zpid: 173 },
    { address: 'House 174 St', lat: 36.7400, long: -118.2600, price: 574000, zpid: 174 },
    { address: 'House 175 St', lat: 36.7500, long: -118.2500, price: 575000, zpid: 175 },
    { address: 'House 176 St', lat: 36.7600, long: -118.2400, price: 576000, zpid: 176 },
    { address: 'House 177 St', lat: 36.7700, long: -118.2300, price: 577000, zpid: 177 },
    { address: 'House 178 St', lat: 36.7800, long: -118.2200, price: 578000, zpid: 178 },
    { address: 'House 179 St', lat: 36.7900, long: -118.2100, price: 579000, zpid: 179 },
    { address: 'House 180 St', lat: 36.8000, long: -118.2000, price: 580000, zpid: 180 },
    { address: 'House 181 St', lat: 36.8100, long: -118.1900, price: 581000, zpid: 181 },
    { address: 'House 182 St', lat: 36.8200, long: -118.1800, price: 582000, zpid: 182 },
    { address: 'House 183 St', lat: 36.8300, long: -118.1700, price: 583000, zpid: 183 },
    { address: 'House 184 St', lat: 36.8400, long: -118.1600, price: 584000, zpid: 184 },
    { address: 'House 185 St', lat: 36.8500, long: -118.1500, price: 585000, zpid: 185 },
    { address: 'House 186 St', lat: 36.8600, long: -118.1400, price: 586000, zpid: 186 },
    { address: 'House 187 St', lat: 36.8700, long: -118.1300, price: 587000, zpid: 187 },
    { address: 'House 188 St', lat: 36.8800, long: -118.1200, price: 588000, zpid: 188 },
    { address: 'House 189 St', lat: 36.8900, long: -118.1100, price: 589000, zpid: 189 },
    { address: 'House 190 St', lat: 36.9000, long: -118.1000, price: 590000, zpid: 190 },
    { address: 'House 191 St', lat: 36.9100, long: -118.0900, price: 591000, zpid: 191 },
    { address: 'House 192 St', lat: 36.9200, long: -118.0800, price: 592000, zpid: 192 },
    { address: 'House 193 St', lat: 36.9300, long: -118.0700, price: 593000, zpid: 193 },
    { address: 'House 194 St', lat: 36.9400, long: -118.0600, price: 594000, zpid: 194 },
    { address: 'House 195 St', lat: 36.9500, long: -118.0500, price: 595000, zpid: 195 },
    { address: 'House 196 St', lat: 36.9600, long: -118.0400, price: 596000, zpid: 196 },
    { address: 'House 197 St', lat: 36.9700, long: -118.0300, price: 597000, zpid: 197 },
    { address: 'House 198 St', lat: 36.9800, long: -118.0200, price: 598000, zpid: 198 },
    { address: 'House 199 St', lat: 36.9900, long: -118.0100, price: 599000, zpid: 199 },
    { address: 'House 200 St', lat: 37.0000, long: -118.0000, price: 600000, zpid: 200 },
    { address: 'House 201 St', lat: 37.0100, long: -117.9900, price: 601000, zpid: 201 },
    { address: 'House 202 St', lat: 37.0200, long: -117.9800, price: 602000, zpid: 202 },
    { address: 'House 203 St', lat: 37.0300, long: -117.9700, price: 603000, zpid: 203 },
    { address: 'House 204 St', lat: 37.0400, long: -117.9600, price: 604000, zpid: 204 },
    { address: 'House 205 St', lat: 37.0500, long: -117.9500, price: 605000, zpid: 205 },
    { address: 'House 206 St', lat: 37.0600, long: -117.9400, price: 606000, zpid: 206 },
    { address: 'House 207 St', lat: 37.0700, long: -117.9300, price: 607000, zpid: 207 },
    { address: 'House 208 St', lat: 37.0800, long: -117.9200, price: 608000, zpid: 208 },
    { address: 'House 209 St', lat: 37.0900, long: -117.9100, price: 609000, zpid: 209 },
    { address: 'House 210 St', lat: 37.1000, long: -117.9000, price: 610000, zpid: 210 },
    { address: 'House 211 St', lat: 37.1100, long: -117.8900, price: 611000, zpid: 211 },
    { address: 'House 212 St', lat: 37.1200, long: -117.8800, price: 612000, zpid: 212 },
    { address: 'House 213 St', lat: 37.1300, long: -117.8700, price: 613000, zpid: 213 },
    { address: 'House 214 St', lat: 37.1400, long: -117.8600, price: 614000, zpid: 214 },
    { address: 'House 215 St', lat: 37.1500, long: -117.8500, price: 615000, zpid: 215 },
    { address: 'House 216 St', lat: 37.1600, long: -117.8400, price: 616000, zpid: 216 },
    { address: 'House 217 St', lat: 37.1700, long: -117.8300, price: 617000, zpid: 217 },
    { address: 'House 218 St', lat: 37.1800, long: -117.8200, price: 618000, zpid: 218 },
    { address: 'House 219 St', lat: 37.1900, long: -117.8100, price: 619000, zpid: 219 },
    { address: 'House 220 St', lat: 37.2000, long: -117.8000, price: 620000, zpid: 220 },
    { address: 'House 221 St', lat: 37.2100, long: -117.7900, price: 621000, zpid: 221 },
    { address: 'House 222 St', lat: 37.2200, long: -117.7800, price: 622000, zpid: 222 },
    { address: 'House 223 St', lat: 37.2300, long: -117.7700, price: 623000, zpid: 223 },
    { address: 'House 224 St', lat: 37.2400, long: -117.7600, price: 624000, zpid: 224 },
    { address: 'House 225 St', lat: 37.2500, long: -117.7500, price: 625000, zpid: 225 },
    { address: 'House 226 St', lat: 37.2600, long: -117.7400, price: 626000, zpid: 226 },
    { address: 'House 227 St', lat: 37.2700, long: -117.7300, price: 627000, zpid: 227 },
    { address: 'House 228 St', lat: 37.2800, long: -117.7200, price: 628000, zpid: 228 },
    { address: 'House 229 St', lat: 37.2900, long: -117.7100, price: 629000, zpid: 229 },
    { address: 'House 230 St', lat: 37.3000, long: -117.7000, price: 630000, zpid: 230 },
    { address: 'House 231 St', lat: 37.3100, long: -117.6900, price: 631000, zpid: 231 },
    { address: 'House 232 St', lat: 37.3200, long: -117.6800, price: 632000, zpid: 232 },
    { address: 'House 233 St', lat: 37.3300, long: -117.6700, price: 633000, zpid: 233 },
    { address: 'House 234 St', lat: 37.3400, long: -117.6600, price: 634000, zpid: 234 },
    { address: 'House 235 St', lat: 37.3500, long: -117.6500, price: 635000, zpid: 235 },
    { address: 'House 236 St', lat: 37.3600, long: -117.6400, price: 636000, zpid: 236 },
    { address: 'House 237 St', lat: 37.3700, long: -117.6300, price: 637000, zpid: 237 },
    { address: 'House 238 St', lat: 37.3800, long: -117.6200, price: 638000, zpid: 238 },
    { address: 'House 239 St', lat: 37.3900, long: -117.6100, price: 639000, zpid: 239 },
    { address: 'House 240 St', lat: 37.4000, long: -117.6000, price: 640000, zpid: 240 },
    { address: 'House 241 St', lat: 37.4100, long: -117.5900, price: 641000, zpid: 241 },
    { address: 'House 242 St', lat: 37.4200, long: -117.5800, price: 642000, zpid: 242 },
    { address: 'House 243 St', lat: 37.4300, long: -117.5700, price: 643000, zpid: 243 },
    { address: 'House 244 St', lat: 37.4400, long: -117.5600, price: 644000, zpid: 244 },
    { address: 'House 245 St', lat: 37.4500, long: -117.5500, price: 645000, zpid: 245 },
    { address: 'House 246 St', lat: 37.4600, long: -117.5400, price: 646000, zpid: 246 },
    { address: 'House 247 St', lat: 37.4700, long: -117.5300, price: 647000, zpid: 247 },
    { address: 'House 248 St', lat: 37.4800, long: -117.5200, price: 648000, zpid: 248 },
    { address: 'House 249 St', lat: 37.4900, long: -117.5100, price: 649000, zpid: 249 },
    { address: 'House 250 St', lat: 37.5000, long: -117.5000, price: 650000, zpid: 250 },
    { address: 'House 251 St', lat: 37.5100, long: -117.4900, price: 651000, zpid: 251 },
    { address: 'House 252 St', lat: 37.5200, long: -117.4800, price: 652000, zpid: 252 },
    { address: 'House 253 St', lat: 37.5300, long: -117.4700, price: 653000, zpid: 253 },
    { address: 'House 254 St', lat: 37.5400, long: -117.4600, price: 654000, zpid: 254 },
    { address: 'House 255 St', lat: 37.5500, long: -117.4500, price: 655000, zpid: 255 },
    { address: 'House 256 St', lat: 37.5600, long: -117.4400, price: 656000, zpid: 256 },
    { address: 'House 257 St', lat: 37.5700, long: -117.4300, price: 657000, zpid: 257 },
    { address: 'House 258 St', lat: 37.5800, long: -117.4200, price: 658000, zpid: 258 },
    { address: 'House 259 St', lat: 37.5900, long: -117.4100, price: 659000, zpid: 259 },
    { address: 'House 260 St', lat: 37.6000, long: -117.4000, price: 660000, zpid: 260 },
    { address: 'House 261 St', lat: 37.6100, long: -117.3900, price: 661000, zpid: 261 },
    { address: 'House 262 St', lat: 37.6200, long: -117.3800, price: 662000, zpid: 262 },
    { address: 'House 263 St', lat: 37.6300, long: -117.3700, price: 663000, zpid: 263 },
    { address: 'House 264 St', lat: 37.6400, long: -117.3600, price: 664000, zpid: 264 },
    { address: 'House 265 St', lat: 37.6500, long: -117.3500, price: 665000, zpid: 265 },
    { address: 'House 266 St', lat: 37.6600, long: -117.3400, price: 666000, zpid: 266 },
    { address: 'House 267 St', lat: 37.6700, long: -117.3300, price: 667000, zpid: 267 },
    { address: 'House 268 St', lat: 37.6800, long: -117.3200, price: 668000, zpid: 268 },
    { address: 'House 269 St', lat: 37.6900, long: -117.3100, price: 669000, zpid: 269 },
    { address: 'House 270 St', lat: 37.7000, long: -117.3000, price: 670000, zpid: 270 },
    { address: 'House 271 St', lat: 37.7100, long: -117.2900, price: 671000, zpid: 271 },
    { address: 'House 272 St', lat: 37.7200, long: -117.2800, price: 672000, zpid: 272 },
    { address: 'House 273 St', lat: 37.7300, long: -117.2700, price: 673000, zpid: 273 },
    { address: 'House 274 St', lat: 37.7400, long: -117.2600, price: 674000, zpid: 274 },
    { address: 'House 275 St', lat: 37.7500, long: -117.2500, price: 675000, zpid: 275 },
    { address: 'House 276 St', lat: 37.7600, long: -117.2400, price: 676000, zpid: 276 },
    { address: 'House 277 St', lat: 37.7700, long: -117.2300, price: 677000, zpid: 277 },
    { address: 'House 278 St', lat: 37.7800, long: -117.2200, price: 678000, zpid: 278 },
    { address: 'House 279 St', lat: 37.7900, long: -117.2100, price: 679000, zpid: 279 },
    { address: 'House 280 St', lat: 37.8000, long: -117.2000, price: 680000, zpid: 280 },
    { address: 'House 281 St', lat: 37.8100, long: -117.1900, price: 681000, zpid: 281 },
    { address: 'House 282 St', lat: 37.8200, long: -117.1800, price: 682000, zpid: 282 },
    { address: 'House 283 St', lat: 37.8300, long: -117.1700, price: 683000, zpid: 283 },
    { address: 'House 284 St', lat: 37.8400, long: -117.1600, price: 684000, zpid: 284 },
    { address: 'House 285 St', lat: 37.8500, long: -117.1500, price: 685000, zpid: 285 },
    { address: 'House 286 St', lat: 37.8600, long: -117.1400, price: 686000, zpid: 286 },
    { address: 'House 287 St', lat: 37.8700, long: -117.1300, price: 687000, zpid: 287 },
    { address: 'House 288 St', lat: 37.8800, long: -117.1200, price: 688000, zpid: 288 },
    { address: 'House 289 St', lat: 37.8900, long: -117.1100, price: 689000, zpid: 289 },
    { address: 'House 290 St', lat: 37.9000, long: -117.1000, price: 690000, zpid: 290 },
    { address: 'House 291 St', lat: 37.9100, long: -117.0900, price: 691000, zpid: 291 },
    { address: 'House 292 St', lat: 37.9200, long: -117.0800, price: 692000, zpid: 292 },
    { address: 'House 293 St', lat: 37.9300, long: -117.0700, price: 693000, zpid: 293 },
    { address: 'House 294 St', lat: 37.9400, long: -117.0600, price: 694000, zpid: 294 },
    { address: 'House 295 St', lat: 37.9500, long: -117.0500, price: 695000, zpid: 295 },
    { address: 'House 296 St', lat: 37.9600, long: -117.0400, price: 696000, zpid: 296 },
    { address: 'House 297 St', lat: 37.9700, long: -117.0300, price: 697000, zpid: 297 },
    { address: 'House 298 St', lat: 37.9800, long: -117.0200, price: 698000, zpid: 298 },
    { address: 'House 299 St', lat: 37.9900, long: -117.0100, price: 699000, zpid: 299 },
    { address: 'House 300 St', lat: 38.0000, long: -117.0000, price: 700000, zpid: 300 },
    { address: 'House 301 St', lat: 38.0100, long: -116.9900, price: 701000, zpid: 301 },
    { address: 'House 302 St', lat: 38.0200, long: -116.9800, price: 702000, zpid: 302 },
    { address: 'House 303 St', lat: 38.0300, long: -116.9700, price: 703000, zpid: 303 },
  ];

  const mockOnSelect = jest.fn();

  beforeEach(() => {
    jest.clearAllMocks();
    
    // Mock the fetch response
    (global.fetch as jest.Mock).mockResolvedValue({
      ok: true,
      json: async () => ({ houses: mockHouses }),
    });

    // Mock the theme hook
    mockedUseTheme.mockReturnValue({ 
      theme: 'light', 
      systemTheme: 'light',
      setTheme: jest.fn(),
      resolvedTheme: 'light',
      themes: ['light', 'dark', 'system']
    } as any);
  });

  it('renders with loading state initially', () => {
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    const input = screen.getByPlaceholderText('Loading houses...');
    expect(input).toBeInTheDocument();
    expect(input).toBeDisabled();
  });

  it('fetches houses on mount and updates state', async () => {
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    // Wait for the loading state to finish
    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith('/api/locations');
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
  });

  it('filters houses based on search input', async () => {
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'elm' } });
    
    await waitFor(() => {
      expect(screen.getByText('456 Elm St')).toBeInTheDocument();
      expect(screen.queryByText('123 Main St')).not.toBeInTheDocument();
    });
  });

  it('calls onSelect when a house is selected', async () => {
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'main' } });
    
    await waitFor(() => {
      expect(screen.getByText('123 Main St')).toBeInTheDocument();
    });
    
    fireEvent.click(screen.getByText('123 Main St'));
    
    expect(mockOnSelect).toHaveBeenCalledWith(mockHouses[0]);
    expect(input).toHaveValue('123 Main St');
  });

  it('shows dropdown when input is focused and has value', async () => {
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'a' } });
    
    await waitFor(() => {
      expect(screen.getByText('123 Main St')).toBeInTheDocument();
      expect(screen.getByText('789 Oak Ave')).toBeInTheDocument();
    });
  });

  it('displays "No houses found" when search has no matches', async () => {
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'xyz' } });
    
    await waitFor(() => {
      expect(screen.getByText('No houses found')).toBeInTheDocument();
    });
  });

  it('handles API error gracefully', async () => {
    // Mock a failed API response
    (global.fetch as jest.Mock).mockResolvedValue({
      ok: false,
      status: 500
    });
    
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'a' } });
    
    await waitFor(() => {
      expect(screen.getByText('No houses found')).toBeInTheDocument();
    });
  });

  it('applies dark mode styling when theme is dark', async () => {
    // Mock dark theme
    mockedUseTheme.mockReturnValue({ 
      theme: 'dark', 
      systemTheme: 'dark',
      setTheme: jest.fn(),
      resolvedTheme: 'dark',
      themes: ['light', 'dark', 'system']
    } as any);
    
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'a' } });
    
    await waitFor(() => {
      const dropdown = screen.getByText('123 Main St').closest('div');
      expect(dropdown?.parentElement).toHaveClass('bg-card');
      expect(dropdown?.parentElement).toHaveClass('text-card-foreground');
    });
  });

  it('applies system theme when theme is set to system', async () => {
    // Mock system theme as dark
    mockedUseTheme.mockReturnValue({ 
      theme: 'system', 
      systemTheme: 'dark',
      setTheme: jest.fn(),
      resolvedTheme: 'dark',
      themes: ['light', 'dark', 'system']
    } as any);
    
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'a' } });
    
    await waitFor(() => {
      const dropdown = screen.getByText('123 Main St').closest('div');
      expect(dropdown?.parentElement).toHaveClass('bg-card');
      expect(dropdown?.parentElement).toHaveClass('text-card-foreground');
    });
  });

  it('handles invalid response format gracefully', async () => {
    // Mock a response with incorrect format
    (global.fetch as jest.Mock).mockResolvedValue({
      ok: true,
      json: async () => ({ notHouses: 'wrong format' }),
    });
    
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'a' } });
    
    await waitFor(() => {
      expect(screen.getByText('No houses found')).toBeInTheDocument();
    });
  });
});

