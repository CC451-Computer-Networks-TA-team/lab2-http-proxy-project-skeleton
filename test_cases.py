import sys
from lab2_skeleton import check_http_request_validity, parse_http_request, HttpRequestState, HttpRequestInfo

#######################################
# Leave the code below as is. (Tests)
# Read them to know how your classes
# are used.
#######################################


def lineno():
    return sys._getframe().f_back.f_lineno


def simple_http_parsing_test_case():
    """
    Example test cases, do NOT modify this.

    If your code is correct, calling this function will have no effect.
    """
    client_addr = ("127.0.0.1", 9877)

    #######################################
    #######################################
    case = "Parse HTTP method."

    req_str = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"
    parsed = parse_http_request(client_addr, req_str)

    correct_value = "GET"
    actual_value = parsed.method
    assert correct_value == actual_value,\
        f"[Line {lineno()}] [failed] {case}"\
        " Expected ( %s ) got ( %s )" % (correct_value, actual_value)
    print(f"[success] {case}")

    #######################################
    case = "Parse headers."

    # "Host: google.edu" header is added to the request.
    # note that the ":" is removed.
    correct_value = ("Host", "www.google.edu")
    actual_value = parsed.headers[0]        # note: headers is a list of tuples
    assert correct_value == actual_value,\
        f"[Line {lineno()}] [failed] {case}"\
        " Expected ( %s ) got ( %s )" % (correct_value, actual_value)
    print(f"[success] {case}")

    #######################################
    case = "Parse HTTP request path."

    correct_value = "/"
    actual_value = parsed.requested_path
    assert correct_value == actual_value,\
        f"[Line {lineno()}] [failed] {case}"\
        " Expected ( %s ) got ( %s )" % (correct_value, actual_value)
    print(f"[success] {case}")

    #######################################
    case = "Add Default value of the port if it doesn't exist in the request."

    correct_value = str(80)
    actual_value = str(parsed.requested_port)
    assert correct_value == actual_value,\
        f"[Line {lineno()}] [failed] {case}"\
        " Expected ( %s ) got ( %s )" % (correct_value, actual_value)
    print(f"[success] {case}")

    #######################################
    case = "Add requested host field."

    correct_value = "www.google.com"
    actual_value = parsed.requested_host
    assert correct_value == actual_value,\
        f"[Line {lineno()}] [failed] {case}"\
        " Expected ( %s ) got ( %s )" % (correct_value, actual_value)
    print(f"[success] {case}")

    #######################################
    #######################################
    case = "Parse wrong HTTP method."

    # note, this is an invalid request, [parse_http_request] ONLY parses
    # the HTTP request and does NOT validate it.
    req_str = "GOAT http://www.google.edu/ HTTP/1.0\r\n\r\n"
    parsed = parse_http_request(client_addr, req_str)

    correct_value = "GOAT"
    actual_value = parsed.method
    assert correct_value == actual_value,\
        f"[Line {lineno()}] [failed] {case}"\
        " Expected ( %s ) got ( %s )" % (correct_value, actual_value)
    print(f"[success] {case}")

    #######################################
    case = "Convert full URL in request to relative path."

    correct_value = "/"
    actual_value = parsed.requested_path
    assert correct_value == actual_value,\
        f"[Line {lineno()}] [failed] {case}"\
        " Expected ( %s ) got ( %s )" % (correct_value, actual_value)
    print(f"[success] {case}")

    #######################################
    case = "Add host header if a full HTTP path is used in request."

    correct_value = ("Host", "www.google.edu")
    actual_value = parsed.headers[0]
    assert correct_value == actual_value,\
        f"[Line {lineno()}] [failed] {case}"\
        " Expected ( %s ) got ( %s )" % (correct_value, actual_value)
    print(f"[success] {case}")

    #######################################
    #######################################
    case = "Parse HTTP headers"

    req_str = "GET / HTTP/1.0\r\nHost: www.google.com\r\nAccept: application/json\r\n\r\n"
    parsed = parse_http_request(client_addr, req_str)

    correct_value = str(2)
    actual_value = str(len(parsed.headers))
    assert correct_value == actual_value,\
        f"[Line {lineno()}] [failed] {case}"\
        " Expected ( %s ) got ( %s )" % (correct_value, actual_value)
    print(f"[success] {case}")

    #######################################
    #######################################
    case = "convert HttpRequestInfo to a the corresponding HTTP request"
    # A request to www.google.com/ , note adding the ":" to headers
    # "Host" header comes first
    headers = [("Host", "www.google.com"), ("Accept", "application/json")]
    req = HttpRequestInfo(client_addr, "GET",
                          "www.google.com", 80, "/", headers)

    http_string = "GET / HTTP/1.0\r\nHost: www.google.com\r\n"
    http_string += "Accept: application/json\r\n\r\n"

    correct_value = http_string
    actual_value = req.to_http_string()
    assert correct_value == actual_value,\
        f"[Line {lineno()}] [failed] {case}"\
        " Expected ( %s ) got ( %s )" % (correct_value, actual_value)
    print(f"[success] {case}")


def simple_http_validation_test_case():
    client_addr = ("127.0.0.1", 9877)
    # Invalid input
    case = "Invalid HTTP verb returns INVALID_INPUT"
    req_str = "GOAT http://google.edu/ HTTP/1.0\r\nAccept: application/json\r\n\r\n"
    parsed = parse_http_request(client_addr, req_str)

    correct_value = HttpRequestState.INVALID_INPUT
    actual_value = check_http_request_validity(parsed)
    assert correct_value == actual_value,\
        f"[Line {lineno()}] [failed] {case}"\
        " Expected ( %s ) got ( %s )" % (correct_value.name, actual_value.name)
    print(f"[success] {case}")

    #######################################
    #######################################
    case = "PUT request returns NOT_SUPPORTED"
    req_str = "PUT http://google.edu/ HTTP/1.0\r\nAccept: application/json\r\n\r\n"
    parsed = parse_http_request(client_addr, req_str)

    # We only work with GET requests.
    correct_value = HttpRequestState.NOT_SUPPORTED
    actual_value = check_http_request_validity(parsed)
    assert correct_value == actual_value,\
        f"[Line {lineno()}] [failed] {case}"\
        " Expected ( %s ) got ( %s )" % (correct_value.name, actual_value.name)
    print(f"[success] {case}")

    #######################################
    #######################################
    case = "GET request with full URL in path returns GOOD"
    req_str = "GET http://google.edu/ HTTP/1.0\r\n"
    parsed = parse_http_request(client_addr, req_str)

    correct_value = HttpRequestState.GOOD
    actual_value = check_http_request_validity(parsed)
    assert correct_value == actual_value,\
        f"[Line {lineno()}] [failed] {case}"\
        " Expected ( %s ) got ( %s )" % (correct_value.name, actual_value.name)
    print(f"[success] {case}")

    #######################################
    #######################################
    case = "GET request with relative path and host header returns GOOD"
    req_str = "GET / HTTP/1.0\r\nHost: google.edu\r\n\r\n"
    parsed = parse_http_request(client_addr, req_str)

    correct_value = HttpRequestState.GOOD
    actual_value = check_http_request_validity(parsed)
    assert correct_value == actual_value,\
        f"[Line {lineno()}] [failed] {case}"\
        " Expected ( %s ) got ( %s )" % (correct_value.name, actual_value.name)
    print(f"[success] {case}")

    #######################################
    #######################################
    case = "Relative path without host header returns INVALID_INPUT"
    req_str = "GET / HTTP/1.0\r\n\r\n"
    parsed = parse_http_request(client_addr, req_str)

    correct_value = HttpRequestState.INVALID_INPUT
    actual_value = check_http_request_validity(parsed)
    assert correct_value == actual_value,\
        f"[Line {lineno()}] [failed] {case}"\
        " Expected ( %s ) got ( %s )" % (correct_value.name, actual_value.name)
    print(f"[success] {case}")


def main():
    ###################
    # Run tests
    ###################
    # Sorted by checklist order, feel free to comment/un-comment
    # any of those functions.
    try:
        simple_http_parsing_test_case()
        simple_http_validation_test_case()
    except AssertionError as e:
        print("Test case failed:\n", str(e))
        exit(-1)


if __name__ == "__main__":
    main()
