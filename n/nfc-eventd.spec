Name:           nfc-eventd
Summary:        NFC event daemon
License:        GPL-3.0+
Group:          Hardware/Other
Version:        0.1.7
Release:        2.1
URL:            http://nfc-tools.org/
Source:         %name-%version.tar.xz
BuildRequires:  libnfc-devel

%description
nfc-eventd is a daemon that looks for tags insertions/removes from
NFC device. It is provided with two NEM (Nfc Eventd Modules) which
allow many kind of usage of theses events.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete

%files
%config %_sysconfdir/nfc-eventd.conf
%_bindir/nfc-eventd
%_libdir/%name

%changelog
* Fri Jul 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.7
- Rebuild for Fedora
* Fri Jun 28 2013 jengelh@inai.de
- Update to new upstream release 0.1.7
  * Support the libnfc-1.7.0 API
* Fri May 31 2013 jengelh@inai.de
- Update to new upstream snapshot 0.1.5+svn1129
  * Check return value in an internal call
* Sun Jun 24 2012 jengelh@inai.de
- Initial package for build.opensuse.org
