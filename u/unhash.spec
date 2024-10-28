Name:         unhash
Summary:      MD5/SHA1 Brute-Force Cracking Utility
URL:          https://www.dxp2532.info/index.php?fid=tools
Group:        Cryptography
License:      GPL
Version:      2.0
Release:      9.1
Source0:      https://www.dxp2532.info/tools/unhash-%{version}.tbz
BuildRequires: openssl-devel

%description
UnHash is a program that tries a brute-force attack against a given
MD5 or SHA1 hash.

%prep
%setup -q

%build
%{__make} %{_smp_mflags} \
    CC="%{__cc}" \
    CFLAGS="%{optflags -O} %{optflags}" \
    LDFLAGS="%{optflags}" \
    LIBS="-ldl -lssl -lcrypto"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_bindir}
install -c -m 755 \
    unhash $RPM_BUILD_ROOT%{_bindir}

%files
%{_bindir}/%{name}

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
