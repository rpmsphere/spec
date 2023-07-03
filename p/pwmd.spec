Name:           pwmd
Version:        3.3.6
Release:        1
Summary:        A server for storing application data at a central location
License:        GPLv2+
URL:            https://bjk.sourceforge.net/pwmd/
Source0:        https://downloads.sourceforge.net/project/%{name}/%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  cracklib-devel
Buildrequires:  glib2-devel
Buildrequires:  gnutls-devel
BuildRequires:  libacl-devel
BuildRequires:  libassuan-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libubsan
BuildRequires:  libxml2-devel
BuildRequires:  zlib-devel
BuildRequires:  texinfo
BuildRequires:  gpgme-devel
Requires:       pinentry
#Source44:       import.info

%description
Password Manager Daemon is a server that provides a way for applications
to securely store and retrieve data at a centralized location. The data is
stored in an (optionally AES256 encrypted) XML file and clients connect and
send commands to manipulate the data. Some of the features include:

* Multi-threaded. More than one client may access the data at the same
  time.
* A key cache so clients won't need to enter a key each time a file is
  opened or saved.
* Key retrieval via pinentry(1).
* Configuration file which supports file specific settings including:
  encryption iterations, cache expiration and encryption key or key file
  and more.
* Compressed data file support.
* Logging to file and/or syslog.
* Secure memory usage. PWMD will zero out memory before freeing it and
  also has the option to lock the entire process in RAM to avoid swapping
  the data to virtual memory.

%prep
%setup -q -n %{name}-v%{version}

%build
./autogen.sh
%configure \
    --disable-static \
    --enable-gnutls \
    --enable-agent \
    --enable-quality \
    --enable-acl

#sed -i 's|-Wall|-Wall -Wl,--allow-multiple-definition|' Makefile */Makefile
%make_build

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}%{_infodir}/dir

%files
%doc KnownBugs NEWS README doc/config.example COPYING
%{_mandir}/man*/%{name}*.*
%{_infodir}/%{name}.info.*
%{_bindir}/%{name}*

%changelog
* Sun Apr 9 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 3.3.6
- Rebuilt for Fedora
* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.18-alt1_11
- new version
