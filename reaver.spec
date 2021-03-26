Name:           reaver
Version:        1.4
Release:        2.1
Summary:        Brute force attack against Wifi Protected Setup
License:        GPLv2
URL:            http://code.google.com/p/reaver-wps/
Source0:        http://reaver-wps.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:  libpcap-devel
BuildRequires:  sqlite-devel

%description
Reaver implements a brute force attack against Wifi Protected Setup (WPS)
registrar PINs in order to recover WPA/WPA2 passphrases, as described in
http://sviehb.files.wordpress.com/2011/12/viehboeck_wps.pdf.

Reaver has been designed to be a robust and practical attack against WPS, and
has been tested against a wide variety of access points and WPS
implementations.

On average Reaver will recover the target AP's plain text WPA/WPA2 passphrase
in 4-10 hours, depending on the AP. In practice, it will generally take half
this time to guess the correct WPS pin and recover the passphrase

%prep
%setup -q

%build
cd src
%configure
make %{?_smp_mflags}

%install
install -m 644 -D src/reaver.db $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/reaver.db
install -m 755 -D src/%{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}
install -m 644 -D docs/README $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}/README
install -m 644 -D docs/%{name}.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/%{name}.1.gz

%files
%{_bindir}/%{name}
%{_sysconfdir}/%{name}
%{_mandir}/man1/reaver.1.gz
%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jul 10 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuild for Fedora

* Fri Jun 08 2012 qmp <glang@lavabit.com> - 1.4-1
- New upstream version
- Removed "walsh" binary

* Sat Jan 14 2012 qmp <glang@lavabit.com> - 1.3-1
- Initial packaging
