/* Something should be returned from the '/' page. */

var request = require('request');

describe('Basic suite', function() {
  it('has a really basic test', function() {
      expect(true).toBe(true);
  });
});

/*
it('should have the words "technology tree" from /', function(done) {
   request("localhost:8080", function(error, response, body) {
        expect(body).toContain('technology tree');
        done();
   });
});
*/
