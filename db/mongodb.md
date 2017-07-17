Start mongo db
```
$ mongod
```

access to mongodb
```
$ mongo
```

Access to DB and collections
```
$ show bds
$ use blog
$ show collections
```

insert into db
```
> db.names.insert({'name':'Takuya Yamaguchi'});
> db.names.insertOne();
> db.names.insertMany();
```

find in db
```
$ db.names.find()
```

find
```
> db.movies.find().pretty()
> db.movies.find({'year': 1981}).pretty()
```

interect thought movies elements
```
> var m = db.movies.find()
> c.hasNext()
> c.next()
```

Change value and save
```
> var j = db.names.findOne()
> j.name = "takuya yamaguchi padilla"
> db.names.save(j)
```

db.students.createIndex({student_id:1})
db.students.createIndex({"class":1, "student_id":1})

**get indexes**
db.students.getIndexes()

**delete element**
db.students.dropIndex({student_id:1})

**explain query**
db.foo.explain.find({a:1, b:1})

**Multikey indexes (array indexes)**
can't create an index with array and array
db.foo.insert({a:1, b:1})
db.foo.createIndex({a:1, b:1})
db.foo.insert({a:1, b:[1,2,3]}) # multi index
db.foo.insert({a:[4,5,6], b:1}) # multi index
db.foo.insert({a:[4,5,6], b:[9,8,7]}) Error, coz we have a index in a, b

**dot notation**
dot notation and multi key
Create a index in value
db.students.createIndex({'scores.score':1})
# elemMatch match both condition
db.students.find({scores: {$elemMatch: {scores.type: "exam", scores.score:{'$gt':99.8}} }})
# and is one of the elements
db.students.find({scores: {$and: {scores.type: "exam", scores.score:{'$gt':99.8}} }})

**unique indexes**
db.stuff.insert({'thing': 'apple'})
db.stuff.createIndex({thing: 1})
# add unique key
db.stuff.createIndex({thing: 1}, {unique:true})
db.stuff.remove({thing: 'apple'}, {justOne: true})

**background** is slow but you can work when it's creating index
db.students.createIndex({'scores.score': 1}, {'background': true})

**explain**
db.foo.find().explain()
db.foo.explain().find()

var exp = db.example.explain()
exp.help()
exp.find({a:12, b:54}).sort({b:-1})

**Profiling**
queries that took longer than one second
db.system.profile.find( { millis : { $gt:1000 } } ).sort( { ts : -1 } )

**mongotop**
show top for mongo

**mongostat**
Which of the following statements about mongostat output are true? Check all that apply.
default column appears only in the mmapv1
