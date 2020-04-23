SELECT TableDataKelompokUmur12.RW,TableDataKelompokUmur12.SE ,
       TableDataKelompokUmur13.SE ,
       TableDataKelompokUmur14.SE
       
FROM TableDataKelompokUmur12
LEFT JOIN TableDataKelompokUmur13 ,TableDataKelompokUmur14

ON TableDataKelompokUmur12.RW = TableDataKelompokUmur13.RW
AND TableDataKelompokUmur12.RW = TableDataKelompokUmur14.RW