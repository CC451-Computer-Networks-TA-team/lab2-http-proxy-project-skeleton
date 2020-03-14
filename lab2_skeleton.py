# Don't forget to change this file's name before submission.
import sys
import os
# Abstract Base Class, incase you're wondering.
from abc import ABCMeta, abstractmethod


class HttpUnit(metaclass=ABCMeta):
    """
    A base class representing an interface for
    HTTP request / response that allows
    an object to become an HTTP string.
    """
    @abstractmethod
    def to_http_string(self):
        """
        Convert the HTTP request/response
        to a valid HTTP string.

        You still need to convert this string
        to byte array before sending it to the socket,
        keeping it as a string in this stage is to ease
        debugging and testing.
        """
        pass

    def to_byte_array(self, http_string):
        """
        Converts an HTTP string to a byte array.
        """
        return bytes(http_string, "UTF-8")


class HttpRequestInfo(HttpUnit):
    """
    A class that represents a HTTP request information

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


class HttpErrorResponse(HttpUnit):
    """
    Since you'll need to return some error messages in some
    cases, use this class to compose the HTTP error response, then
    call to_http_string() -> to_byte_array() on it before
    sending it to the socket.

    NOTE: you need to implement to_http_string() for this class.
    """

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message


class HttpProcessor(object):
    """
    Implements logic for an HTTP proxy server.
    The input to this object is a received HTTP message,
    the output is the packets to be written to the TCP sockets
    that are connected to the remote requested server.

    This class MUST NOT know anything about the existing sockets
    its input and outputs are byte arrays ONLY.

    Store the output packets in a buffer (some list) in this class
    the function get_next_output_packet returns the first item in
    the packets to be sent.

    This class is also responsible for reading/writing files to the
    hard disk.

    Failing to comply with those requirements will invalidate
    your submission.

    Feel free to add more functions to this class as long as
    those functions don't interact with sockets nor inputs from
    user/sockets. For example, you can add functions that you
    think they are "private" only. Private functions in Python
    start with an "_", check the example below
    """

    def __init__(self):
        """
        Add and initialize the *internal* fields you need.
        Do NOT change the arguments passed to this function.

        Here's an example of what you can do inside this function.
        """
        self.packet_buffer = []
        pass

    def process_input_request(self, input_request: HttpRequestInfo):
        """
        This function contains all your packet processing pipeline,
        call your functions here.

        Return a byetarray from this function
        """
        # add your other logic functions here. (like validation, ...etc)
        # return the errors here also (as bytearray)
        pass

    def _parse_http_packet(self, packet_bytes) -> HttpRequestInfo:
        """
        You'll use process the request using:
        - the struct module OR
        - string manipulation

        whichever you like, to determine the type of the request
        and extract other available information.

        This function does NOT check errors. It's not its responsibility
        """
        pass

    def process_http_packet(self, packet_data, packet_source):
        """
        Parse the input packet, execute your logic according to that packet.
        packet data is a bytearray, packet source contains the address
        information of the sender.

        Leave this function as is.
        """
        # Add your logic here, after your logic is done,
        # add the packet to be sent to self.packet_buffer
        # feel free to remove this line
        in_request = self._parse_http_packet(packet_data)

        print(f"Received a request from {packet_source}")
        print(f"Method: {in_request.method}")
        print(f"Host: {in_request.requested_host}")
        print(f"Port: {in_request.requested_port}")
        print("Headers:\n", ",".join(in_request.headers))

        # This shouldn't change.
        out_packet = self.process_input_request(in_request)
        self.packet_buffer.append(out_packet)

    def get_next_output_packet(self):
        """
        Returns the next packet that needs to be sent.
        This function returns a byetarray representing
        the next packet to be sent.

        For example;
        s_socket.send(http_processor.get_next_output_packet())

        Leave this function as is.
        """
        return self.packet_buffer.pop(0)

    def has_pending_packets_to_be_sent(self):
        """
        Returns if any packets to be sent are available.

        There should always be 1 or 0 packets in this list, since
        we're processing everything sequentially.

        Leave this function as is.
        """
        return len(self.packet_buffer) != 0


def check_file_name():
    """Checks if this file has a valid name for submission"""
    script_name = os.path.basename(__file__)
    import re
    matches = re.findall(r"(\d{4}_)lab2\.py", script_name)
    if not matches:
        print(f"[WARN] File name is invalid [{script_name}]")
    pass


def setup_sockets(proxy_port_number):
    """
    Socket logic MUST NOT be written in the HttpProcessor
    class. It knows nothing about the sockets.

    Feel free to delete this function.
    """
    print("Starting HTTP proxy on port:", proxy_port_number)

    # when calling socket.listen() pass a number
    # that's larger than 10.
    pass


def do_socket_logic():
    """
    Example function for some helper logic, in case you
    want to be tidy and avoid stuffing the main function.

    Feel free to delete this function.
    """
    pass


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
    # For a server, this means the IP that the server socket
    # will use.
    # The IP of the server.
    proxy_port_number = sys.argv[1]
    setup_sockets(proxy_port_number)


if __name__ == "__main__":
    main()
