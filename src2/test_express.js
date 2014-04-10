var express = require('express');
var app = express();

app.get('/', function(req,res) {
   res.send('This is the main page. Try a subpage');
});

app.get('/print', function(req, res) {
   res.send('This is the print page');
});

app.listen(3000);   // 3000 means what?
