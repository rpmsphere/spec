%define maj 0.9.8

Summary:	Secure Sockets Layer communications libs & utils
Name:		openssl%{maj}-spotify
Version:	0.9.8
Release:        1%{?dist}
License:	BSD-like
Group:		System/Libraries
URL:		http://www.openssl.org/
Source0:	ftp://ftp.openssl.org/source/openssl-%{version}y.tar.gz

BuildRequires:	zlib-devel perl openssl

%description
The openssl certificate management tool and the shared libraries that provide
various encryption and decription algorithms and protocols, including DES, RC4,
RSA and SSL.

NOTE: Only the shared library and the engines are provided with this source
rpm package.


%prep

%setup -q -n openssl-%{version}y

%build 

./config --prefix=/usr/share/spotify/ --openssldir=/usr/share/spotify/ssl --libdir=/usr/share/spotify/libs/ \
    shared zlib enable-md2 -Wa,--noexecstack

  make


%install

install -Dm755 libssl.so.0.9.8 %{buildroot}/usr/share/spotify/libs/libssl.so.0.9.8
install -Dm755 libcrypto.so.0.9.8 %{buildroot}/usr/share/spotify/libs/libcrypto.so.0.9.8



%files 
%{_datadir}/spotify/libs/libssl.so.0.9.8
%{_datadir}/spotify/libs/libcrypto.so.0.9.8

%changelog
* Fri Jan 24 2014 David Vásquez <davidjeremias82@gmail.com> - 0.9.8-1
- Initial build rpm

