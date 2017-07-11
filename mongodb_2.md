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
$project
```
db.products.aggregate([
    {$project:
     {
	 _id:0,
	 'maker': {$toLower:"$manufacturer"},
	 'details': {'category': "$category",
		     'price' : {"$multiply":["$price",10]}
		    },
	 'item':'$name'
     }
    }
])

db.zips.aggregate([{$project:{_id:0, city:{$toLower:"$city"}, pop:1, state:1, zip:"$_id"}}])
```
$match
```
db.zips.aggregate([
    {$match:
     {
	 state:"NY"
     }
    }
])
```
match and group
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
    }
])
```
