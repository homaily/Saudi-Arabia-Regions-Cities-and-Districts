const fs = require('fs');
const regions = {
  1: {
    en: 'Riyadh',
    ar: 'الرياض',
  },
  2: {
    en: 'Makkah',
    ar: 'مكة المكرمة',
  },
  3: {
    en: 'Madinah',
    ar: 'المدينة المنورة',
  },
  4: {
    en: 'Qassim',
    ar: 'القصيم',
  },
  5: {
    en: 'Eastern Province',
    ar: 'الشرقية',
  },
  6: {
    en: 'Asir',
    ar: 'عسير',
  },
  7: {
    en: 'Tabuk',
    ar: 'تبوك',
  },
  8: {
    en: 'Hail',
    ar: 'حائل',
  },
  9: {
    en: 'Northern Borders',
    ar: 'الحدود الشمالية',
  },
  10: {
    en: 'Jizan',
    ar: 'جازان',
  },
  11: {
    en: 'Najran',
    ar: 'نجران',
  },
  12: {
    en: 'Bahah',
    ar: 'الباحة',
  },
  13: {
    en: 'Jawf',
    ar: 'الجوف',
  },
};

fs.readFile('./cities.json', 'utf8', (err, jsonString) => {
  if (err) {
      console.log("File read failed:", err);
      return;
  }

  const json = JSON.parse(jsonString);
  var regionsCities = {};
  json.forEach(city => {
    const region_id = city.region_id;
    delete city.region_id;

    if(!regionsCities[region_id])
      regionsCities[region_id] = {
        region: regions[region_id],
        cities: []
      };

    regionsCities[region_id]['cities'].push(city);
  });
  
  fs.writeFile('./ksaCitiesBasedOnRegion.json', JSON.stringify(regionsCities), err => {
    if (err) {
        console.log('Error writing file', err)
    } else {
        console.log('Successfully wrote file')
    }
});
  
});