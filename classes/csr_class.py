# csr_generator.py
"""
This script generates a Certificate Signing Request (CSR) for SSL certificates.
It uses the cryptography library to create the CSR based on user-provided information.

Usage:
    1. Instantiate the class with the required information.
    2. Call the `generate_csr` method to create the CSR.
    3. Optionally, write the CSR to a file.

Example:
    csr_generator = CsrGenerator(
        common_name="example.com",
        country="US",
        state="California",
        city="San Francisco",
        organization="Example Corp",
        organizational_unit="IT",
        email="admin@example.com"
    )
    csr, private_key = csr_generator.generate_csr()
    csr_generator.write_csr_to_file("example.csr", csr)
    csr_generator.write_key_to_file("private_key.pem", private_key)
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from cryptography.hazmat.primitives.serialization import BestAvailableEncryption
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.x509.oid import NameOID
import cryptography.x509 as x509


class CsrGenerator:
    def __init__(self, common_name, country, state, city, organization, organizational_unit, email):
        """
        Initialize the class with certificate details.

        :param common_name: Common Name (e.g., domain name)
        :param country: Country Name (e.g., 'US')
        :param state: State or Province Name (e.g., 'California')
        :param city: Locality Name (e.g., 'San Francisco')
        :param organization: Organization Name (e.g., 'Example Corp')
        :param organizational_unit: Organizational Unit Name (e.g., 'IT')
        :param email: Email Address (e.g., 'admin@example.com')
        """
        self.common_name = common_name
        self.country = country
        self.state = state
        self.city = city
        self.organization = organization
        self.organizational_unit = organizational_unit
        self.email = email

    def generate_csr(self):
        """
        Generate a Certificate Signing Request (CSR).

        :return: CSR and private key in PEM format.
        """
        # Generate a new private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )

        # Create the subject of the certificate
        subject = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, self.country),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, self.state),
            x509.NameAttribute(NameOID.LOCALITY_NAME, self.city),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, self.organization),
            x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, self.organizational_unit),
            x509.NameAttribute(NameOID.COMMON_NAME, self.common_name),
            x509.NameAttribute(NameOID.EMAIL_ADDRESS, self.email),
        ])

        # Build the CSR
        csr = x509.CertificateSigningRequestBuilder().subject_name(subject).sign(
            private_key, hashes.SHA256()
        )

        return csr.public_bytes(Encoding.PEM), private_key.private_bytes(
            Encoding.PEM,
            PrivateFormat.PKCS8,
            NoEncryption()
        )

    def write_csr_to_file(self, filename, csr_content):
        """
        Write the CSR to a file.

        :param filename: The name of the file to write the CSR to.
        :param csr_content: The CSR content to write to the file.
        """
        with open(filename, 'wb') as file:
            file.write(csr_content)
        print(f"CSR written to {filename}")

    def write_key_to_file(self, filename, key_content):
        """
        Write the private key to a file.

        :param filename: The name of the file to write the private key to.
        :param key_content: The private key content to write to the file.
        """
        with open(filename, 'wb') as file:
            file.write(key_content)
        print(f"Private key written to {filename}")


# Example usage:
# csr_generator = CsrGenerator(
#     common_name="example.com",
#     country="US",
#     state="California",
#     city="San Francisco",
#     organization="Example Corp",
#     organizational_unit="IT",
#     email="admin@example.com"
# )
# csr, private_key = csr_generator.generate_csr()
# csr_generator.write_csr_to_file("example.csr", csr)
# csr_generator.write_key_to_file("private_key.pem", private_key)
