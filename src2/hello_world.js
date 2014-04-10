var http = require('http');

var server = http.createServer(function(req, res) {
    res.writeHead(200);   // 200 is http OK code
    res.end('Hello HTTP');
});
server.listen(8080);
