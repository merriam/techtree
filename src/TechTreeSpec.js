describe("TechTree", function() {
  it("Should pass a test", function() {
    expect(true).toBeTruthy();
  });

  /*
  it("Should fail this test", function() {
     expect(false).toBeTruthy();
  });
  */

  describe("the environment should be ready", function() {
     it("should pass a simple test", function() {
        expect(true).toBeTruthy();
     });
     it("should pass multiple tests", function() {
         expect(true).toBeTruthy();
     });
  });

  /* should have source files, have pings,  */
  /* should respond to basic fetches  */


/* This just here as examples...
  // demonstrates use of spies to intercept and test method calls
  it("tells the current song if the user has made it a favorite", function() {
    spyOn(song, 'persistFavoriteStatus');

    player.play(song);
    player.makeFavorite();

    expect(song.persistFavoriteStatus).toHaveBeenCalledWith(true);
  });

  //demonstrates use of expected exceptions
  describe("#resume", function() {
    it("should throw an exception if song is already playing", function() {
      player.play(song);

      expect(function() {
        player.resume();
      }).toThrowError("song is already playing");
    });
  });
*/
});
