Detect Data Leaks (Example)
######################################
Security leak detection automation is an automated process that aims to detect security leaks in telemetry binaries.

The goal of the automated security leak detection tests is to ensure that
    1. No critical security parameter (CSP) shall be part of telemetry logs in any form, including encrypted
    #. No CSP shall leave the production device in any form, including encrypted
    #. Security leaks in telemetry logs, if any are detected, are addressed in a timely manner
    #. The manual security leak analysis effort is minimized
    #. For a list of sensitive data, please refer to Data Control classification.

To automate the security leak detection tests only detect leaks from the run-time generated security keys and Random Number Generator (RNG) data, which is the most difficult part to automate and is made possible for automation with instrumentation.

There are other sensitive data in sensitive data that we don't have security leak tests for yet, such as user data, ID, Opal password, etc. Sensitive data can be set to known in the test, it is easy to develop tests for them without the need of instrumentation.

Instruments the key generation, DRBG (random data generation), key wrapping, and key unwrapping operations to force a known pattern instead of a random number. We can then search for this known pattern in the telemetry logs to identify any security leaks. The pattern can represent any potential customer data as well.

.. code-block:: python

    import re, ctypes, binascii

    class MetaDataStructure(Structure):
        _fields_ = [("metaData", ctypes.c_byte()*sizeof(Structure)]

    def searchSecurityLeak(metaData, pattern = '\xE7', repeatCount = 32)
    """
    Brief:
        searchSecurityLeak() - Scan the telemetry log for security leaks

    Description:
        In order to use this method to search for security leaks in telemetry log, security pattern injection has to be enabled on side first. Once that's done, we can search the pre-defined fixed pattern in the telemetry log to identify if there's any security leaks in the log.

    Return Value(s):
        True if security leaks are detected in the telemetry log
        False if no security leaks are detected in the telemetry log
    """
    # The pattern below needs to match the pattern on side when security pattern injection is enabled on side
    SECURITY_PATTERN = pattern
    # Minimum length in bytes of security keys or random data generated on side
    REPEATED_BYTES = repeatCount
    data = bytearray(metaData)

    # I.E regular expression '(\xE7){32}' representing 32 bytes of 0xE7
    # search 32 continuous bytes of E7 in the telemetry log for security leaks
    regPattern = '({}){{{}}}'.format(SECURITY_PATTERN, REPEATED_BYTES)
    regex = re.compile(regPattern)
    result = False
    # Find all non-overlapping matched instances in the log and
    # print out the byte offset in the log of the matched instances
    # Which are the security leaks
    for matchedInstance in regex.finditer(data):
        result = True
        byteOffset = matchedInstance.start()
        print("Found security leak pattern ({} bytes of {}) at byte offset {}".format(REPETED_BYTES, '0x' + binascii.b2a_hex(SECURITY_PATTERN), hex(byteOffset)))
    return result
