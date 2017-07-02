## Aggregation
```
use agg
db.products.aggregate([
  {$group: {
    _id: "$category",
    num_products:{$sum:1}
    }
  }
])
```
Group by multiple keys
```
use agg
db.products.aggregate([
  {$group: {
    _id: {
      "manufacturer": "$manufacturer",
      "category": "$category",
      }
    num_products:{$sum:1}
    }
  }
])
```
```
db.zips.aggregate([{"$group":{"_id":"$state", "population":{$sum:"$pop"}}}])
```
Average
```
use agg
db.products.aggregate([
    {$group:
     {
	 _id: {
	     "category":"$category"
	 },
	 avg_price:{$avg:"$price"}
     }
    }
])
```
addToSet
```
use agg
db.products.aggregate([
    {$group:
     {
	 _id: {
	     "maker":"$manufacturer"
	 },
	 categories:{$addToSet:"$category"}
     }
    }
])
```
```
db.zips.aggregate([{"$group":{"_id":"$city", "postal_codes":{$addToSet:"$_id"}}}])
```
Push
```
use agg
db.products.aggregate([
    {$group:
     {
	 _id: {
	     "maker":"$manufacturer"
	 },
	 categories:{$push:"$category"}
     }
    }
])
```
max
```
use agg
db.products.aggregate([
    {$group:
     {
	 _id: {
	     "maker":"$manufacturer"
	 },
	 maxprice:{$max:"$price"}
     }
    }
])
```
Match, group and project
```
db.zips.aggregate([
    {$match:
     {
	 state:"NY"
     }
    },
    {$group:
     {
	 _id: "$city",
	 population: {$sum:"$pop"},
	 zip_codes: {$addToSet: "$_id"}
     }
    },
    {$project:
     {
	 _id: 0,
	 city: "$_id",
	 population: 1,
	 zip_codes:1
     }
    }
])
```
