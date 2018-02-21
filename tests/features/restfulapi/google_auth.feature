Feature: Google authentication feature

  Background: Set base url and headers
    Given I set base URL to "context.base_url"
    And I set "Accept" header to "application/json"

  @test
  Scenario: Test scenario for invalid request
    When I make a GET request to "startsession"
    Then the response status code should equal 400
    And the response status message should equal "BAD REQUEST"
    And the response header "Content-Type" should equal "application/json"

  @test
  Scenario: Test scenario for invalid ID token
    When I make a GET request to "startsession" with parameters
    |id_token|
    |ABCinvalidtoken789|
    Then the response status code should equal 400
    And the response status message should equal "BAD REQUEST"
    And the response header "Content-Type" should equal "application/json"
    And the response parameter "error_description" should equal "Invalid Value"

  @test
  Scenario: Test scenario for valid ID token
    When I make a GET request to "startsession" with parameters
    |id_token|
    |XYZmyvalidtoken123|
    Then the response status code should equal 200
    And the response status message should equal "OK"
    And the response header "Content-Type" should equal "application/json"
    And the response parameter "status" should equal "logged_in"
