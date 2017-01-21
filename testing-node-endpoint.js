var http = require('http');

var options = {
  host: "localhost",
  port: 5000,
  path: "/"
};

http.get(options, function(resp){
  resp.setEncoding('utf8');
  resp.on('data', function(chunk){
    chunk = JSON.parse(chunk);
    console.log(chunk["message"])
  });
}).on("error", function(e){
  console.log("Got error: " + e.message);
});