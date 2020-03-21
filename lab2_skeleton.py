# Don't forget to change this file's name before submission.
import sys
import os
import enum
#########################
# Leave as is.
#########################


def get_arg(param_index, default=None):
    """
        Gets a command line argument by index (note: index starts from 1)
        If the argument is not supplies, it tries to use a default value.

        If a default value isn't supplied, an error message is printed
        and terminates the program.
    """
    try:
        return sys.argv[param_index]
    except IndexError as e:
        if default:
            return default
        else:
            print(e)
            print(
                f"[FATAL] The comand-line argument #[{param_index}] is missing")
            exit(-1)    # Program execution failed.


def check_file_name():
    """
    Checks if this file has a valid name for *submission*

    leave this function and as and don't use it. it's just
    to notify you if you're submitting a file with a correct
    name.
    """
    script_name = os.path.basename(__file__)
    import re
    matches = re.findall(r"(\d{4}_)lab2\.py", script_name)
    if not matches:
        print(f"[WARN] File name is invalid [{script_name}]")


class HttpRequestState(enum.Enum):
    """
    The values here have nothing to do with
    response values i.e. 400, 502, ..etc.

    Leave this as is, feel free to add yours.
    """
    BAD_REQUEST = 0
    NOT_IMPLEMENTED = 1
    GOOD = 2


#########################
#########################


class HttpRequestInfo(object):
    """
    Represents a HTTP request information

    Since you'll need to standardize all requests you get
    as specified by the document, after you parse the
    request from the TCP packet put the information you
    get in this object.

    To send the request to the remote server, call to_http_string
    on this object, convert that string to bytes then send it in
    the socket.

    client_address_info: address of the client;
    the client of the proxy, which sent the HTTP request.

    requested_host: the requested website, the remote website
    we want to visit.

    requested_port: port of the webserver we want to visit.

    requested_path: path of the requested resource, without
    including the website name.

    NOTE: you need to implement to_http_string() for this class.
    """

    def __init__(self, client_info, method: str, requested_host: str,
                 requested_port: int,
                 requested_path: str,
                 headers: list):
        self.method = method
        self.client_address_info = client_info
        self.requested_host = requested_host
        self.requested_port = requested_port
        self.requested_path = requested_path
        # Headers will be represented as a list of tuples
        # for example ("Host", "www.google.com")
        # if you get a header as:
        # "Host: www.google.com:80"
        # convert it to ("Host", "www.google.com") note that the
        # port is removed (because it goes into the request_port variable)
        self.headers = headers

    def to_http_string(self):
        """
        Convert the HTTP request/response
        to a valid HTTP string.
        As the protocol specifies:

        [request_line]\r\n
        [header]\r\n
        [headers..]\r\n
        \r\n

        You still need to convert this string
        to byte array before sending it to the socket,
        keeping it as a string in this stage is to ease
        debugging and testing.
        """

        print("*" * 50)
        print("[to_http_string] Implement me!")
        print("*" * 50)
        return None

    def to_byte_array(self, http_string):
        """
        Converts an HTTP string to a byte array.
        """
        return bytes(http_string, "UTF-8")

    def display(self):
        print(f"Client:", self.client_address_info)
        print(f"Method:", self.method)
        print(f"Host:", self.requested_host)
        print(f"Port:", self.requested_port)
        print("Headers:\n", "\n".join(self.headers))


class HttpErrorResponse(object):
    """
    Represents a proxy-error-response.
    """

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def to_http_string(self):
        """ Same as above """
        pass

    def to_byte_array(self, http_string):
        """
        Converts an HTTP string to a byte array.
        """
        return bytes(http_string, "UTF-8")

    def display(self):
        print(self.to_http_string())


def parse_http_request(source_addr, http_raw_data) -> HttpRequestInfo:
    """
    This function parses an HTTP request into an HttpRequestInfo
    object.

    it does NOT validate the HTTP request.
    """
    print("*" * 50)
    print("[parse_http_request] Implement me!")
    print("*" * 50)
    return None


def check_http_request_validity(http_request_info: HttpRequestInfo) -> HttpRequestState:
    """
    Checks if an HTTP response is valid

    returns:
    One of values in HttpRequestState
    """
    print("*" * 50)
    print("[check_http_request_validity] Implement me!")
    print("*" * 50)
    # return HttpRequestState.GOOD (for example)
    return None


def sanitize_http_request(request_info: HttpRequestInfo) -> HttpRequestInfo:
    """
    Puts an HTTP request on the sanitized (standard form)

    returns:
    A modified object of the HttpRequestInfo with
    sanitized fields

    for example, expand a URL to relative path + Host header.
    """
    print("*" * 50)
    print("[sanitize_http_request] Implement me!")
    print("*" * 50)
    return None


def http_request_pipeline(source_addr, http_raw_data):
    """
    HTTP request processing pipeline.

    - Parses the given HTTP request
    - Validates it
    - Returns a sanitized HttpRequestInfo or HttpErrorResponse
        based on request validity.

    returns:
     HttpRequestInfo if the request was parsed correctly.
     HttpErrorResponse if the request was invalid.

    Please don't remove this function, but feel
    free to change its content
    """
    # Parse HTTP request
    parsed = parse_http_request(source_addr, http_raw_data)

    # Validate, sanitize, return Http object.
    print("*" * 50)
    print("[http_request_pipeline] Implement me!")
    print("*" * 50)
    return None

#######################################
# write functions that deal
# with sockets and threading below.
# Feel free to add any functions you
# need.
#######################################


def entry_point(proxy_port_number):
    """
    Entry point, start your code here.

    Please don't delete this function,
    but feel free to modify the code
    inside it.
    """
    setup_sockets(proxy_port_number)
    print("*" * 50)
    print("[cleanup_tcp_socket_data] Implement me!")
    print("*" * 50)
    return None


def setup_sockets(proxy_port_number):
    """
    Socket logic MUST NOT be written in the any
    class. Classes know nothing about the sockets.

    But feel free to add your own classes/functions.

    Feel free to delete this function.
    """
    print("Starting HTTP proxy on port:", proxy_port_number)

    # when calling socket.listen() pass a number
    # that's larger than 10.
    print("*" * 50)
    print("[setup_sockets] Implement me!")
    print("*" * 50)
    return None


def do_socket_logic():
    """
    Example function for some helper logic, in case you
    want to be tidy and avoid stuffing the main function.

    Feel free to delete this function.
    """
    pass

#######################################
#######################################
# *********************************** #
#######################################
# Leave the code below as is.
#######################################


def simple_http_parsing_test_case():
    """
    Example test cases, do NOT modify this.

    If your code is correct, calling this function will have no effect.
    """
    req_str = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"
    parsed = parse_http_request(("127.0.0.1", 9877), req_str)
    correct_value = "GET"
    assert parsed.method == correct_value,\
        "[failed] HTTP method parsing. Expected [%s] got [%s]" %\
        (parsed.method, correct_value)
    print("[success] HTTP method parsing")
    # note: headers is a list of tuples
    host_header = parsed.headers[0]

    # "Host: google.edu" header is added to the request.
    # note that the ":" is removed.
    correct_value = ("Host", "google.edu")
    assert correct_value == host_header, "[failed] HTTP path extraction." +\
        " Expected: [%s] got [%s]" % (correct_value, host_header)
    print("[success] HTTP path extraction")

    assert "/" == parsed.requested_path, "[failed] HTTP path parsing." +\
        " Expected [%s] got [%s]" % ("/", parsed.requested_path)
    print("[success] HTTP path parsing")

    # Default value of the port if it doesn't exist.
    assert 80 == parsed.requested_port, "[failed] HTTP port parsing." +\
        " Expected [%s] got [%s]" % (80, parsed.requested_port)
    print("[success] HTTP  port parsing")

    #######################################
    #######################################

    req_str = "GET / HTTP/1.0\r\nHost: www.google.com\r\nAccept: application/json\r\n\r\n"
    parsed = parse_http_request(("127.0.0.1", 9877), req_str)
    # note, this is an invalid request, [parse_http_request] ONLY parses
    # the HTTP request and does NOT validate it.
    req_str = "GOAT http://google.edu/ HTTP/1.0\r\n\r\n"
    parsed = parse_http_request(("127.0.0.1", 9877), req_str)

    # assert means "check"
    correct_value = "GOAT"
    assert parsed.method == correct_value,\
        "[failed] HTTP method parsing. Expected [%s] got [%s]" %\
        (parsed.method, correct_value)

    assert parsed.requested_path == "/",  "[failed] HTTP path parsing. " +\
        "(URL isn't transformed)"\
        " Expected [%s] got [%s]" % ("/", parsed.requested_path)
    print("[success] HTTP path parsing")

    correct_value = 2
    assert correct_value == len(parsed.headers), "[failure] header count." +\
        " Expected [%d] got [%d]" % (correct_value, len(parsed.headers))
    print("[success] HTTP header count")

    # A request to www.google.com/ , note adding the ":" to headers
    # "Host" header comes first
    headers = [("Host", "www.google.com"), ("Accept", "application/json")]
    req = HttpRequestInfo(("127.0.0.1", 9877), "GET",
                          "www.google.com", 80, "/", headers)

    #######################################
    #######################################

    http_string = "GET / HTTP/1.0\r\nHost: www.google.com\r\n"
    http_string += "Accept: application/json\r\n\r\n"
    assert req.to_http_string() == http_string, \
        "[failed] convert HttpRequestInfo to a valid HTTP request"
    print("[success] convert HttpRequestInfo to a valid HTTP request")


def simple_http_validation_test_case():
    # Invalid input
    req_str = "GOAT http://google.edu/ HTTP/1.0\r\nAccept: application/json\r\n\r\n"
    parsed = parse_http_request(("127.0.0.1", 9877), req_str)

    assert parsed.method == "GOAT", "[failed] HTTP method parsing"
    print("[success] HTTP method parsing")

    assert check_http_request_validity(
        parsed) == HttpRequestState.BAD_REQUEST, "[failed] HTTP validation"
    print("[success] HTTP validation")

    req_str = "PUT http://google.edu/ HTTP/1.0\r\nAccept: application/json\r\n\r\n"
    parsed = parse_http_request(("127.0.0.1", 9877), req_str)
    assert parsed.method == "PUT", "[failed] HTTP method parsing"
    print("[success] HTTP method parsing")

    # We only work with GET requests.
    assert check_http_request_validity(
        parsed) == HttpRequestState.NOT_IMPLEMENTED, "[failed] recognizing invalid HTTP verbs"
    print("[success] recognizing invalid HTTP verbs")

    req_str = "GET http://google.edu/ HTTP/1.0\r\n"
    assert check_http_request_validity(
        parsed) == HttpRequestState.GOOD, "[failed] recognizing valid HTTP verb"
    print("[success] recognizing valid HTTP verb")

    req_str = "GET / HTTP/1.0\r\nHost: google.edu\r\n\r\n"
    assert check_http_request_validity(
        parsed) == HttpRequestState.GOOD, "[failed] recognizing valid HTTP verb"
    print("[success] recognizing valid HTTP verb")

    # Host header isn't included
    req_str = "GET / HTTP/1.0\r\n\r\n"
    assert check_http_request_validity(
        parsed) == HttpRequestState.BAD_REQUEST, "[failed] recognizing valid HTTP verb"
    print("[success] recognizing valid HTTP verb")


def main():
    """
    Please leave the code in this function as is.

    To add code that uses sockets, feel free to add functions
    above main and outside the classes.
    """
    print("*" * 50)
    print(f"[LOG] Printing command line arguments [{', '.join(sys.argv)}]")
    check_file_name()
    print("*" * 50)

    # This argument is required.
    proxy_port_number = sys.argv[1]
    ###################
    # Run tests?
    ###################
    run_tests = False    # Change this value
    if run_tests:
        # Sorted by checklist order, feel free to comment/un-comment
        # those functions.
        simple_http_parsing_test_case()
        simple_http_validation_test_case()

    entry_point(proxy_port_number)


if __name__ == "__main__":
    main()
